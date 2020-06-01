# coding=utf-8
# 2016, all rights reserved
import datetime
import hashlib
import json
import os
# import sys
import uuid
import warnings

import PySimpleGUI as sg
import openpyxl
import requests
import unicodecsv as csv
from decouple import config

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


# def resource_path(relative_path):
#     if hasattr(sys, "_MEIPASS"):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("."), relative_path)


def month_iterator(initial_date, finish_date):
    current_date = initial_date.replace(day=1)
    while current_date <= finish_date:
        yield current_date
        current_date += datetime.timedelta(days=32)
        current_date = current_date.replace(day=1)


def main(eMail, senha, meses, extensao, year=2020, last_year=None, last_month=None):
    """Download GuiaBolso transactions in a csv format."""
    guiabolso = GuiaBolso(eMail, senha)
    initial_date = datetime.date(year, meses, 1)
    finish_date = datetime.date(last_year or year, last_month or meses, 1)
    for date in month_iterator(initial_date, finish_date):
        year = date.year
        meses = date.month
        filename = f"{year}-{meses}"
        if extensao == "xlsx":
            filename += ".xlsx"
            guiabolso.xlsx_transactions(year, meses, filename)
        elif extensao == "txt":
            filename += ".txt"
            guiabolso.txt_transactions(year, meses, filename)
        else:
            filename += ".csv"
            guiabolso.csv_transactions(year, meses, filename)
        print(filename)


def get_month_count(year=None, meses=None):
    today = datetime.date.today()
    if year is None:
        year = today.year
    if meses is None:
        meses = today.month
    return year * 12 + meses - 1


class GuiaBolso:
    def __init__(self, eMail, senha):
        self.email = eMail
        self.password = senha
        hardware_address = str(uuid.getnode()).encode("utf-8")
        self.device_token = hashlib.md5(hardware_address).hexdigest()
        self.session = requests.Session()
        self.token = self.login()
        basic_info = self.get_basic_info()
        # variables common
        self.categories = basic_info["categoryTypes"]
        self.statements = basic_info["accounts"]
        self.fieldnames = [
            "id",
            "label",
            "description",
            "date",
            "account",
            "category",
            "subcategory",
            "duplicated",
            "currency",
            "value",
            "deleted",
        ]
        self.category_resolver = {}
        for categ in self.categories:
            for sub_categ in categ["categories"]:
                self.category_resolver[sub_categ["id"]] = (
                    categ["name"],
                    sub_categ["name"],
                )

        self.account_resolver = {}
        for account in self.statements:
            for sub_account in account["statements"]:
                self.account_resolver[sub_account["id"]] = sub_account["name"]

    def login(self):
        url = "https://www.guiabolso.com.br/comparador/v2/events/others"
        payload = """
        {
             "name":"web:users:login",
             "version":"1",
             "payload":{"email":%s,
                        "pwd":%s,
                        "userPlatform":"GUIABOLSO",
                        "deviceToken":"%s",
                        "os":"Windows",
                        "appToken":"1.1.0",
                        "deviceName":"%s"},
             "flowId":"","id":"",
             "auth":{"token":"","x-sid":"","x-tid":""},
             "metadata":{"origin":"web",
                         "appVersion":"1.0.0",
                         "createdAt":"2020-04-24T23:20:05.552Z"},
             "identity":{}
        }""" % (
            json.dumps(self.email),
            json.dumps(self.password),
            self.device_token,
            self.device_token,
        )
        headers = {"content-type": "application/json"}
        response = self.session.post(url, headers=headers, data=payload).json()
        if response["name"] != "web:users:login:response":
            print(response["name"])
            raise Exception(response["payload"]["code"])
        return response["auth"]["token"]

    def get_basic_info(self):
        url = "https://www.guiabolso.com.br/comparador/v2/events/"
        headers = {"content-type": "application/json"}
        payload = """
        {
            "name":"rawData:info",
            "version":"6",
            "payload":{"userPlatform":"GUIABOLSO",
                       "appToken":"1.1.0",
                       "os":"Win32"},
            "flowId":"",
            "id":"",
            "auth":{"token":"Bearer %s",
                    "sessionToken":"%s",
                    "x-sid":"",
                    "x-tid":""},
            "metadata":{"origin":"web",
                        "appVersion":"1.0.0",
                        "createdAt":""},
            "identity":{}
        }""" % (
            self.token,
            self.token,
        )
        response = self.session.post(url, headers=headers, data=payload).json()
        d = {
            "categoryTypes": response["payload"]["categoryTypes"],
            "accounts": response["payload"]["accounts"],
        }
        return dict(d)

    def json_transactions(self, year, meses):
        month_count = get_month_count(year, meses)
        url = "https://www.guiabolso.com.br/comparador/v2/events/"
        headers = {"content-type": "application/json"}
        payload = """
        {
             "name":"users:summary:month",
             "version":"1",
             "payload":{"userPlatform":"GUIABOLSO",
                        "appToken":"1.1.0",
                        "os":"Win32",
                        "monthCode":%i},
             "flowId":"",
             "id":"",
             "auth":{"token":"Bearer %s",
                     "sessionToken":"%s",
                     "x-sid":"",
                     "x-tid":""},
             "metadata":{"origin":"web",
                         "appVersion":"1.0.0",
                         "createdAt":"2020-04-25T20:20:05.552Z"},
             "identity":{}
        }""" % (
            month_count,
            self.token,
            self.token,
        )
        response = self.session.post(url, headers=headers, data=payload)
        return response

    def transactions(self, year, meses):
        transactions_new = []
        transactions = self.json_transactions(year, meses).json()
        for statement in transactions["payload"]["userMonthHistory"]["statements"]:
            for t in statement["transactions"]:
                cat_id = t["categoryId"]
                t["category"], t["subcategory"] = self.category_resolver[cat_id]
                t["account"] = self.account_resolver.get(
                    t["statementId"], t["statementId"]
                )
                unwanted_keys = set(t) - set(self.fieldnames)

                for k in unwanted_keys:
                    del t[k]
                transactions_new.append(t)

        return transactions_new

    def csv_transactions(self, year, meses, file_name):
        transactions = self.transactions(year, meses)

        if len(transactions) == 0:
            warnings.warn(f"No transactions for the period ({year}-{meses})")
            return

        with open(file_name, "wb") as f:
            csv_writer = csv.DictWriter(
                f, fieldnames=self.fieldnames, encoding="utf-8-sig"
            )  # add BOM to csv
            csv_writer.writeheader()
            csv_writer.writerows(transactions)

    def xlsx_transactions(self, year, meses, file_name):
        transactions = self.transactions(year, meses)

        if len(transactions) == 0:
            warnings.warn("No transactions for the period ({}-{})".format(year, meses))
            return

        wb = openpyxl.Workbook()
        ws = wb.active

        ws.append(self.fieldnames)

        for trans in transactions:
            if "date" in trans:
                trans["date"] = datetime.datetime.fromtimestamp(
                    trans["date"] / 1000
                ).date()
            row = [trans[k] for k in self.fieldnames]
            ws.append(row)

        wb.save(file_name)

    def txt_transactions(self, year, meses, file_name):
        transactions = self.transactions(year, meses)
        transactions = sorted(transactions, key=lambda d: d["date"])

        if len(transactions) == 0:
            warnings.warn(f"No transactions for the period ({year}-{meses})")
            return
        paipline = "|".center(5, "-")
        homepath = os.path.expanduser(os.getenv("USERPROFILE"))
        desktoppath = "Desktop"
        local_save = os.path.join(homepath, desktoppath, file_name)
        list_subcategory_ignorade = [
            "Pagamento de cartão",
            "Taxas bancárias",
            "TV / Internet / Telefone",
            "Impostos",
            "Saques",
            "Juros",
            "Remuneração",
            "Transferência",
            "Boletos",
            "Outros gastos",
        ]
        with open(local_save, "w", encoding="utf8") as _file:
            for conta in transactions:
                if conta["subcategory"] not in list_subcategory_ignorade:
                    data = datetime.datetime.fromtimestamp(conta["date"] / 1000).date()
                    content = f"""{data} {paipline} {conta['label'].ljust(51, ' ')} {paipline}{str(conta['value'])[1:].rjust(8, ' ')}{paipline} {conta['subcategory']} """
                    print(content)
                    _file.write(content)
                    _file.write("\n")


class Tela:
    def __init__(self):
        self.months = [
            {1: "Janeiro"},
            {2: "Fevereiro"},
            {3: "Março"},
            {4: "Abril"},
            {5: "Maio"},
            {6: "Junho"},
            {7: "Julho"},
            {8: "Agosto"},
            {9: "Setembro"},
            {10: "Outubro"},
            {11: "Novembro"},
            {12: "Dezembro"},
        ]

    def layout_inicial(self):
        layout = [
            [sg.T("Escolha o mês")],
            [
                sg.Combo(
                    self.months, size=(20, 12), enable_events=False, key="choicemonth"
                )
            ],
            [
                sg.Frame(
                    layout=[
                        [
                            sg.Radio(
                                "TXT", "RADIO1", key="txt", default=True, size=(10, 1)
                            ),
                            sg.Radio("XLSX", "RADIO1", key="xlsx"),
                            sg.Radio("CSV", "RADIO1", key="csv"),
                        ]
                    ],
                    title="Qual extensão?",
                    title_color="yellow",
                    relief=sg.RELIEF_SUNKEN,
                    tooltip="Use these to set flags",
                )
            ],
            [sg.Cancel(), sg.OK()],
        ]
        window = sg.Window("Guia Bolso", grab_anywhere=False).Layout(layout)
        event, values = window.read()
        window.close()
        if event == "OK":
            radio_selected = [v[0] for v in values.items() if v[1] is True][0]
            return values["choicemonth"], radio_selected
        else:
            return None


if __name__ == "__main__":
    email = config("GUIABOLSO_EMAIL")
    password = config("GUIABOLSO_PASSWORD")
    telas = Tela()
    gb = GuiaBolso(email, password)
    month, extension = telas.layout_inicial()
    main(email, password, list(month)[0], extension)
    # resource_path("myimage.gif")

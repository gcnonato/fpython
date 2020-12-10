#!/usr/bin/python3
import urllib.request
from datetime import datetime

import PySimpleGUI as sg
from parsel import Selector
from requests import post


class DiarioOficial:
    def __init__(self, month, url, year=2020):
        self.year = year
        self.month = month
        self.response = ""
        self.url = url
        self.url_base = "http://www.imprensaoficial.com.br"
        self.cookies = {
            "PortalIOJoyRide": "ridden",
            "ASP.NET_SessionId": "xwgb4pqwuwvdxwwjricfy0r3",
            "_ga": "GA1.3.343843048.1589019110",
            "_gid": "GA1.3.946827584.1589019110",
            "PortalIOIntro": "OK",
            "_gat_gtag_UA_129106988_1": "1",
        }
        self.headers = {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "http://www.imprensaoficial.com.br",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                      "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "http://www.imprensaoficial.com.br/DO/"
                       "BuscaDO2001Resultado_11_3.aspx?filtropalavraschave=24311856&f="
                       "xhitlist&xhitlist_vpc=first&xhitlist_x=Advanced&xhitlist_q="
                       "(24311856)&xhitlist_mh=9999&filtrotipopalavraschavesalvar=UP&filtrotodoscadernos="
                       "True&xhitlist_hc=%5bXML%5d%5bKwic%2c3%5d&xhitlist_vps=15&xhitlist_xsl=xhitlist.xsl&xhitlist_s="
                       "&xhitlist_sel=title%3bField%3adc%3atamanho%3bField%3adc%3adatapubl%3bField%3adc%3acaderno%3"
                       "bitem-bookmark%3bhit-context",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        self.params = (
            ("filtropalavraschave", "24311856"),
            ("f", "xhitlist"),
            ("xhitlist_vpc", "first"),
            ("xhitlist_x", "Advanced"),
            ("xhitlist_q", "(24311856)"),
            ("xhitlist_mh", "9999"),
            ("filtrotipopalavraschavesalvar", "UP"),
            ("filtrotodoscadernos", "True"),
            ("xhitlist_hc", "[XML][Kwic,3]"),
            ("xhitlist_vps", "15"),
            ("xhitlist_xsl", "xhitlist.xsl"),
            ("xhitlist_s", ""),
            (
                "xhitlist_sel",
                "title;Field:dc:tamanho;Field:dc:datapubl;Field:dc:caderno;item-bookmark;hit-context",
            ),
        )
        self.data = {
            "__EVENTTARGET": "ctl00$content$Coluna$Navegadores$dtlNavegadores$ctl02$ctl05",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR": "BDCE6B05",
            "__EVENTVALIDATION": "",
            "ctl00$content$txt_nav": f"anonavigator|{self.year}",
            "ctl00$content$BuscaSimples$txtPalavrasChave": "24311856",
        }
        self.response = post(
            self.url,
            headers=self.headers,
            params=self.params,
            cookies=self.cookies,
            data=self.data,
        )

    def encurtador_urls(self, url):
        apiurl = "http://tinyurl.com/api-create.php?url="
        tinyurl = urllib.request.urlopen(apiurl + url).read()
        return tinyurl.decode("utf-8")

    def scrapy(self):
        parsel = Selector(text=self.response.text)
        list_urls = []
        for luciano in parsel.xpath("//b[contains(text(), '24311856')]"):
            url_extract = luciano.xpath("ancestor-or-self::a/@href").get()
            url_extract = "".join(url_extract.split(" "))
            url_download = "".join([self.url_base, url_extract])
            url_download = self.encurtador_urls(url_download)
            for nome in (
                "".join(
                    [e for e in luciano.xpath("ancestor-or-self::a/text()").getall()]
                )
                .strip()
                .split("Art.191/193 - I EFP")
            ):
                if "Luciano da Silva Martins" in nome:
                    list_urls.append(nome)
            list_urls.append(url_download)
        return list_urls


class Gui:
    def __init__(self):
        self.months = [
            "1:Janeiro",
            "2:Fevereiro",
            "3:Março",
            "4:Abril",
            "5:Maio",
            "6:Junho",
            "7:Julho",
            "8:Agosto",
            "9:Setembro",
            "10:Outubro",
            "11:Novembro",
            "12:Dezembro",
        ]
        self.years = [str(year) for year in range(2008, 2026)]

    def layout_inicial(self):
        sg.change_look_and_feel("Dark Blue 3")
        default_month = self.months[int(datetime.now().month - 1)]
        default_year = int(datetime.now().year)
        layout = [
            [sg.T("Escolha o mês")],
            [
                sg.Combo(
                    self.months,
                    size=(20, 12),
                    enable_events=False,
                    key="choicemonth",
                    default_value=default_month,
                )
            ],
            [
                sg.Combo(
                    self.years,
                    size=(20, 12),
                    enable_events=False,
                    key="choiceyear",
                    default_value=default_year,
                )
            ],
            [sg.Cancel(), sg.OK()],
        ]
        window = sg.Window("DO", grab_anywhere=False).Layout(layout)
        event, values = window.read()
        window.close()
        return values["choicemonth"], values["choiceyear"]

    def view(self, list_finals):
        layout = [
            [
                sg.Listbox(
                    values=list_finals,
                    size=(60, 15),
                    select_mode="LISTBOX_SELECT_MODE_SINGLE",
                    key="_LISTBOX_",
                    font=("Arial", 18),
                )
            ],
            [sg.Input(key="-IN-")],
            [sg.B("Preview"), sg.Button("Sair")],
        ]
        window = sg.Window("D.O.", layout)
        while True:
            event, values = window.read()  # type: (str, dict)
            if event in (None, "Sair"):
                break
            elif "Preview" in event:
                window["-IN-"].update(values["_LISTBOX_"])
        window.close()


if __name__ == "__main__":
    url = "http://www.imprensaoficial.com.br/DO/BuscaDO2001Resultado_11_3.aspx"
    gui = Gui()
    month, year = gui.layout_inicial()
    do = DiarioOficial(month, url, year)
    list_finals = do.scrapy()
    gui.view(list_finals)

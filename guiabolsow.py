import csv
import os
import random
from datetime import datetime
from time import sleep
import grecaptchabypass

import PySimpleGUI as sg
from decouple import config
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait


class GuiaBolsoSelenium:
    def __init__(self):
        self.months = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        self.with_data_and_buys = ""
        self.excludes = [
            "Impostos",
            "Saque",
            "Pagto conta telefone",
            "Pagamento de Boleto",
            "Taxas bancárias",
            "consignado",
            "Transf.Eletr.Disponiv",
            "Banco do Brasil S/A",
            "IOF",
            "Internet",
            "Outros gastos",
            "Tarifa Pacote",
            "Pgto BB",
            "Contr BB",
            "ANUIDADE NACIONAL",
        ]

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Essa função basicamente simulará a digitação de uma pessoa"""
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            sleep(random.randint(1, 5) / 30)

    def write_in_txt(self):
        # Write out the TXT file.
        filename = "C://Users//luxu//Desktop//guiabolso.txt"
        with open(filename, "w") as txtFileObj:
            for dado in self.with_data_and_buys:
                result = dado.text.split("\n")
                rows = ""
                search = False
                for row in result:
                    if search:
                        search = False
                    else:
                        try:
                            self.mes.index(row)
                            rows += f"{row}\n"
                            txtFileObj.write(rows)
                            # csvWriter.writerow(rows)
                            print(rows)
                            rows = ""
                        except:
                            if "R$" in row:
                                rows += f"{row}\n"
                                txtFileObj.write(rows)
                                # csvWriter.writerow(rows)
                                print(rows)
                                rows = ""
                                passar_um_traco = f"{'*' * 80}\n"
                                txtFileObj.write(passar_um_traco)
                                # csvWriter.writerow('*' * 80)
                                print(passar_um_traco)
                            else:
                                # row + '/'
                                rows += f"{row}/"
            # sleep(3)
        # txtFileObj.close()

    def write_in_csv(self):
        # Write out the CSV file.
        csvFileObj = open("guiabolso.csv", "w", newline="")
        csvWriter = csv.writer(csvFileObj, delimiter=" ")
        for dado in self.with_data_and_buys:
            result = dado.text.split("\n")
            rows = ""
            search = False
            for row in result:
                for exclude in self.excludes:
                    if exclude in row:
                        search = True
                        break
                if search:
                    search = False
                else:
                    try:
                        self.mes.index(row)
                        rows += row
                        csvWriter.writerow(rows)
                        print(rows)
                        rows = ""
                    except:
                        if "R$" in row:
                            rows += row
                            csvWriter.writerow(rows)
                            print(rows)
                            rows = ""
                            csvWriter.writerow("*" * 80)
                            print("*" * 100)
                        else:
                            rows += row + "/"
            sleep(3)
        csvFileObj.close()

    def show_only_em_picture(self):
        passar_um_traco = f"{'*' * 40}\n"
        for dado in self.with_data_and_buys:
            result = dado.text.split("\n")
            if "#tags" in result:
                print(result)
            rows = ""
            search = False
            for row in result:
                if search:
                    search = False
                else:
                    try:
                        self.mes.index(row)
                        rows += f"{row}\n"
                        print(f"{passar_um_traco}{rows}{passar_um_traco}")
                        rows = ""
                    except:
                        if "R$" in row:
                            rows += f"{row}\n"
                            print(rows)
                            rows = ""
                            print(passar_um_traco)
                        else:
                            rows += f"{row}/"

    def main(self, url, params):
        if os.name != "posix":  # Windows
            driver = webdriver.Chrome()
            # chrome_options.add_argument('--headless')
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Firefox()
        driver.set_window_size(1120, 800)
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ],
        )
        driver.get(url)
        xpath_input_email = '//input[@name="email"]'
        input_email = wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_input_email))
        )
        sleep(random.randint(1, 17) / 30)
        input_email.clear()
        input_email.send_keys(params["eMail"])
        sleep(random.randint(5, 7) / 30)
        xpath_input_password = '//input[@name="password"]'
        input_password = wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_input_password))
        )
        sleep(random.randint(5, 7) / 30)
        input_password.clear()
        input_password.send_keys(params["senha"])
        sleep(random.randint(15, 18) / 30)
        xpath_button_login = "//button//span[text()='Entrar']"
        button_login = wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_button_login))
        )
        sleep(random.randint(15, 17) / 30)
        button_login.click()
        sleep(random.randint(1, 17) / 30)
        # browser = grecaptchabypass.getBrowserFirefox(headless=False)
        bypass = grecaptchabypass.Bypass(webdriver=driver)
        bypass()
        sleep(random.randint(1, 17) / 30)
        return

        xpath_options_choice_months = '//div[@class="center"]'
        try:
            options_choice_months = driver.find_element_by_xpath(
                xpath_options_choice_months
            )
            options_choice_months.click()
            sleep(random.randint(2, 3))
            current_month = params["current_month"].lower()
            xpath_choice_month_to_show = (
                f'//ul[@class="jss313 jss314"]//*[text()="{current_month}"]'
            )
            f"//div[@class='jss256 jss523 jss266 jss257 jss524']//h1[text()='{current_month}']"
            choice_month_to_show = driver.find_element_by_xpath(
                xpath_choice_month_to_show
            )
            choice_month_to_show.click()
            driver.get(
                "https://www.guiabolso.com.br/web/#/financas/gastos-e-rendas/gastos"
            )
            xpath_with_data_and_buys = "//div[@id='extrato-desktop']"
            # xpath_with_data_and_buys = '//div[@class="sc-bnXvFD ibVkfa"]'
            # xpath_with_data_and_buys_second = '//section[@class="sc-bnXvFD lhIiZa"]'
            sleep(random.randint(2, 3))
            # id = 'extrato-desktop'
            result = driver.find_elements_by_xpath(xpath_with_data_and_buys)
            # result_second = driver.find_elements_by_xpath(xpath_with_data_and_buys_second)
            if len(result) > 0:
                # self.write_in_csv()
                self.with_data_and_buys = result
                # self.write_in_txt()
                self.show_only_em_picture()
            # elif len(result_second) > 0:
            # self.write_in_csv()
            # self.with_data_and_buys = result_second
            # self.write_in_txt()
            else:
                print("Sem dados captados :-(")
        except Exception as err:
            print(f"ERROR..: {err}")
            ...
            # driver.quit()
            # url = 'https://www.guiabolso.com.br/web/#/login'
            # params = {}
            # params['eMail'] = env.ENVIRON['GUIABOLSO_EMAIL']
            # params['senha'] = env.ENVIRON['GUIABOLSO_PASSWORD']
            # gb = GuiaBolsoSelenium()
            # gb.main(url, params)
        driver.quit()

    def layout_inicial(self):
        default_value = self.months[int(datetime.now().month - 1)]
        layout = [
            [sg.T("Escolha o mês")],
            [
                sg.Combo(
                    self.months,
                    size=(20, 12),
                    enable_events=False,
                    key="choicemonth",
                    default_value=default_value,
                )
            ],
            [sg.Cancel(), sg.OK()],
        ]
        window = sg.Window("Guia Bolso", grab_anywhere=False).Layout(layout)
        event, values = window.read()
        window.close()
        return values["choicemonth"]


class QuebraRecaptcha:

    def teste(self):
        # Iniciando browser, se headless for True o browser rodará em background.
        browser = grecaptchabypass.getBrowserFirefox(headless=False)

        # Para desabilitar o Logger: {grecaptcha.Logger.SHOW = False}

        # Instanciando classe Bypass.
        bypass = grecaptchabypass.Bypass(webdriver=browser)

        # Entrando na página onde o recaptcha está sendo exibido.
        browser.get("http://patrickhlauke.github.io/recaptcha/")

        # Quebrando o reCaptcha simplesmente invocando bypass().
        bypass()  # Retorna reCaptcha response: '03AGdBq26D_yqkZygev0CfRyFt2-U2PSN-8OaRfWGJ8U...'


if __name__ == "__main__":
    url = "https://www.guiabolso.com.br/web/#/login"
    # qr = QuebraRecaptcha()
    # qr.teste()
    gb = GuiaBolsoSelenium()
    params = {}
    params["eMail"] = config("GUIABOLSO_EMAIL")
    params["senha"] = config("GUIABOLSO_PASSWORD")
    params["current_month"] = gb.layout_inicial()
    if params["current_month"] != None:
        gb.main(url, params)
        print('Muito bem vamos lá!')
    else:
        print("Sem mês escolhido num dá!")

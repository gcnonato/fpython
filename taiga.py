from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from time import sleep
import os, random, re, json, sys, csv, environ
from datetime import datetime

ROOT_DIR = environ.Path(__file__)
env = environ.Env()
env.read_env()

class TaigaSelenium:
    def __init__(self):
        ...
        # if (os.name != 'posix'):  # Windows
        #     self.driver = webdriver.Chrome()
        #     chrome_options = webdriver.ChromeOptions()
        #     # chrome_options.add_argument('--headless')
        #     self.driver = webdriver.Chrome(options=chrome_options)
        # else:
        #     self.driver = webdriver.Firefox()
        #     self.driver.set_window_size(1120, 550)
        # chrome_options.add_argument('--headless')
        # self.driver.set_window_size(1120, 550)
        # self.wait = WebDriverWait(
        #     self.driver,
        #     10,
        #     poll_frequency=1,
        #     ignored_exceptions=[
        #         NoSuchElementException,
        #         ElementNotVisibleException,
        #         ElementNotSelectableException,
        #     ],
        # )

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Essa função basicamente simulará a digitação de uma pessoa"""
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            sleep(random.randint(1, 5) / 30)


    def main(self, url, params):
        if (os.name != 'posix'):  # Windows
            driver = webdriver.Chrome()
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Firefox()
            driver.set_window_size(1120, 550)
        # driver = self.driver
        print(f'URL.: {url}')
        driver.get(url)
        sleep(random.randint(5, 7) / 30)

        # xpath_input_username = '//input[@name="username"]'
        # input_username = self.wait.until(
        #     CondicaoExperada.element_to_be_clickable(
        #         (By.XPATH, xpath_input_username)
        #     )
        # )
        # sleep(random.randint(5, 7) / 30)
        # input_username.clear()
        # input_username.send_keys(params['username'])
        # sleep(random.randint(5, 7) / 30)
        # xpath_input_password = '//input[@name="password"]'
        # input_password = self.wait.until(
        #     CondicaoExperada.element_to_be_clickable(
        #         (By.XPATH, xpath_input_password)
        #     )
        # )
        # sleep(random.randint(5, 7) / 30)
        # input_password.clear()
        # input_password.send_keys(params['password'])
        # sleep(random.randint(15, 18) / 30)
        # xpath_button_login = "//button//span[text()='Login']"
        # button_login = self.wait.until(
        #     CondicaoExperada.element_to_be_clickable(
        #         (By.XPATH, xpath_button_login)
        #     )
        # )
        # sleep(random.randint(15, 17) / 30)
        # button_login.click()
        # sleep(random.randint(5, 6))
        #
        # xpath_options_choice_months = '//div[@class="center"]'
        # try:
        #     options_choice_months = driver.find_element_by_xpath(xpath_options_choice_months)
        #     options_choice_months.click()
        # except:
        #     driver.quit()
        #     url = 'https://www.guiabolso.com.br/web/#/login'
        #     params = {}
        #     params['username'] = env.ENVIRON['TAIGA_USERNAME']
        #     params['password'] = env.ENVIRON['TAIGA_PASSWORD']
        #     gb = TaigaSelenium()
        #     gb.main(url, params)
        # sleep(random.randint(2, 3))
        # xpath_choice_month_to_show = '//ul[@class="jss313 jss314"]//*[text()="janeiro"]'
        # choice_month_to_show = driver.find_element_by_xpath(xpath_choice_month_to_show)
        # choice_month_to_show.click()
        # driver.get('https://www.guiabolso.com.br/web/#/financas/gastos-e-rendas/gastos')
        # # xpath_with_data_and_buys = '//div[@class="sc-cpmLhU cllocz"]'
        # xpath_with_data_and_buys = '//div[@class="sc-bnXvFD ibVkfa"]'
        # sleep(random.randint(2, 3))
        # self.with_data_and_buys = driver.find_elements_by_xpath(xpath_with_data_and_buys)
        # if len(self.with_data_and_buys) > 0:
        #     # self.write_in_csv()
        #     self.write_in_txt()
        # else:
        #     print('Sem dados captados :-(')
        driver.quit()

    def write_in_txt(self):
        # Write out the TXT file.
        filename = "C://Users//luxu//Desktop//guiabolso.txt"
        with open(filename, 'w') as txtFileObj:
            for dado in self.with_data_and_buys:
                result = dado.text.split('\n')
                rows = ''
                search = False
                for row in result:
                    # for exclude in self.excludes:
                    #     if exclude in row:
                    #         search = True
                    #         break
                    if search:
                        search = False
                    else:
                        try:
                            self.mes.index(row)
                            rows += f"{row}\n"
                            txtFileObj.write(rows)
                            # csvWriter.writerow(rows)
                            print(rows)
                            rows = ''
                        except:
                            if 'R$' in row:
                                rows += f"{row}\n"
                                txtFileObj.write(rows)
                                # csvWriter.writerow(rows)
                                print(rows)
                                rows = ''
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
        csvFileObj = open("guiabolso.csv", 'w', newline='')
        csvWriter = csv.writer(csvFileObj, delimiter=' ')
        for dado in self.with_data_and_buys:
            result = dado.text.split('\n')
            rows = ''
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
                        rows = ''
                    except:
                        if 'R$' in row:
                            rows += row
                            csvWriter.writerow(rows)
                            print(rows)
                            rows = ''
                            csvWriter.writerow('*' * 80)
                            print('*' * 100)
                        else:
                            rows += row + '/'
            sleep(3)
        csvFileObj.close()


if __name__ == '__main__':
    # url = "https://projetos.clint.com.br/api/v1/auth"
    url = "https://projetos.clint.com.br/discover"
    params = {}
    params['username'] = env.ENVIRON['TAIGA_USERNAME']
    params['password'] = env.ENVIRON['TAIGA_PASSWORD']
    gb = TaigaSelenium()
    gb.main(url, params)

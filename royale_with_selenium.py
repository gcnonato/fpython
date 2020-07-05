import os
import random
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait


class RoyaleWithSelenium:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        # webdriver.Chrome(chrome_options=options)
        # chrome_options.add_argument(
        #     'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"'
        # )
        # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(
            self.driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ],
        )

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Essa função basicamente simulará a digitação de uma pessoa"""
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            sleep(random.randint(1, 5) / 30)

    def main(self, url):
        driver = self.driver
        driver.get(url)
        xpath_field_input_tag = '//*[@id="zorium-root"]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div[1]/div/div[1]/input'
        sleep(random.randint(5, 7) / 30)
        try:
            field_input_tag = self.wait.until(
                CondicaoExperada.element_to_be_clickable(
                    (By.XPATH, xpath_field_input_tag)
                )
            )
            sleep(random.randint(5, 7) / 30)
            field_input_tag.clear()
            field_input_tag.send_keys('P9V0VC9R')
            sleep(random.randint(5, 7) / 30)
            driver.find_element_by_xpath(
                '//*[@id="zorium-root"]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div[2]/div/div/button'
            ).click()
            sleep(random.randint(20, 22) / 30)
            xpath_list_chests = "//div[@class='chest']"
            try:
                result_cheats = self.wait.until(
                    CondicaoExperada.element_to_be_clickable(
                        (By.XPATH, xpath_list_chests)
                    )
                )
                data_and_time = datetime.now().strftime('%d-%m-%Y %Hh%M')
                final = '-'.join(data_and_time.split(' '))
                filename = f"Cheats-{final}.png"
                print(data_and_time)
                driver.save_screenshot(filename)
                driver.quit()
                return True
            except ElementNotVisibleException as err:
                print(f'Error (2).: {err}')
                driver.quit()
                return False
        except TimeoutException as err:
            print(f'Error(1).: {err}')
            driver.quit()
            return False

if __name__ == '__main__':
    # url = 'https://statsroyale.com/pt/'
    url = 'https://fam.gg/'
    # P9V0VC9R
    royale = RoyaleWithSelenium()
    result = royale.main(url)
    while not result:
        if result:
            print('Tudo certo :-)')
        else:
            print('Deu ruim ¬¬')
            royale = RoyaleWithSelenium()
            result = royale.main(url)

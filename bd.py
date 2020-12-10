# -*- coding: utf-8 -*-
import os
import random
from time import sleep

from decouple import config
from selenium import webdriver
from selenium.common.exceptions import (

    NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait


class BadooWithSelenium:
    def __init__(self):
        if os.name != "posix":  # Windows
            self.driver = webdriver.Chrome()
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
        else:
            CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"
            WINDOW_SIZE = "1920,1080"
            chrome_options = Options()
            # chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
            chrome_options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(
                executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options
            )
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

    def main(self, url, params):
        driver = self.driver
        driver.get(url)
        xpath_input_email = '//input[@name="email"]'
        input_email = self.wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_input_email))
        )
        sleep(random.randint(5, 7) / 30)
        input_email.clear()
        input_email.send_keys(params["email"])
        sleep(random.randint(5, 7) / 30)
        xpath_input_password = '//input[@name="password"]'
        input_password = self.wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_input_password))
        )
        sleep(random.randint(5, 7) / 30)
        input_password.clear()
        input_password.send_keys(params["password"])
        sleep(random.randint(15, 18) / 30)
        xpath_button_login = "//button[@name='post']"
        button_login = self.wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_button_login))
        )
        sleep(random.randint(15, 17) / 30)
        button_login.click()
        sleep(15)
        driver.get("https://badoo.com/search?filter=online")
        """ Daqui pra frente dá erro, pois quero manter a página aberta. """
        button_login = self.wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_button_login))
        )


if __name__ == "__main__":
    url = "https://us1.badoo.com/pt/signin/?f=top"
    params = {}
    params["email"] = config("BADOO_EMAIL")
    params["password"] = config("BADOO_PASSWORD")
    bd = BadooWithSelenium()
    bd.main(url, params)

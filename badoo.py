from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from time import sleep
import os, random, re, json, sys
from datetime import datetime


class BadooWithSelenium:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(1120, 550)
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
            CondicaoExperada.element_to_be_clickable(
                (By.XPATH, xpath_input_email)
            )
        )
        sleep(random.randint(5, 7) / 30)
        input_email.clear()
        input_email.send_keys(params['email'])
        sleep(random.randint(5, 7) / 30)
        xpath_input_password = '//input[@name="password"]'
        input_password = self.wait.until(
            CondicaoExperada.element_to_be_clickable(
                (By.XPATH, xpath_input_password)
            )
        )
        sleep(random.randint(5, 7) / 30)
        input_password.clear()
        input_password.send_keys(params['password'])
        sleep(random.randint(15, 18) / 30)
        xpath_button_login = "//button[@name='post']"
        button_login = self.wait.until(
            CondicaoExperada.element_to_be_clickable(
                (By.XPATH, xpath_button_login)
            )
        )
        sleep(random.randint(15, 17) / 30)
        button_login.click()
        sleep(random.randint(5, 7) / 30)
        xpath_pessoas_perto = "//a[@href='/search']"
        pessoas_perto = self.wait.until(
            CondicaoExperada.element_to_be_clickable(
                (By.XPATH, xpath_pessoas_perto)
            )
        )
        pessoas_perto.click()
        online = "(.//*[normalize-space(text()) and normalize-space(.)='Pessoas Perto'])[2]/following::div[7]"
        WebDriverWait(driver, 10).until(esperar_pelo_elemento(driver,online))
        driver.find_element_by_link_text("Pessoas Perto").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Pessoas Perto'])[2]/following::div[7]"
        ).click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Pessoas Perto'])[2]/following::div[7]"
        ).click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Novos membros'])[2]/following::div[1]"
        ).click()

if __name__ == '__main__':
    url = 'https://us1.badoo.com/pt/signin/?f=top'
    params = {}
    # params['email'] = input('Digite o e-mail:')
    # params['password'] = input('Digite a senha:')
    params['email'] = ''
    params['password'] = ''
    bd = BadooWithSelenium()
    bd.main(url, params)
    # if len(params['email']) < 1:
    #     print('Digite e-mail/senha para acessar o site!!')
    #     sys.exit(0)
    # else:
    #     print(params)
    #     bd.main(url, params)

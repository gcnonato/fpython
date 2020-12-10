# -*- coding: utf-8 -*-
import os
import random
from time import sleep
import environ

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait

environ.Path(__file__)
env = environ.Env()
env.read_env(".envs/.env")

URL = "https://www.instagram.com/"
URL_TAG = "https://www.instagram.com/explore/tags/"
BTN_TO_LOGIN = "//a[@href='/accounts/login/?source=auth_switcher']"
INPUT_USERNAME = "//input[@name='username']"
INPUT_PASSWORD = "//input[@name='password']"
SCRIPT_TO_SCROLL_PAGE = "window.scrollTo(0, document.body.scrollHeight);"
BTN_CURTIDA = "//button[@class='dCJp8 afkep']"
# '//button[@class="dCJp8 afkep"]'


class InstagramBot:
    def __init__(self, username, password, hashtag):
        if os.name != "posix":  # Windows
            self.driver = webdriver.Chrome()
            webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
        else:
            self.driver = webdriver.Firefox()
            # self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_window_size(1120, 550)
        self.username = username
        self.password = password
        self.hashtag = hashtag
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

    def login(self):
        driver = self.driver
        driver.get(URL)
        sleep(random.randint(3, 6))
        login_button = driver.find_element_by_xpath(BTN_TO_LOGIN)
        login_button.click()
        sleep(random.randint(4, 6))
        user_element = self.wait.until(
            CondicaoExperada.element_to_be_clickable((By.XPATH, INPUT_USERNAME))
        )
        # user_element = driver.find_element_by_xpath(INPUT_USERNAME)
        user_element.clear()
        self.type_like_a_person(self.username, user_element)
        # sleep(random.randint(4, 6))
        password_element = driver.find_element_by_xpath(INPUT_PASSWORD)
        password_element.clear()
        self.type_like_a_person(self.password, password_element)
        sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        sleep(random.randint(4, 6))
        self.curtir_fotos_com_a_hastag(self.hashtag)

    def curtir_fotos_com_a_hastag(self, hashtag):
        driver = self.driver
        driver.get(f"{URL_TAG}{hashtag}")
        sleep(5)
        for i in range(1, 3):
            driver.execute_script(SCRIPT_TO_SCROLL_PAGE)
            sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        # teste = f"{hashtag} fotos: {str(len(pic_hrefs))}"
        # testes = [
        #     href
        #     for href in pic_hrefs
        #     if hashtag in href and href.index("https://www.instagram.com/p") != -1
        # ]

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError:
                print("pulando link inválido")
                continue
            driver.get(pic_href)
            driver.execute_script(SCRIPT_TO_SCROLL_PAGE)
            try:
                driver.find_element_by_xpath(BTN_CURTIDA).click()
                print("Foto curtida com sucesso!! :-)")
                sleep(random.randint(19, 23))
            except Exception as e:
                print(e)
                sleep(5)


username = env.ENVIRON["INSTA_USERNAME"]
password = env.ENVIRON["INSTA_PASSWORD"]
hashtag = "informática"
insta = InstagramBot(username, password, hashtag)
insta.login()

# -*- coding: utf-8 -*-
import os
import random
from time import sleep

from decouple import config
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException, ElementNotVisibleException,
    ElementNotSelectableException, TimeoutException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait


def type_like_a_person(sentence, single_input_field):
    """ Essa função basicamente simulará a digitação de uma pessoa"""
    print("going to start typing message into message share text area")
    for letter in sentence:
        single_input_field.send_keys(letter)
        sleep(random.randint(1, 5) / 30)


if os.name != "posix":  # Windows
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=chrome_options)
else:
    browser = webdriver.Firefox()
browser.set_window_size(1120, 800)
wait = WebDriverWait(
    browser,
    10,
    poll_frequency=1,
    ignored_exceptions=[
        NoSuchElementException,
        ElementNotVisibleException,
        ElementNotSelectableException,
    ],
)

url = "https://www.fazenda.sp.gov.br/folha/nova_folha/acessar_dce.asp?menu=dem&user=rs"
browser.get(url)

login = browser.find_element_by_name("txt_logindce")
senha = browser.find_element_by_name("txt_senhadce")
linkElem = browser.find_element_by_name("enviar")
xpath_input_caixaAviso = '//*[@id="aviso"]/div/div[3]/center/input'
try:
    input_caixaAviso = wait.until(
        CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_input_caixaAviso))
    )
    input_caixaAviso.send_keys(Keys.ENTER)
except TimeoutException:
    ...
sleep(random.randint(5, 7) / 30)
type_like_a_person("11632112", login)
type_like_a_person(config("HOLERITE_SENHA"), senha)
sleep(random.randint(1, 5) / 30)
linkElem.send_keys(Keys.ENTER)
sleep(random.randint(15, 25) / 30)
# de PROPÓSITO PARA QUEBRAR PARA NÃO FECHAR
input_caixaAviso = wait.until(
    CondicaoExperada.element_to_be_clickable((By.XPATH, xpath_input_caixaAviso))
)
# browser.quit()

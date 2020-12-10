# -*- coding: utf-8 -*-
import random
from time import sleep

import PySimpleGUI as sg
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condicaoexperada
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.listamais.com.br/"
BTN_TO_SEARCH = "//button[@class='tg-btn']"
SCRIPT_TO_SCROLL_PAGE = "window.scrollTo(0, document.body.scrollHeight);"
BTN_CURTIDA = "//button[@class='dCJp8 afkep']"


class ListaTelefonica:
    def __init__(self):
        self.o_que_procurar = ""
        self.cidade = "Presidente Prud"
        self.escolha = 0
        self.wait = None

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que
            você simule a digitação como uma pessoa"""
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            sleep(random.randint(1, 5) / 30)

    def layout_inicial(self):
        layout = [[sg.Input(size=(80, 1))], [sg.Cancel(), sg.OK()]]

        window = sg.Window("Procurar no Lista Mais", layout)
        event, values = window.read()
        window.close()

        if values[0] is True:
            self.escolha = 0
        if event == "OK":
            self.o_que_procurar = values[0]
        else:
            self.o_que_procurar = ""
        lmais.search()

    def search(self):
        if len(self.o_que_procurar) < 1:
            return
        driver = webdriver.Chrome()
        self.wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ],
        )
        driver.get(URL)
        campo_busca = self.wait.until(
            condicaoexperada.element_to_be_clickable(
                (By.XPATH, '//span//input[@name="busca"]')
            )
        )
        self.type_like_a_person(self.o_que_procurar, campo_busca)

        campo_cidade = self.wait.until(
            condicaoexperada.element_to_be_clickable(
                (By.XPATH, "//span//input[@tabindex='3']")
            )
        )
        self.type_like_a_person(self.cidade, campo_cidade)
        sleep(random.randint(3, 6))
        btn_search = self.wait.until(
            condicaoexperada.element_to_be_clickable((By.XPATH, BTN_TO_SEARCH))
        )
        sleep(random.randint(3, 6))
        btn_search.click()

    # def box_search(self):
    #     sleep(random.randint(3, 6))
    #     xpath_qtdade_encontrada = "//div[@id='resultado-texto-pesquisa']//strong"
    #     qtdade_encontrada = self.driver.find_element_by_xpath(xpath_qtdade_encontrada).text
    #     xpath_nome_do_pesquisado = "//div[@id='resultado-texto-pesquisa']//h1"
    #     nome_do_pesquisado = self.driver.find_element_by_xpath(xpath_nome_do_pesquisado).text
    #     xpath_info = "//*[@class='informacoes-empresa hidden-xs']"
    #     infos = ''
    #     try:
    #         infos = self.driver.find_element_by_xpath(xpath_info).text
    #     except:
    #         pass
    #     xpath_distance = "//span[@class='distancia-empresa']//span"
    #     distance = self.driver.find_element_by_xpath(xpath_distance).text
    #     xpath_open_now = "//*[@class='aberto-agora']"
    #     open_now = ''
    #     try:
    #         open_now = self.driver.find_element_by_xpath(xpath_open_now).text
    #     except:
    #         pass
    #     class_company = 'endereco-empresa'
    #     xpath_address = f"//*[@class='{class_company}']//div//div//div//a"
    #     try:
    #         address = self.driver.find_element_by_xpath(xpath_address).text
    #     except:
    #         class_company = 'endereco-empresa-gratuito'
    #         xpath_address = f"//div[@class='{class_company}']//div//div//div//a"
    #         address = self.driver.find_element_by_xpath(xpath_address).text
    #     for i in range(1, 3):
    #         xpath_address = f"//*[@class='{class_company}']//div//div//div//span[{i}]"
    #         address += self.driver.find_element_by_xpath(xpath_address).text
    #     xpath_hour = "//*[@class='horario-atual']//div"
    #     hour_open = ''
    #     try:
    #         hour_open = self.driver.find_element_by_xpath(xpath_hour).text
    #     except:
    #         pass
    #     self.driver.find_element_by_xpath('//a[@title="Ver telefone."]').click()
    #     sleep(random.randint(1, 3))
    #     list_telephones = []
    #     size_div_telephones = len(self.driver.find_elements_by_xpath("//*[@class='show-grid']//div"))
    #     if size_div_telephones == 1:
    #         xpath_phone = f"//*[@class='show-grid']//div[1]"
    #         list_telephones.append(
    #             self.driver.find_element_by_xpath(xpath_phone).text
    #         )
    #         print(qtdade_encontrada)
    #         print(nome_do_pesquisado)
    #         print(infos)
    #         print(distance)
    #         print(address)
    #         print(hour_open)
    #         print(open_now)
    #         print(list_telephones)
    #     elif size_div_telephones > 1:
    #         for i in range(1, size_div_telephones):
    #             xpath_phone = f"//*[@class='show-grid']//div[{i}]"
    #             list_telephones.append(
    #                 self.driver.find_element_by_xpath(xpath_phone).text
    #             )
    #         print(qtdade_encontrada)
    #         print(nome_do_pesquisado)
    #         print(infos)
    #         print(distance)
    #         print(address)
    #         print(hour_open)
    #         print(open_now)
    #         print(list_telephones)
    #     else:
    #         print(f'SEM TELEFONE PARA A BUSCA.: {nome_do_pesquisado}')
    #     sleep(random.randint(20, 30))
    #     self.driver.quit()


if __name__ == "__main__":
    lmais = ListaTelefonica()
    lmais.layout_inicial()

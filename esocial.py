
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

browser = webdriver.Firefox(executable_path='geckodriver')
# browser = webdriver.Firefox(executable_path='C:\\Users\\aline.almeida\\PycharmProjects\\geckodriver.exe')

#Busca a pag. que será manipulada
browser.get('http://consultacadastral.inss.gov.br/Esocial/pages/index.xhtml')

# Clica no botão "Consulta On-line"
campo_busca = browser.find_element_by_xpath('//*[@id="indexForm1:botaoConsultar"]').click()

text = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:nome"]')
text.send_keys('Luciano')
# text.send_keys(input("Nome Completo"))

def type_like_a_person(sentence, single_input_field):
    """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
    print("going to start typing message into message share text area")
    for letter in sentence:
        single_input_field.send_keys(letter)
        sleep(random.randint(1, 5) / 30)

# sleep(3)
# date = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:dataNascimento"]')
data = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:dataNascimento"]')
# date.send_keys(input("Data_Nasc"))
nasc = "18061974"
type_like_a_person(nasc, data)
# date.send_keys(nro)

# num = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:cpf"]')
num = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:cpf"]')
# num.send_keys(input("CPF"))
num.send_keys("20443596859")

# num = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:nis"]')
num = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:nis"]')
# num.send_keys(input("NIS"))
num.send_keys("1809213")
import random
from time import sleep

from selenium import webdriver

browser = webdriver.Firefox(executable_path="geckodriver")
browser.get("http://consultacadastral.inss.gov.br/Esocial/pages/index.xhtml")
campo_busca = browser.find_element_by_xpath(
    '//*[@id="indexForm1:botaoConsultar"]'
).click()
text = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:nome"]')
text.send_keys("Luciano")


def type_like_a_person(sentence, single_input_field):
    """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
    print("going to start typing message into message share text area")
    for letter in sentence:
        single_input_field.send_keys(letter)
        sleep(random.randint(1, 5) / 30)


data = browser.find_element_by_xpath(
    '//*[@id="formQualificacaoCadastral:dataNascimento"]'
)
nasc = "18061974"
type_like_a_person(nasc, data)
num = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:cpf"]')
num.send_keys("20443596859")
num = browser.find_element_by_xpath('//*[@id="formQualificacaoCadastral:nis"]')
num.send_keys("1809213")

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import environ

ROOT_DIR = environ.Path(__file__)
env = environ.Env()
env.read_env()

browser = webdriver.Chrome()
browser.get('https://www.fazenda.sp.gov.br/folha/nova_folha/acessar_dce.asp?menu=dem&user=rs')

login = browser.find_element_by_name('txt_logindce')
senha = browser.find_element_by_name('txt_senhadce')
linkElem = browser.find_element_by_name('enviar')
try:
	caixaAviso = browser.find_element_by_xpath('//*[@id="aviso"]/div/div[3]/center/input')
	caixaAviso.send_keys(Keys.ENTER)
except Exception as e:
	pass
else:
	pass
finally:
	pass
login.send_keys('11632112')
senha.send_keys(env.ENVIRON['HOLERITE_SENHA'])
linkElem.send_keys(Keys.ENTER)

sleep(1)

caixaAviso = browser.find_element_by_xpath('//*[@id="aviso"]/div/div[3]/center/input')
caixaAviso.send_keys(Keys.ENTER)

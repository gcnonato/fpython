# -*- coding: utf-8 -*-
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

login = "seuemail@email.com"
password = "suasenha"


def initiateSelenium():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome()
        return driver
    except Exception as e:
        print("Error on initiateSelenium(): %s" % str(e))
        raise


def go():
    try:
        driver = initiateSelenium()
        url = "https://site.verocard.com.br/apex/f?p=105:105"
        driver.get(url)
        nro_cartao = "6064450790280350"
        idinput1 = '//*[@id="P105_CARTAO"]'
        nro = driver.find_element_by_xpath(idinput1)
        nro.send_keys(nro_cartao)
        form = driver.find_element_by_class_name("form-holder")
        btn = form.find_element_by_xpath(".//button[@class='button fill full small']")
        btn.click()
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "amount-input"))
        )
        # Roda indefinidamente
        while True:
            inputs = driver.find_elements_by_class_name("amount-input")
            print(
                "Price at: %s is %s"
                % (
                    datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    inputs[1].text,
                )
            )
            print("Saving to DB (chamar funcao de save no banco)")
            time.sleep(1)
    except Exception as e:
        print("Error on go(): %s" % str(e))


go()

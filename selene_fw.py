from selene import Browser, Config
from selenium import webdriver

browser = Browser(Config(
    driver=webdriver.Chrome(),
    base_url='https://google.com',
    timeout=2))


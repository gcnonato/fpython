from time import sleep
from selenium import webdriver

# Use with Chromium:
#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType

# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

# Use with FireFox:
#
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
#
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
sleep(2)
driver.close()

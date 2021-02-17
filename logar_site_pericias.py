from time import sleep

from selenium import webdriver

url = 'http://periciasmedicas.gestaopublica.sp.gov.br/eSisla/noauth/login/prepare.do'

options = webdriver.ChromeOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--allow-running-localhost')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# A partir dessa etapa, ele virá fazer tudo automaticamente dentro do browser
# Abre o browser do Google Chrome automaticamente
browser = webdriver.Chrome(options = options)

# Obtém os dados através da variavel URL
browser.get(url)

# sleep(5)
xpath_consulta_servidor = '//*[@id="imgcon"]'
browser.find_element_by_xpath(xpath_consulta_servidor).click()

sleep(5)
browser.find_element_by_css_selector('selecaoConsulta').click()
# browser.find_element_by_tag_name('selecaoConsulta').click()

xpath_option_cpf = '//*[@id="consulta"]/form/fieldset/div[1]/label/select/option[3]'

browser.find_element_by_xpath(xpath_option_cpf).click()

browser.find_element_by_tag_name('num').send_keys('204435968')

browser.find_element_by_tag_name('dig').send_keys('59')

browser.find_element_by_tag_name('dtNasc').send_keys('18')

browser.find_element_by_tag_name('dtNasc').send_keys('06')

browser.find_element_by_tag_name('dtNasc').send_keys('1974')

browser.find_element_by_class_name('submeter').click()



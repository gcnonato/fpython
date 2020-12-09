# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup as bs

url = 'http://luxu.com.br/code.html'
page = get(url)
soup = bs(page.content, 'html.parser')
texto = soup.find_all('span')[7].text
print(texto)

#coding: utf-8
from requests import get
from bs4 import BeautifulSoup as bs

url = 'https://www.mentebinaria.com.br/'
p = get(url)
soup = bs(p.content, 'html.parser')
with open('mentein.txt', 'w') as f:
    for pag in soup.find_all('li', class_='ipsDataItem ipsClearfix'):
        f.write(pag.div.time.getText())

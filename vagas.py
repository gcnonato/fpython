# encoding: utf-8

import urllib.request

from bs4 import BeautifulSoup as bs

url = "http://jenisandrade.blogspot.com/2018/10/convocacao-dos-aevps-nomeados-em-10-08.html"
site = urllib.request.urlopen(url)
soup = bs(site, "html.parser")

nv = []
lista = soup.select(".comments")

for p in lista:
    print(p)
    nv.append(p)

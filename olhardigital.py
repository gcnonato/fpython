# encoding: utf-8

import urllib.request

from bs4 import BeautifulSoup as bs


# url = 'https://olhardigital.com.br/'
url = "https://www.buzzfeed.com/trending?utm_term=.aiYqq0KzPG#.imA44kywqY"
site = urllib.request.urlopen(url)
soup = bs(site, "html.parser")
nv = []
lista = soup.select(".link-gray")
for p in lista:
    nv.append(p)
for p in nv:
    print(p.find("a"))
    print(100 * "*")

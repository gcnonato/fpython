import json

from bs4 import BeautifulSoup as bs
from requests import get

headers = {
    'authority': 'www.zapimoveis.com.br',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '__cfduid=d192a417ff850885b70f7277b4d7f97fb1590280881; __cfruid=fa734f5267d3e57ba3713e5d9b09b6019195b691-1590280881',
}

url = 'https://www.zapimoveis.com.br/venda/apartamentos/'
response = get(url, headers=headers)
soup = bs(response.content, 'lxml')
# soup.find_all('script')[1].contents
print(soup)

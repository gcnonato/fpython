from requests import get
from bs4 import BeautifulSoup as bs
import re

url = "http://www.iamspe.sp.gov.br/rede/dhtml.php?p1=f3&p2=0&p3=9532&p4=0&p5=0"

payload = {}
headers = {
  'Connection': 'keep-alive',
  'Accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'Referer': 'http://www.iamspe.sp.gov.br/rede/index.php',
  'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', str(raw_html))
  return cleantext


response = get(url, headers=headers, data=payload)
soup = bs(response.content, "lxml")
texto_final = cleanhtml(soup)
juntar = ''
for r in texto_final.split('\n\n'):
  if len(r) > 0:
    # print(f'{r}\n{"*"*70}')
      if 'MUNIC' in r:
        print(f'{"*" * 70}{r}')
      else:
        print(f'{r.strip()}')
    # if 'call' in r or 'location_on' in r:
    #   juntar += ' ' + r
    #   # juntar += juntar
    #   # print(juntar)
    # else:
    #   print(f'{"*"*70}\nSize..:{len(r)}{r}\n{"*"*70}')


# print()
# for t in response.content:#.encode('utf8')
#   print(t)
# df = pd.read_html(response.text.encode('utf8'))

# print()
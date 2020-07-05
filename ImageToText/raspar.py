import csv

from bs4 import BeautifulSoup as bs
from requests import get

pages = []

for i in range(1, 5):
  url = f'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ{str(i)}.htm'
  pages.append(url)
# pprint(pages)

for item in pages:
  page = get(item)
  soup = bs(page.text, 'html.parser')

  # Remover links inferiores
  last_links = soup.find(class_='AlphaNav')
  last_links.decompose()

  # Criar um arquivo para gravar, adicionar linha de cabeçalhos
  f = csv.writer(open('z-artist-names.csv', 'w'))
  f.writerow(['Name', 'Link'])

  # Pegar todo o texto da div BodyText
  artist_name_list = soup.find(class_='BodyText')

  # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
  artist_name_list_items = artist_name_list.find_all('a')

  # Criar loop para imprimir todos os nomes de artistas
  for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = f"https://web.archive.org{artist_name.get('href')}"

    # Adicionar em uma linha o nome de cada artista e o link associado
    f.writerow([names, links])
    # print(artist_name.prettify())

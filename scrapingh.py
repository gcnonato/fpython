import os

from requests import get
from scrapinghub import ScrapinghubClient as sh
import time


def rodar_spider(dict_spider):
  str_spyder = dict_spider.split('/')
  print(str_spyder)
  client = sh(apikey)
  project = client.get_project(int(str_spyder[1]))
  spider = project.spiders.get(str_spyder[0])
  job = spider.jobs.run()


def baixar():
  base_url = 'https://storage.scrapinghub.com/items/'
  resultado = get(
      f'{base_url}{project_id}/{spider_id[nro_spider]}?format=json&apikey={apikey}')
      # .json()
  # agora = 0
  for i in resultado:
    if 'time' in i.keys():
      agora = i['time']
      lastupdate = i['lastupdate']  # '1546170806'
    else:
      print(i)
      print('*' * 66)

  if agora > 0:
    print(agora)
    print(time.ctime(int(str(agora))))
    print(time.strftime("%D %H:%M", time.localtime(int(str(agora)))))
    print(lastupdate)
    print(time.strftime("%D %H:%M", time.localtime(int(str(lastupdate)))))
    print(time.ctime(int(str(lastupdate))))


if __name__ == '__main__':
  apikey = u'a103bede59104d20a3fcdd4573996355'
  dict_spider = {
    0: "empregos/263925/2",
    1: "climatempo/263925/7",
    2: "royale/263925/8",
    3: "jenis/263925/9",
    4: "sedepp/263925/10"
  }
  os.system('cls')
  print(u'-' * 70)
  for key, value in dict_spider.items():
    print(u'%s -> %s' % (key, value))
  print(u'{}\n{}'.format(
    '-' * 70,
    'Digite o spider desejado ou ENTER para royale'))
  escolha = input()
  if escolha:
    nro_spider = int(escolha)
  else:
    nro_spider = 2
  print(dict_spider[int(nro_spider)])
  rodar_spider(dict_spider[int(nro_spider)])

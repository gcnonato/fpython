import json

from requests import get
url = 'https://www.dracena.sp.gov.br/' \
      'indexAjax.php' \
      '?pag=T0RVPU9EUT1PRGM9T1RRPU9UZz1Oamc9T0RrPU9HVT1PV0k9T1dZPU9XRT1ZVEE9' \
      '&view=GET-DADOS-ABERTOS' \
      '&tipo=legislacao' \
      '&tipolei=4' \
      '&tipodownload=json' \
      '&ano=2009'
response = get(url)
for index, r in response.json().items():
    print(r)
    if isinstance(r, list):
        for t in r:
            print(t)
# 'tipo', 'numero', 'ano', 'data', 'ementa', 'autores', 'situacao', 'legislatura', 'tipo-projeto-origem', 'numero-projeto-origem'
# for texto in json.loads(response.content):
#     print(texto)
# print(json.loads(response.content))

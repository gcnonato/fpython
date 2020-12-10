from requests import get


url = "https://www.gazetadopovo.com.br/vozes/madeleine-lacsko/" \
      "preso-homem-que-abusou-sexualmente-de-dezenas-de-criancas-usando-perfis-falsos/"
html = get(url)
print(html.content)

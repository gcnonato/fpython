from requests import get

url = 'https://revistapegn.globo.com/Empreendedorismo/noticia/2020/09/google-dara-mentorias-gratuitas-para-voce-achar-emprego-ou-criar-negocio.html'
html = get(url)
print(html.text)

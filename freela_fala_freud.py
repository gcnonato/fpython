from parsel import Selector
from requests import get
import csv
import os


lista_ean = {
    "7891721201806",
    "7896026306188",
    "7896016808173",
    "7896016807916",
    "7897705202586",
    "7896382707742",
    "5000456028370",
    "7897705202548",
    "7896004752730",
}
cont = 0
homepath = os.path.expanduser(os.getenv("USERPROFILE"))
desktoppath = "Desktop"
file = "comparacao_preco.csv"
filename = os.path.join(homepath, desktoppath, file)

with open(filename, "w", newline="") as _f:
    for ean in lista_ean:
        url = f"https://www.cliquefarma.com.br/preco/7891721201806/?termo={ean}"
        text = get(url).text
        selector = Selector(text=text)

        prices = selector.css(".preco-oferta2::text")
        descriptions = selector.css(".descricao::text")
        for description, price in zip(descriptions, prices):
            if len(description.get()) > 1:
                print(f"{description.get().strip()} {price.get().strip()}")
                cont += 1
                arq = csv.writer(_f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
                arq.writerow([description.get().strip(), price.get().strip()])
                # arq.writerow(f'{description.get().strip()},{price.get().strip()}')
print(cont)

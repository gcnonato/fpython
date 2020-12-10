from sorveteria import Sorveteria
from scrapingh import Scraping


def test_cmd():
    sorveteria = Sorveteria()
    assert str(sorveteria) == "sim, é possível usar doctest"


def test_contador_vendas():
    sorveteria = Sorveteria()
    assert sorveteria.contador_vendas == 0


def test_pegar_nome_spider():
    name_spider = 'climatempo'
    sh = Scraping(name_spider)
    assert str(sh) == name_spider


def test_status_code():
    name_spider = 'climatempo'
    sh = Scraping(name_spider)
    sh.getScrappingPage()
    assert sh.getStatusCode() == 200


def test_pegar_ultimo_item_spider():
    name_spider = 'climatempo'
    sh = Scraping(name_spider)
    sh.getNumberSpider()
    assert sh.number_item == 34

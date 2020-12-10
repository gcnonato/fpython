# -*- coding: utf-8 -*-
import os
from requests import get
from scrapinghub import DuplicateJobError, ScrapinghubClient as sh


class Error(Exception):
    pass


class isSchedule(Error):
    """Raised when the job is scheduled"""
    pass


class Scraping:
    def __init__(self, name_spider):
        self.name_spider = name_spider
        self.apikey = "a103bede59104d20a3fcdd4573996355"
        self.number_item = 0
        self.number_project = 263925
        self.resultado = ''
        self.spiders = {
            "empregos": 2,
            "climatempo": 7,
            "royale": 8,
            "jenis": 9,
            "sedepp": 10
        }

    def __str__(self):
        return self.name_spider

    def generateNewSpiderItem(self):
        client = sh(self.apikey)
        try:
            project = client.get_project(self.number_project)
            spider = project.spiders.get(name_spider)
            job = spider.jobs.run()
            nr_item = str(job.key).split("/")[-1]
            print(f'spider.name: {spider.name} - job.key: {job.key} - number_job: {nr_item}')
            return nr_item
        except DuplicateJobError as err:
            print(f'WARNING: {err}')
            return 0

    def getNumberSpider(self):
        client = sh(self.apikey)
        project = client.get_project(self.number_project)
        spider = project.spiders.get(self.name_spider)
        self.number_item = int([s['key'] for s in spider.jobs.iter_last()][0].split('/')[-1])

    def getStatusCode(self):
        return self.resultado.status_code

    def getScrappingPage(self):
        base_url = "https://storage.scrapinghub.com/items"
        # https://storage.scrapinghub.com/items/263925/7/32/?format=json&apikey=a103bede59104d20a3fcdd4573996355
        number_spider = self.spiders['climatempo']
        url = f"{base_url}/{self.number_project}/{number_spider}/{self.number_item}?format=json&apikey={self.apikey}"
        self.resultado = get(url)

    def getListResultScrapping(self):
        for clima in self.resultado.json():
            data = clima['data']
            probabilidade = clima['probabilidade']
            sensacaoTermica = clima['sensacaoTermica']
            min = clima['temperaturaMinima']
            max = clima['temperaturaMaxima']
            desc = clima['texto']
            print(f'{data} - {probabilidade} - {sensacaoTermica} - {min} - {max} - {desc}\n{"*" * 120}')


if __name__ == "__main__":
    name_spider = 'climatempo'
    raspar = Scraping(name_spider)
    os.system("cls")
    # raspar.generateNewSpiderItem()
    raspar.getNumberSpider()
    print(raspar.number_item)
    raspar.getScrappingPage()
    raspar.getListResultScrapping()
    # raspar.baixar()
    # for nro_spider in range(5):
    #     generate_new_spider(spiders[int(nro_spider)])
    #     print('*'*70)

# encoding: utf-8
import scrapy


class MedidasProvisorias(scrapy.Spider):
    name = "mp"

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
        }
        yield scrapy.Request(
            "http://www.planalto.gov.br/CCIVIL_03/MPV/Principal.htm", headers=headers
        )

    def parse(self, response):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
        }
        mps_urls = response.xpath(
            "//a[contains(@href, 'Quadro') and not(contains(@href, 'AGU'))]/@href"
        ).getall()
        for url in mps_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse_mp_table)

    def parse_mp_table(self, reponse):
        print(reponse)

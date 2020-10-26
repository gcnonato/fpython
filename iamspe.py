import os
import re

from bs4 import BeautifulSoup as bs
from requests import get
from splitty import clear_list_strings


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
    cleantext = re.sub(cleanr, "", str(raw_html))
    return cleantext


class Iamspe:
    def __init__(self):
        self.writeResults = []
        self.cont = 0
        self.homepath = os.path.expanduser(os.getenv("USERPROFILE"))
        self.desktoppath = "Desktop"
        self.url = (
            "http://www.iamspe.sp.gov.br/rede/dhtml.php?p1=f3&p2=0&p3=9532&p4=0&p5=0"
        )
        self.headers = {
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://www.iamspe.sp.gov.br/rede/index.php",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        }

    def scrapy(self):
        response = get(self.url, headers=self.headers)
        soup = bs(response.content, "lxml")
        texto_final = cleanhtml(soup)
        for r in texto_final.split("\n\n"):
            self.cont += 1
            if len(r) > 0:
                if "MUNIC" in r:
                    tratado = f'{"*" * 70}{r}'
                    self.writeResults.append(tratado)
                else:
                    tratado = f"{r.strip()}"
                    self.writeResults.append(tratado)
        print(self.writeResults)

    def write_txt(self, filename):
        local_save = os.path.join(self.homepath, self.desktoppath, filename)
        with open(local_save, "w", encoding="utf8") as _file:
            for medico in self.writeResults:
                _file.write(medico)
                _file.write("\n")

    def load_txt(self, filename):
        arquivo = os.path.join(self.homepath, self.desktoppath, filename)
        with open(arquivo, encoding="utf8") as _file:
            texto = clear_list_strings(_file.readlines())
        for t in texto:
            print(f"{t}")


if __name__ == "__main__":
    file_name = "iamspe.txt"
    iamspe = Iamspe()
    # iamspe.scrapy()
    # iamspe.write_txt(file_name)
    iamspe.load_txt(file_name)

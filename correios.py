# -*- coding: utf-8 -*-
import sys

import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
from requests import post


class Correios:
    def __init__(self):
        self.nro_rastreamento = 0
        self.cookies = {
            "CFID": "102956239",
            "CFTOKEN": "6fc0f7ceebf578b7-1CB381EE-D0BA-1488-E9E36764A9BA1C1F",
            "JSESSIONID": "F71FBE475FD98D20E346A374999C5EDF.cfusion02",
            "ssvbr0331_www2sro": "sac2841SRO",
            "sitecorreioscookie-%3FEXTERNO%3Fpool_site_institucional_443": "BEBOKIMA",
            "ssvbr0331_www2": "sac2842",
            "_ga": "GA1.3.1493968158.1588327061",
            "_gid": "GA1.3.1615543768.1588327061",
            "_gat_gtag_UA_564464_1": "1",
            "CFGLOBALS": "urltoken%3DCFID%23%3D102956239%26CFTOKEN%23%3D6fc0f7ceebf578b7%2D1CB381EE%2DD0BA%2D1488%2DE9E36764A9BA1C1F%26jsessionid%23%3DF71FBE475FD98D20E346A374999C5EDF%2Ecfusion02%23lastvisit%3D%7Bts%20%272020%2D05%2D01%2007%3A10%3A24%27%7D%23hitcount%3D10%23timecreated%3D%7Bts%20%272020%2D05%2D01%2006%3A57%3A38%27%7D%23cftoken%3D6fc0f7ceebf578b7%2D1CB381EE%2DD0BA%2D1488%2DE9E36764A9BA1C1F%23cfid%3D102956239%23",
        }

        self.headers = {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://www2.correios.com.br",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www2.correios.com.br/sistemas/rastreamento/default.cfm",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        }

    def main(self):
        data = {
            "objetos": self.nro_rastreamento,
        }
        url = "https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm"
        response = post(url, cookies=self.cookies, headers=self.headers, data=data)
        soup = bs(response.content, "lxml")
        list_tables = soup.find_all("table")
        msg = ''
        if list_tables:
            for table in list_tables:
                final = " ".join(table.getText().split())
                msg = final
        else:
            msg = 'Lista vazia'
        return msg

    def telaInicial(self):
        layout = [
            [sg.Text("Nro_Rastreamento", size=(15, 1)), sg.InputText()],
            [sg.Cancel(), sg.OK()],
        ]
        window = sg.Window("Digite o código", layout)
        event, values = window.read()
        window.close()
        event, values[0]
        if "OK" in event and len(values[0]) == 13:
            self.nro_rastreamento = values[0]
        else:
            print(f'Lembre-se: para rastrear digite exatos 13 caracteres, vc digitou {len(values[0])} caracteres')
            sys.exit(0)


if __name__ == "__main__":
    # nro_rastreamento = 'PW808073941BR'
    correio = Correios()
    correio.telaInicial()
    print(correio.main())

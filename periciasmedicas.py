import os

import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
from requests import post


class Periciasmedicas:
    def __init__(self, _cpf, _dtnasc, _dig, _filename):
        self.cookies = {
            "JSESSIONID": "0000NDkoef_2_diITGgUgbfZ035:17jauq432",
        }
        self.headers = {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "http://periciasmedicas.gestaopublica.sp.gov.br",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "http://periciasmedicas.gestaopublica.sp.gov.br/eSisla/noauth/login/LoginExecute.do",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        self.url = "http://periciasmedicas.gestaopublica.sp.gov.br/eSisla/noauth/consultaExecute.do"
        self.cpf = _cpf
        self.dtnasc = _dtnasc
        self.dig = _dig
        self.homepath = os.path.expanduser(os.getenv("USERPROFILE"))
        self.desktoppath = "Desktop"
        self.lista_cabecalho = []
        self.lista_infos = []
        self.filename = filename

    def load(self):
        data = {
            "selecaoConsulta": "CPF",
            "num": f"{self.cpf}",
            "dig": f"{self.dig}",
            "dtNasc": {self.dtnasc},
            "tipoConsulta": "H",
            "x": "39",
            "y": "14",
        }
        response = post(
            self.url,
            headers=self.headers,
            cookies=self.cookies,
            data=data,
            verify=False,
        )
        return bs(response.text, "lxml")

    def get(self):
        soup = pm.load()
        try:
            msg = soup.find("h6", class_="msg_erro_centro").getText()
            print(f"CPF..:{cpf}-{dig}\nData Nasc..:{dtnasc}\n{msg}")
        except Exception as err:
            print(err)
            for cabecalho in soup.find_all("th")[:-1]:
                self.lista_cabecalho.append(cabecalho.getText())
            for r in soup.find_all("td")[:-1]:
                try:
                    if "\n\n" not in r.getText():
                        self.lista_infos.append(r.getText())
                except AttributeError as err:
                    print(err)

    def write(self):
        local_save = os.path.join(self.homepath, self.desktoppath, filename)
        with open(local_save, "w", encoding="utf8") as _file:
            for info in enumerate(self.lista_infos):
                if info[0] == 0:
                    cont_cabecalho = 0
                try:
                    _file.write(f"{self.lista_cabecalho[cont_cabecalho]}={info[1]}")
                    if "TP" in self.lista_cabecalho[cont_cabecalho]:
                        _file.write(f"\n{'*' * 70}")
                except Exception as err:
                    print(err)
                    _file.write(f"Data Agend/Exp={info[1]}")
                _file.write(f"\n")
                if info[0] % 9 == 0:
                    cont_cabecalho = 1
                else:
                    cont_cabecalho += 1

class Tela:
    def __init__(self):
        ...

    def list_folder(self, lista_info):
        layout = [
            [sg.Button("Salvar em disco", key='printer'), sg.Button("Exit", key='exit')],
            [sg.T("Source Folder")],
            [sg.Multiline(lista_info, size=[100, 250], autoscroll=True)],
        ]
        window = sg.Window("Gerenciador", layout, size=(430, 410))
        event, values = window.read()
        while True:
            if event == 'printer':
                sg.popup_auto_close('Imprimindo...', auto_close_duration=2.5)
                event = ''
            if event == 'exit':
                sg.popup_auto_close('Saindo...', auto_close_duration=0.5)
                break
        window.close()


if __name__ == "__main__":
    cpf = "204435968"
    dig = "59"
    dtnasc = "18/06/1974"
    filename = "periciasmedicas.txt"
    pm = Periciasmedicas(cpf, dtnasc, dig, filename)
    pm.get()
    tela = Tela()
    tela.list_folder(pm.lista_infos)

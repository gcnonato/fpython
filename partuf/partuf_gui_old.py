import subprocess
import PySimpleGUI as sg
import cfscrape
import fire
from bs4 import BeautifulSoup

requests = cfscrape.create_scraper()


class Partuf:
    def __init__(self):
        self.titulos = []
        self.links = []
        self.escolha = self.option()
        self.resolut = []
        self.magnetico = []
        self.tabelas = []

    def option(self, numero=0):
        # global escolha
        self.escolha = int(numero)

    def layout_inicial(self):
        # global escolha
        title = "PARTUF - SUA FERRAMENTA DE STREAMING E DOWNLOAD DE TORRENT"
        layout = [
            [sg.Text(f'{" "*16}{title}', size=(80, 2))],
            [
                sg.Text(" " * 23),
                sg.Radio("Streaming!", "1", default=True),
                sg.Radio("Download!", "1"),
                sg.Radio("Link Magnético!", "1"),
            ],
            [sg.Input(size=(80, 1))],
            [sg.Cancel(), sg.OK()],
        ]

        window = sg.Window("Partuf", layout)
        event, values = window.read()
        window.close()

        if values[0] is True:
            self.escolha = 0
        elif values[1] is True:
            self.escolha = 1
        elif values[2] is True:
            self.escolha = 2

        return values[3]

    def url_scrape(self):
        busca = self.layout_inicial()
        termos_da_busca = []
        url_final = ""
        if busca is not None:
            busca = busca.split()
            for item in range(len(busca) - 1):
                termos_da_busca.append(busca[item] + "+")
            concatenando = "".join(termos_da_busca)
            # busca[len(busca)-1] Retorna a último palavra capturada pelo input
            if len(busca) > 0:
                url = concatenando + busca[len(busca) - 1]
                url_final = "https://www.baixarfilmetorrent.net/?s=" + url
        return url_final

    def mostrar_lista_filmes(self):
        # global titulos, links

        print("\nCarregando lista de filmes...\n")
        html = self.url_scrape()
        if len(html) > 0:
            req = requests.get(html)
            soup = BeautifulSoup(req.text, "html.parser")
            listagem_da_pesquisa = soup.find_all("div", {"class": "item"})
            # titulos = []
            # links = []
            for filme in listagem_da_pesquisa:
                self.titulos.append(str(filme).split('"')[5])
                self.links.append(str(filme).split('"')[3])
            for titulo in range(0, len(self.titulos)):
                print([titulo + 1], self.titulos[titulo])

    def layout_selecionar_filmes(self):
        layout = [[sg.Listbox(self.titulos, size=(60, 18), font="Arial 18")], [sg.OK()]]
        window = sg.Window("Títulos", layout)
        event, values = window.read()
        window.close()
        posit = 666
        for p in range(0, len(self.titulos)):
            if self.titulos[p] == values[0][0]:
                posit = p
        return posit + 1

    def table(self):
        # global tabelas

        print()
        select_number = self.layout_selecionar_filmes()
        lin = self.links[select_number - 1]

        link = requests.get(lin)
        soup = BeautifulSoup(link.text, "html.parser")
        self.tabelas = soup.find_all("table")
        return None

    #######################
    # resolut = []
    # magnetico = []
    #######################

    # **PARA FILMES** Adiciona resolucoes e links magneticos as suas respectivas listas
    def lista_magneticos_do_filme_selecionado(self):
        for tabela in range(0, len(self.tabelas)):
            single_table = BeautifulSoup(str(self.tabelas[tabela]), "html.parser")
            strong = single_table.find("strong")

            try:
                html_qualidades = single_table.find_all("td", {"class": "td-mv-res"})
                html_magnetic = single_table.find_all("td", {"class": "td-mv-dow"})

                for quali in range(0, len(html_qualidades)):
                    self.resolut.append(
                        f"{html_qualidades[quali].string} {strong.string}"
                    )

                for link_mag in range(len(html_magnetic)):
                    self.magnetico.append(str(html_magnetic[link_mag]).split('"')[3])
            except Exception:
                pass

    # **PARA SERIES** Adiciona resolucoes e links magneticos as suas respectivas listas
    def lista_magneticos_da_serie_selecionada(self):
        if len(self.magnetico) == 0:
            for tabela in range(0, len(self.tabelas)):
                single_table = BeautifulSoup(str(self.tabelas[tabela]), "html.parser")
                strong = single_table.find("strong")

                # HTML para episódios da série
                html_num_epi = single_table.find_all("td", {"class": "td-ep-eps"})
                html_qualidades = single_table.find_all("td", {"class": "td-ep-res"})
                html_magnetic = single_table.find_all("td", {"class": "td-ep-dow"})

                for quali in range(0, len(html_qualidades)):
                    self.resolut.append(
                        f"{html_num_epi[quali].string.replace('Ep.', '-')}"
                        f" {'->>'} {html_qualidades[quali].string} {strong.string}"
                    )
                    self.magnetico.append(str(html_magnetic[quali]).split('"')[3])

            self.magnetico.append("")
            self.resolut.append("")

    def layout_selecionar_resolucao(self):
        if len(self.magnetico) != 0:
            for cont in range(0, len(self.magnetico)):
                print([cont + 1], self.resolut[cont])

        layout = [[sg.Listbox(self.resolut, size=(60, 18), font="Arial 18")], [sg.OK()]]
        window = sg.Window("Resolut", layout)
        event, values = window.read()
        window.close()

        posit = 666
        for p in range(0, len(self.resolut)):
            if self.resolut[p] == values[0][0]:
                posit = p
        return posit + 1

    def opcoes_de_uso(self):
        # global escolha
        selected_resolution = self.layout_selecionar_resolucao()
        mag_final = self.magnetico[selected_resolution - 1]
        print(self.escolha)

        if self.escolha == 0:
            print("\nAguarde o carregamento... \nEnjoy!!")
            # try:
            #     # start = subprocess.check_call(["peerflix", mag_final, "--path", os.getcwd(), "--vlc"])
            #     start = subprocess.Popen(["peerflix", mag_final, "--vlc"], shell=True)
            # except FileNotFoundError as err:
            #     print(f"Error.: {err}\n{self.escolha}")

        elif self.escolha == 1:
            print("\nDownload iniciado... ")
            # start = subprocess.check_call(["peerflix", mag_final, "--path", os.getcwd()])
            subprocess.Popen(["peerflix", mag_final], shell=True)

        elif self.escolha == 2:
            print(f"\nLink magnético:\n{mag_final}\n")


if __name__ == "__main__":
    pu = Partuf()
    fire.Fire(pu.option())
    while True:
        # Essa função chama outra função chamada "url_scrape(), a "url_scrape" chama a "layout_inicial()".
        pu.mostrar_lista_filmes()
        if len(pu.titulos):
            pu.table()  # Table chama "layout_selecionar_filmes()"
            pu.lista_magneticos_do_filme_selecionado()
            pu.lista_magneticos_da_serie_selecionada()
            pu.opcoes_de_uso()
        else:
            print("Não há títulos! :-(")
            break

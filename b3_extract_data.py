# -*- coding: utf-8 -*-
import pandas as pd
import time
import datetime
import shutil
import os
import glob
import zipfile
import pathlib
import plotly.figure_factory as ff
from selenium import webdriver

class B3:

    def __init__(self):
        homepath = os.path.expanduser(os.getenv("USERPROFILE"))
        desktoppath = "Desktop"
        folder_downloads = "Downloads"
        # Define o nome do diretório onde está o arquivo baixado
        self.path_to_folder_downloads = os.path.join(homepath, folder_downloads)
        self.path_to_desktop = os.path.join(homepath, desktoppath)
        self.src = pathlib.Path(self.path_to_folder_downloads)
        self.dst = pathlib.Path(self.path_to_desktop)


    def function_path(self):
        # Recebe os arquivos do diretório na variavel
        files = os.listdir(self.src)

        # Verifica se possui algum arquivo com a extensão ZIP e TXT no diretório, e se estiver, deleta o arquivo
        for file in files:
            if file.lower().endswith(('.zip', '.txt')):
                print(os.path.join(self.src, file))
                os.remove(os.path.join(self.src, file))

    def function_chromedriver(self):

        # A URL abaixo foi retirado do link do site
        # http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/codigo-isin/pesquisa/

        # Coloque a URL abaixo
        url = "https://sistemaswebb3-listados.b3.com.br/isinPage/#accordionBodyTwo"

        # Para abrir o Chrome automaticamente, deve baixar o driver chromedriver de acordo com a versão da web instalado
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--allow-running-localhost')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        # A partir dessa etapa, ele virá fazer tudo automaticamente dentro do browser
        # Abre o browser do Google Chrome automaticamente
        browser = webdriver.Chrome(options = options)

        # Obtém os dados através da variavel URL
        browser.get(url)

        # Aguarda 10 segundos, para o link do site ser carregado antes de ser clicado automaticamente
        time.sleep(5)

        # Clica na caixa para abrir o link onde está o Downloads
        browser.find_element_by_xpath("//a[@class='collapsed']").click()
        time.sleep(1)
        # Através do browser ele clica no item que faz o download dos arquivos necessários.
        browser.find_element_by_xpath("//a[@class='click-p']").click()

        # Adiciona 1 segundo enquanto o arquivo baixado com a extensão zip não constar no diretório, antes de fechar o browser
        # Após ser baixado, adiciona o nome do arquivo para uma variável
        while not glob.glob(str(self.src) + "\*.zip"):
            time.sleep(1)
        else:
            print("Arquivo baixado do link " + str(url))

        # Fecha o browser
        browser.close()

        # Aguarda 5 segundos, para o arquivo ser baixado corretamente
        time.sleep(5)

    def function_pandas(self):
        # Recebe os arquivos do diretório na variavel
        files = os.listdir(self.path_to_desktop)

        MetadataFiles = pd.DataFrame([])
        # Verifica se possui algum arquivo com a extensão zip no diretório
        for file in files:
            if file.lower().endswith('.zip'):
                zip = os.path.join(self.path_to_desktop, file)
                # print(zip)
                # Caso tenha o arquivo zip, cria um data frame para vermos os dados dentro do arquivo zip
                with zipfile.ZipFile(zip) as myzip:
                    for info in myzip.infolist():
                        MetadataFiles = \
                            MetadataFiles.append(
                                pd.DataFrame(
                                    {'ZipFile': [os.path.basename(zip)],
                                     'FileName': [info.filename],
                                     'Extension': [os.path.splitext(info.filename)[1].lower()],
                                     'Size': [str(info.file_size/1000) + ' Kb'],
                                     'Directory': [self.src],
                                     'Modified': [str(datetime.datetime(*info.date_time))]}
                                )
                            )
                        df = pd.DataFrame(
                            MetadataFiles,
                                columns = [
                                    'ZipFile',
                                    'FileName',
                                    'Extension',
                                    'Size',
                                    'Directory',
                                    'Modified'
                                ]
                            )
                        # Mostra os data frame criado dentro do aquivo zip
                        print(df.head())
        # Cria a tabela do plotly de acordo com o data frame criado anteriormente
        fig = ff.create_table(df)

        # Exibe a tabela
        # fig.show()

        # Extrai somente os arquivos com a extensão TXT do arquivo zip na variavel do diretório de destino
        QtdArq = 0
        with zipfile.ZipFile(zip) as myzip:
            for FileName in myzip.namelist():
                if FileName.lower().endswith(".txt"):
                    myzip.extract(FileName, self.src)
                    QtdArq += 1

        # Exibe uma mensagem que foi descompactado corretamente
        # print("Foram descompactados " + str(QtdArq) + " arquivos")

        # Renomeia o arquivo descompactado para o nome desejado, e salva no diretório de destino da variavel dst
        filename_emissor = "EMISSOR.TXT"
        filename_numeraca = "NUMERACA.TXT"
        filename_emissor_novo = "I_EMISSOR.TXT"
        filename_numeraca_novo = "I_NUMERACA.TXT"
        try:
            os.rename(
                pathlib.Path(os.path.join(
                        str(self.src),filename_emissor)
                ),
                pathlib.Path(os.path.join(
                        str(self.src),filename_emissor_novo)
                )
            )
            os.rename(
                pathlib.Path(os.path.join(
                        str(self.src),filename_numeraca)
                ),
                pathlib.Path(os.path.join(
                        str(self.src),filename_numeraca_novo)
                )
            )
        except FileExistsError as err:
            print(err)
            # os.remove(os.path.join(self.src, file))


        # Copia os arquivos extraidos o para o diretório da variavel dst
        QtdArq = 0
        for file in files:
            if os.path.isfile(os.path.join(self.src, file)):
                if file.lower().endswith('.txt'):
                    shutil.copy(os.path.join(self.src, file), self.dst)
                    QtdArq += 1

        # Exibe uma mensagem de quantos arquivos foram copiados
        print("Foram copiados " + str(QtdArq) + " arquivos para o diretório " + str(self.dst))



if __name__ == '__main__':
    b3 = B3()
    # b3.function_chromedriver()
    b3.function_pandas()

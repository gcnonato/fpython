import json
import random
from pprint import pprint
from time import sleep

from requests import get


class Jogodavelha:
    def __init__(self):
        self.jogador_X = ''
        self.jogador_O = ''
        self.vez = 0
        self.lista_nomes = []
        self.ler_cidades_e_pegar_nomes()
        self.tabuleiroVazio = {}
        self.criar_tabuleiro()
        self.palpitesVazios = [nro for nro in range(1, 10)]
        self.lista_de_posicoes = []
        self.lista_totalpalpites = []


    def ler_cidades_e_pegar_nomes(self):
        url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade=3300100'
        for pessoas in get(url).json():
            for pessoa in pessoas['res']:
                self.lista_nomes.append(pessoa['nome'])

    def tabuleiro(self, **posicao):

        print(" {} | {} | {} ".format(posicao["pos1"], posicao["pos2"], posicao["pos3"]))
        print("------+------+------")
        print(" {} | {} | {} ".format(posicao["pos4"], posicao["pos5"], posicao["pos6"]))
        print("------+------+------")
        print(" {} | {} | {} ".format(posicao["pos7"], posicao["pos8"], posicao["pos9"]))
        contar_jogadas = 0
        vez = 0
        if vez > 0:
            vez = 0

    def is_exists(self, jogada, jogador):
        try:
            len(self.tabuleiro[f'pos{jogada}'])
            self.tabuleiro[f'pos{jogada}'] =
        except KeyError as err:
            print("Você digitou um número já pedido, tente novamente")


    def is_valid(self, jogada):
        while True:
            try:
                jogada = int(jogada)
                break
            except:
                print("Você não digitou um número válido, tente novamente")
                jogada = input("Digite uma posição no tabuleiro para jogar: ")
        return jogada


    def pedir_jogada(self):
        print("-=-" * 15)
        if self.vez == 0:
            jogada = input(self.jogador_1 + ", digite uma posição no tabuleiro para jogar: ")
            jogada = self.is_valid(jogada)
            self.is_exists(jogada)
            vez = 1
        else:
            jogada = input(self.jogador_2 + ", digite uma posição no tabuleiro para jogar: ")
        print("-=-" * 15)
        return jogada


    def verifica_jogada(jogada, numero_jogadas, **posicao):
        for key, value in posicao.items():
            # if jogada == value:
            if numero_jogadas % 2 == 0:
                posicao[key] = "X"
            else:
                posicao[key] = "O"
        return posicao


    def procurar_vencedor(**posicao):
        possiveis_1 = posicao["pos1"] == posicao["pos4"] == posicao["pos7"]
        possiveis_2 = posicao["pos1"] == posicao["pos2"] == posicao["pos3"]
        possiveis_3 = posicao["pos1"] == posicao["pos5"] == posicao["pos9"]
        possiveis_4 = posicao["pos2"] == posicao["pos5"] == posicao["pos8"]
        possiveis_5 = posicao["pos3"] == posicao["pos6"] == posicao["pos9"]
        possiveis_6 = posicao["pos4"] == posicao["pos5"] == posicao["pos6"]
        possiveis_7 = posicao["pos7"] == posicao["pos8"] == posicao["pos9"]
        possiveis_8 = posicao["pos3"] == posicao["pos5"] == posicao["pos7"]
        lista_possiveis = [
            possiveis_1,
            possiveis_2,
            possiveis_3,
            possiveis_4,
            possiveis_5,
            possiveis_6,
            possiveis_7,
            possiveis_8,
        ]
        for possiveis in lista_possiveis:
            if possiveis == True:
                print("Temos um vencedor! Parabéns!")
                return True
            elif contar_jogadas == 8:
                print("Deu velha! Ninguém ganhou.")
                return True


    def criar_tabuleiro(self):
        tabuleiro = {}
        for nro in range(1, 10):
            tabuleiro[f'pos{nro}'] = nro
        self.tabuleiroVazio = tabuleiro
        # return {
        #     "pos1": 1,
        #     "pos2": 2,
        #     "pos3": 3,
        #     "pos4": 4,
        #     "pos5": 5,
        #     "pos6": 6,
        #     "pos7": 7,
        #     "pos8": 8,
        #     "pos9": 9,
        # }


    def denovo():
        jogar_denovo = input(
            """
            Deseja jogar novamente?
            Digite S para SIM ou N para NÃO.
        """
        )
        if jogar_denovo.upper() == "S":
            print("Bem Vindo ao Jogo da Velha! Vamos começar!")
            print("-=-" * 15)
            return True
        elif jogar_denovo.upper() == "N":
            print("Até logo!")
            return False
        else:
            return denovo()

if __name__ == '__main__':
    # print("Bem Vindo ao Jogo da Velha! Vamos começar!")
    jogo = Jogodavelha()
    try:
        jogo.jogador_X = jogo.lista_nomes.pop(random.randint(0, len(jogo.lista_nomes)))
    except:
        jogo.jogador_O = jogo.lista_nomes.pop(random.randint(0, len(jogo.lista_nomes)))
    try:
        jogo.jogador_X = jogo.lista_nomes.pop(random.randint(0, len(jogo.lista_nomes)))
    except:
        jogo.jogador_O = jogo.lista_nomes.pop(random.randint(0, len(jogo.lista_nomes)))
    # jogo.jogador_1 = input("Qual é o seu nome? ")
    print("Olá " + jogo.jogador_1 + ", você jogará com X")
    # jogo.jogador_2 = input("Qual é o seu nome? ")
    print("Olá " + jogo.jogador_2 + ", você jogará com O")
    print("-=-" * 15)
    posicao = jogo.tabuleiroVazio
    jogo.lista_totalpalpites = jogo.palpitesVazios
    # print(lista_totalpalpites)
    jogada = jogo.pedir_jogada(jogo.lista_totalpalpites, jogo.vez)
    # while True:
        # tabuleiro(**posicao)
        # jogada = pedir_jogada(lista_totalpalpites)
    #     lista_totalpalpites[jogada - 1] = "X"
    #     posicao = verifica_jogada(jogada, contar_jogadas, **posicao)
    #     if procurar_vencedor(**posicao):
    #         contar_jogadas = 0
    #         tabuleiro(**posicao)
    #         posicao = tabuleiroVazio()
    #         lista_totalpalpites = palpitesVazios()
    #     if not denovo():
    #         break
    #
    #     contar_jogadas += 1
    #     if vez == 0:
    #         vez += 1
    #     else:
    #         vez = 0

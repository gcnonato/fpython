# -*- coding: utf-8 -*-
"""
4. Crie uma classe "Televisao" e uma classe "ControleRemoto" que pode controlar o volume e trocar os canais da tevisão.
      - O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
      - O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém,
      também possibilita
        trocar para um canal indicado;
      - Também devem existir métodos para consultar o valor do volume de som e o canal selecionado.
"""
import os


class Televisao:
    def __init__(self):
        self.__canal_atual = 0
        self.__volume_atual = 0

    def controla_volume(self, valor):
        if valor == "+":
            if self.__volume_atual < 30:
                self.__volume_atual += 1
            else:
                print("Volume está no máximo!")
        elif valor == "-":
            if self.__volume_atual > 0:
                self.__volume_atual -= 1
            else:
                print("Volume está no mímino!")

    def controla_canal(self, canal):
        if canal == "+":
            self.__canal_atual += 1
        elif canal == "-":
            self.__canal_atual -= 1
        else:
            self.__canal_atual = canal

    def volume(self):
        return self.__volume_atual

    def canal(self):
        return self.__canal_atual


class ControleRemoto:
    def __init__(self, tv):
        self.__tv = tv

    def controlar_volume(self, valor):
        self.__tv.controla_volume(valor=valor)

    def controlar_canal(self, canal):
        self.__tv.controla_canal(canal=canal)


def menu():
    while True:
        print("=" * 90)
        print(f'{"Sistema de Controle da Televisão":^90}')
        print(f'{"MENU":^90}')
        print("=" * 90)
        print("(1) Para Controle do Volume")
        print("(2) Para Controle de Canais")
        print("(3) Para Finalizar o Sistema")
        opcao = input("Informe sua opção: ")
        print("=" * 90)
        if opcao == "1":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("-" * 90)
                print(f'{"VOLUME":^90}')
                print(f'{"(+) para aumentar | (-) para diminuir | (x) para sair":^90}')
                print(f"Volume Atual: {tv32.volume()}")
                print("-" * 90)
                volume = input("Informe sua opção: ")
                if volume == "+" or volume == "-":
                    controle.controlar_volume(valor=volume)
                    os.system("clear")
                elif volume == "x":
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                elif volume != "+" or volume != "-":
                    print("Opção invalida!")
                    break
        if opcao == "2":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("-" * 90)
                print(f'{"TROCAR de CANAL":^90}')
                print(
                    f'{"(+) para aumentar | (-) para diminuir | (i) para indicar um CANAL | (x) para sair":^90}'
                )
                print(f"Canal Atual: {tv32.canal()}")
                print("-" * 90)
                canal = input("Informe sua opção: ")
                if canal == "+" or canal == "-":
                    controle.controlar_canal(canal=canal)
                    os.system("cls" if os.name == "nt" else "clear")
                elif canal == "x":
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                elif canal == "i" or canal == "I":
                    try:
                        canal = int(input("Informe o canal: "))
                        controle.controlar_canal(canal=canal)
                    except ValueError:
                        print("Valor inválido!")
                elif canal != "+" or canal != "-":
                    print("Opção invalida!")
                    break
        elif opcao == "3":
            print("Finalizando Sistema...")
            break
        else:
            print("Opção inválida!")
            os.system("cls" if os.name == "nt" else "clear")


os.system("cls" if os.name == "nt" else "clear")

tv32 = Televisao()

controle = ControleRemoto(tv=tv32)

menu()

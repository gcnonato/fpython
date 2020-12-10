# -*- coding: utf-8 -*-
import os
import platform
import webbrowser

from clint.textui import colored
from googlesearch import search

sistema = platform.platform()
if "win" in sistema.lower():
    cmd_limpar = "cls"
else:
    cmd_limpar = "clear"

os.system(cmd_limpar)
print(colored.blue(
    """Encontrando links da REDE ONION
           Ryan Aragão - BurnSec
    """
    )
)


def menu():
    print(
        """
0. Sair
1. Sites Onion
2. Como Usar
3. Créditos

    """
    )


while True:
    # menu()
    # opcao = int(input("Digite a opção: "))
    opcao = 1
    if opcao == 0:
        os.system(cmd_limpar)
        break
    elif opcao == 1:
        print("")
        # conteudo = str(input("Conteúdo:"))
        conteudo = str("python")
        # dork = f'{conteudo} site:onion.link | site:onion.cab | site:onion.sh | site:tor2web.fi | site:onion.direct'
        dork = f"{conteudo} site:www.stackoverflow.com | site:www.baboo.com.br"
        with open("../" "sitesonion.txt", "w") as stream:
            print(stream)
            for url in search(dork, stop=50 or 1):
                print(url, file=stream)
        os.system(cmd_limpar)
        print("-----------------------------------------------------")
        print("Os links foram salvos no seguinte txt: sitesonion.txt")
        print("-----------------------------------------------------")
        input("Pressione ENTER para continuar")
        os.system(cmd_limpar)
    elif opcao == 2:
        webbrowser.open("https://github.com/burnsecurity/onionlinks")
        webbrowser.open("https://www.instagram.com/burnsecurity/")
    elif opcao == 3:
        os.system(cmd_limpar)
        print("Criado por: Ryan Aragão")
        print("Equipe: BurnSec")
        print("Instagram: @burnsecurity")
        print("-----------------------------------------------------")
        input("pressione ENTER para continuar")
        os.system(cmd_limpar)
    else:
        print("Essa opção não existe, tente novamente!")

import os
from time import sleep


class Sorveteria:
    """
        A class to represent a sorveteria.
        ...
        Attributes
        ----------
        name : str
            first name of the person
        surname : str
            family name of the person
        age : int
            age of the person
    """

    def __init__(self):
        self.produtos = [
            ["A", "Refrigerante", 3.50],
            ["B", "Casquinha Simples", 4.00],
            ["C", "Casquinha Dupla", 5.50],
            ["D", "Sundae", 7.50],
            ["E", "Banana Split", 9.00],
        ]
        self.vendas = {
            "A": ["Refrigerante", 3.50, 0, 0],
            "B": ["Casquinha Simples", 4.00, 0, 0],
            "C": ["Casquinha Dupla", 5.50, 0, 0],
            "D": ["Sundae", 7.50, 0, 0],
            "E": ["Banana Split", 9.00, 0, 0],
        }
        self.contador_vendas = 0

    def mostra_menu(self, matriz_produtos):
        # print(f("Código" < 8)("Produto" < 19)("Preço (R$)" < 10))
        print(f"\nCódigo{' '*14}Produto{' '*20}Preço\n{'-'*52}")
        for produto in matriz_produtos:
            # print(f(produto[0] ^ 8)(produto[1] < 19)(produto[2] ^ 10.2))
            print(f"{produto[0].ljust(20)}{produto[1].ljust(27)}{str(produto[2])}")
        print(f"{'-' * 52}")
        return

    def nova_venda(self):
        tot_pagar = 0
        os.system("cls" if os.name == "nt" else "clear")
        self.mostra_menu(self.produtos)
        while True:
            codigo = (
                str(input("\nDigite o código do produto (0 para finalizar): "))
                .upper()
                .strip()
            )
            if codigo not in ("A", "B", "C", "D", "E", "0"):
                print("Produto não disponível")
                continue
            if codigo == "0":
                print(f"\nTotal a pagar nesta compra:R$[{tot_pagar:.2f}])")
                sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                break
            qnt = int(input(f"Quantidade de {self.vendas[codigo][0]}?: "))
            self.vendas[codigo][2] += qnt
            tot_pagar += qnt * self.vendas[codigo][1]
            self.vendas[codigo][3] += qnt * self.vendas[codigo][1]
        return

    def relatorio(self):
        total = 0
        print("Relatório do dia".center(20, "*"))
        print(
            f'\n{"-"*49}\n{"Produto":<19} {"Quantidade":<10} {"Preço":<10} {"Total" :<16}'
        )
        for produto in self.vendas.values():
            if produto[2] > 0:
                print(
                    f"{produto[0]:<19}  {produto[2]:^10} {produto[1]:^10}  {produto[3]:^16.2f}"
                )
                total += produto[3]
        print(f"\nTotal arrecadado no dia: R$ {total:.2f}")
        print(f"Valor médio em cada compra: R$ {total/self.contador_vendas:.2f}")

    def menu(self):
        while True:
            op = str(input("Sistema Sorveteria\n[1] Nova venda\n[2] Fechar")).strip()
            if op == "1":
                self.contador_vendas += 1
                self.nova_venda()
            elif op == "2":
                os.system("cls" if os.name == "nt" else "clear")
                self.relatorio()
                break
            else:
                print("Opção não reconhecida")
                sleep(2)
                os.system("cls" if os.name == "nt" else "clear")

    def __str__(self):
        return "sim, é possível usar doctest"


def sorvetery():
    """
    >>> sorveteria = Sorveteria()
    >>> str(sorveteria)
    'sim, é possível usar doctest'
    >>> sorveteria.contador_vendas
    0
    >>> sorveteria.produtos[0][0]
    'A'

    """


if __name__ == "__main__":
    sorveteria = Sorveteria()
    sorveteria.menu()

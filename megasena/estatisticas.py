#!/usr/local/bin/python
# coding: utf-8
"""
Script que mostra informações com base nos jogos antetiores da Mega-Sena
"""
import os

import numpy as np
from decimal import Decimal
from collections import OrderedDict
from html_table_parser.parser_functions import extract_tables, make2d


class Estatistica:
    def __init__(self):
        self.numbers = {}
        self.winners = []
        self.prizes = []
        self.sorted_numbers = 0
        self.listed_numbers = 0
        self.more_frequent_numbers = 0
        self.less_frequent_numbers = 0
        self.open_csv()

    def show_statistics(self):
        """ Mostra na tela informações sobre os jogos anteriores """
        print('Analisando...')

        # Lendo dados do arquivo HTML...
        for line in self.data:
            # Soma ocorrência de cada número:
            for num in range(2, 8):
                num = line[num]
                if num not in self.numbers:
                    self.numbers[num] = 0
                self.numbers[num] += 1

            # Quantidade de ganhadores
            winners_qty = int(line[9])
            self.winners.append(winners_qty)

            # Total do prêmio
            prize_value = line[12].replace('.', '').replace(',', '.')
            prize_total = Decimal(prize_value) * Decimal(winners_qty)
            self.prizes.append(prize_total)

        # Ordena os números sorteados por ocorrência
        self.sorted_numbers = OrderedDict(sorted(self.numbers.items(), key=lambda x: x[1], reverse=True))
        self.listed_numbers = [n for n in self.sorted_numbers.keys()]
        self.more_frequent_numbers = sorted(self.listed_numbers[:10])
        self.less_frequent_numbers = sorted(self.listed_numbers[-10:])
        self.less_frequent_numbers.reverse()

        print('\nConcursos de %s até %s:' % (self.data[0][1], self.data[-1][1]))
        print('    Concursos realizados: %s\n' % self.format_number(len(self.data)))

        print('    Total de ganhadores: %s' % self.format_number(int(np.sum(self.winners))))
        print('    Média de ganhadores por concurso: %s\n' % self.format_number(float(np.mean(self.winners))))

        print('    Total em prêmios concedidos: R$ %s' % self.format_number(int(np.sum(self.prizes))))
        print('    Média de prêmio por concurso: R$ %s\n' % self.format_number(int(np.mean(self.prizes))))

        print('    Os 10 números mais frequêntes: %s' % ', '.join(self.more_frequent_numbers))
        print('    Os 10 números menos frequêntes: %s' % ', '.join(self.less_frequent_numbers))

    def format_number(self, number):
        """ Formata número para BRL """
        if type(number) == int:
            return '{:0,}'.format(number).replace(',', '.')
        return '{0:.2f}'.format(number).replace('.', ',')

    def open_csv(self):
        print(os.getcwd())
        with open('data/d_mega.htm') as file:
            tables = extract_tables(file.read())
            self.data = make2d(tables[0])[1:]

    def retornar_os_10_mais_sorteados(self):
        for line in self.data:
            # Soma ocorrência de cada número:
            for num in range(2, 8):
                num = line[num]
                if num not in self.numbers:
                    self.numbers[num] = 0
                self.numbers[num] += 1
        self.sorted_numbers = OrderedDict(sorted(self.numbers.items(), key=lambda x: x[1], reverse=True))
        self.listed_numbers = [n for n in self.sorted_numbers.keys()]
        self.more_frequent_numbers = sorted(self.listed_numbers[:10])
        self.more_frequent_numbers = [int(n) for n in self.more_frequent_numbers]
        return self.more_frequent_numbers


if __name__ == '__main__':
    estatistic = Estatistica()
    # estatistic.show_statistics()
    os_10_mais = estatistic.retornar_os_10_mais_sorteados()
    print(os_10_mais)

#!/usr/local/bin/python
# coding: utf-8
"""
Script que gera um número para jogar na Mega-Sena
"""

from megasena.estatisticas import Estatistica


def generate_number(qty, os_dez_numeros_mais_frequentes):
    """ Retorna a quantidade de dezenas aleatórias informadas em 'qty' """
    # numbers = list(range(1, 61))
    numbers = os_dez_numeros_mais_frequentes
    # random.shuffle(numbers)

    selected_numbers = []
    even_numbers = 0
    odd_numbers = 0

    for num in numbers:
        # Permite incluir apenas X números
        if len(selected_numbers) == qty:
            break

        # Não inclui os números menos frequêntes
        # if num in [26, 55, 60, 40, 22, 39, 21, 57, 19, 25]:
        #    continue

        # Impede mais de um número na mesma coluna
        if num > 9:
            has_similar = False
            for sel in selected_numbers:
                if str(num)[-1] == str(sel)[-1]:
                    has_similar = True
                    break
            if has_similar:
                continue

        # Impede sequências
        if (num + 1) in selected_numbers or (num - 1) in selected_numbers:
            continue

        # Garante a mesma quantidade de pares e ímpares
        if num % 2 and odd_numbers > even_numbers:
            continue
        if not num % 2 and even_numbers > odd_numbers:
            continue

        # Incluí número
        selected_numbers.append(num)

        # Soma quantidade de pares e ímpares
        if num % 2:
            odd_numbers += 1
        else:
            even_numbers += 1

    # Ordena e formata números selecionados
    selected_numbers.sort()
    selected_numbers = [str(num).rjust(2, '0') for num in selected_numbers]

    print('Seu número é... %s' % ' '.join(selected_numbers))
    return selected_numbers
    # print('Boa sorte!')


def jogo_esta_na_lista_de_jogos(cartela_nova, cartelas_geradas_anteriormente):
    for number_da_nova_cartela in cartela_nova:
        # print(number_da_nova_cartela)
        if number_da_nova_cartela in cartelas_geradas_anteriormente:
            print('Número já está em jogos anteriores')
            return False
    return True


if __name__ == '__main__':
    estatistica = Estatistica()
    os_dez_numeros_mais_frequentes = estatistica.retornar_os_10_mais_sorteados()
    quantidade_de_cartelas = 5
    quantidade_de_numero_por_cartela = 6
    cartelas_geradas_anteriormente = []
    for cartela in range(quantidade_de_cartelas):
        cartela_nova = generate_number(quantidade_de_numero_por_cartela, os_dez_numeros_mais_frequentes)
        naoTemEssaCartela = jogo_esta_na_lista_de_jogos(
            cartela_nova, cartelas_geradas_anteriormente
        )
        if naoTemEssaCartela:
            cartelas_geradas_anteriormente.append(cartela_nova)
    # print(cartelas_geradas_anteriormente)

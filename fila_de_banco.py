# total_casos = int(input('Digite.: '))
# while total_casos > 0:
#     # Escreva aqui sua solucao
#     total = 0
#     print(total)
#     total_casos -= 1

def testar_fila(clients:dict) -> int :
    """ A primeira linha contém um inteiro N, indicando o número de casos de teste a seguir.
        Cada caso de teste inicia com um inteiro M (1 ≤ M ≤ 1000), indicando o número de clientes.
        Em seguida haverá M inteiros distintos Pi (1 ≤ Pi ≤ 1000), onde o i-ésimo inteiro indica o
        número recebido via sms do i-ésimo cliente.
        Os inteiros acima são dados em ordem de chegada, ou seja, o primeiro inteiro diz respeito
        ao primeiro cliente a chegar na fila, o segundo inteiro diz respeito ao segundo cliente, e assim sucessivamente.

    >>> testar_fila([[3,'2121-3200'],[2,'2221-4432'],[4,'3221-0000']])
    2221-4432
    """
    m = len(clients) # numero de clientes
    p = clients[1][1] # numero sms
    return p

if __name__ == "__main__":
    import doctest
    doctest.testmod()
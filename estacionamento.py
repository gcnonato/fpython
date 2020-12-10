# -*- coding: utf-8 -*-

horarios = []
vagas_guardadas = []
vagas = {
    "1": [0],
    "2": [0],
    "3": [0],
    "4": [0],
    "5": [0],
    "6": [0],
    "7": [0],
    "8": [0],
    "9": [0],
    "10": [0],
}


def lerArquivo():
    s = "entrada.txt"
    with open(s) as _file:
        text = _file.readlines()
    return text


def nro_da_vaga(vagas, vaga, preco, veiculo):
    """Passo a vaga no indice e vou somando o que já está salvo
    como valor ex. vagas['1':10]"""
    # print(
    #     'Na vaga {} entrou um {} - R$ {} reais'.format(vaga[0], veiculo, preco)
    # )
    vagas["{}".format(vaga[0])][0] += preco


texto = lerArquivo()


for t in range(12):
    # print('Hora{}: {}'.format(t+1, texto[t]))
    horarios.append(texto[t])
    """Intera na lista de horas e separa numa lista de vagas"""
    # for h in range(12):
    for h in horarios:
        # print('Vaga {}: {}'.format(h, h))
        # print(h)
        vagas_guardadas.append(h)
    horarios = []

for v in vagas_guardadas:
    if not v.startswith("0"):
        for j in v.split():
            j = j.split("-")
            if j[1] == "1":
                nro_da_vaga(vagas, j, 3, "moto")
            if j[1] == "2":
                nro_da_vaga(vagas, j, 5, "carro")
            if j[1] == "3":
                nro_da_vaga(vagas, j, 10, "caminhão")

soma = 0
print("Vaga          Valor arrecadado")
for key, value in vagas.items():
    print(u"  {}            R$ {} reais".format(key, value[0]))
    soma += value[0]
print(u"{} \nTotal de:   R$ {} reais".format("-" * 40, soma))

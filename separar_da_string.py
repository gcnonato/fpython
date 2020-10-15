lista = []
with open('arquivo.txt', encoding="utf-8") as _file:
    f = _file.readlines()
for tex in f:
    lista.append(tex.split(' ')[1])
    lista.append(tex.split(' ')[2])
    lista.append(tex.split(' ')[3])
for r in lista:
    print(f'{r}\n')

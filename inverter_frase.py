# -*- coding: utf-8 -*-
palavra = "blue is sky the"
frase = ""
frase_ultima = ""
frase_antes = ""
espaco = 0

qt_de_espaco = len([p for p in palavra if p in " "])

for p in palavra:
    if p not in " ":
        frase += p
    else:
        frase_antes += "".join((frase, " "))
        frase = ""
        espaco += 1
    if qt_de_espaco == espaco:
        frase_ultima = frase
print(frase_ultima, frase_antes)

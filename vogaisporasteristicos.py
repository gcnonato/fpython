def trocaVogaisConsecutivas(s):
    vogal = "aAeEiIoOuU"
    tam = len(s)
    if tam == 0:
        return ''

    if tam > 2 and s[0] in vogal and s[1] in vogal and s[2] in vogal:
        return "*" + trocaVogaisConsecutivas(s[2:])

    elif tam > 1 and s[0] in vogal and s[1] in vogal:
        return "*" + trocaVogaisConsecutivas(s[2:])

    else:
        return s[0] + trocaVogaisConsecutivas(s[1:])

palavras = ["iguais", "Aguai", "Uruguaiana", "criogenia", "Coroa"]

for palavra in palavras:
    print(trocaVogaisConsecutivas(palavra))

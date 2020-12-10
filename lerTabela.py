# -*- coding: utf-8 -*-
import json
import rows

FILENAME = "../players_br.txt"


def lerArquivo():
    with open(FILENAME) as _file:
        resultado = json.dumps(_file.read(), indent=4, ensure_ascii=False)
    return resultado


def t_rows(data):
    table = rows.import_from_dicts(data)
    for person in table:
        print_person(person)


def print_person(person):
    print("{} is {} years old.".format(person.name, person.age))

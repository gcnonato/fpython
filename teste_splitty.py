from pprint import pprint
from json import dump
import os
import re
import json
from splitty import (
    list_by_re_pattern,
    make_intervals,
    apply_intervals,
    clear_list_strings,
)


class Example:
    def __init__(self):
        vara_names = ["Vara Cível", "Vara Federal"]
        varas = ["1ª", "2º"]
        processos = [
            "Matou por motivo fútil",
            "prevaricação ao cliente",
            "Matou a mulher",
        ]
        nroproceso = ["332345666", "099932002", "097475757"]
        # processos_por_vara = {}
        # for vara_name, vara in zip(vara_names, varas):
        #     processo_por_numero = {}
        #     for processo, nroproceso in zip(processos, nroproceso):
        #         processo_por_numero[nroproceso] = ''.join(processo)
        #         # processo_por_numero[get_process_number(processo)] = ''.join(processo)
        #     processos_por_vara[vara_name] = processo_por_numero

        processos = {
            vara_name: {
                nroproceso: "".join(processo)
                for processo, nroproceso in zip(processos, nroproceso)
            }
            for vara_name, vara in zip(vara_names, varas)
        }
        pprint(processos)

        # with open('teste.json', 'w') as f:
        #     dump(processos_por_vara, f, indent=2, ensure_ascii=False, sort_keys=True)


class Luxu:
    def __init__(self):
        self.filename = "iamspe.txt"
        self.dicionario = {}
        self.list_medical = {}
        self.especialidades = [
            "ANÁLISES CLÍNICAS",
            "ANATOMIA PATOLÓGICA",
            "CARDIOLOGIA",
            "CIRURGIA GERAL",
            "CIRURGIA VASCULAR",
            "CLÍNICA MÉDICA",
            "COLONOSCOPIA",
            "COLPOSCOPIA",
            "DERMATOLOGIA",
            "ECOCARDIOGRAMA",
            "ELETROCARDIOGRAMA",
            "ELETROENCEFALOGRAMA",
            "ENDOCRINOLOGIA",
            "ENDOSCOPIA DIGESTIVA ALTA",
            "FISIOTERAPIA",
            "GASTROENTEROLOGIA CLÍNICA",
            "GINECOLOGIA",
            "GINECOLOGIA E OBSTETRÍCIA",
            "HEMODINÂMICA",
            "HOLTER",
            "HOSPITAL",
            "MAPA",
            "MATERNIDADE",
            "MEDICINA NUCLEAR",
            "NEUROCLINÍCA",
            "OFTALMOLOGIA",
            "ORTOPEDIA",
            "OTORRINOLARINGOLOGIA",
            "PAPANICOLAU (COLPOCITOLOGIA)",
            "PEDIATRIA",
            "PRONTO-SOCORRO",
            "QUIMIOTERAPIA",
            "RADIOLOGIA",
            "RESSONÂNCIA MAGNÉTICA",
            "REUMATOLOGIA",
            "TESTE ERGOMÉTRICO",
            "TOMOGRAFIA COMPUTADORIZADA",
            "ULTRASSONOGRAFIA",
            "UROLOGIA",
        ]
        # homepath = os.path.expanduser(os.getenv('USERPROFILE'))
        # desktoppath = 'Desktop'
        # local_save = os.path.join(homepath, desktoppath, filename)

    def loadarchive(self):
        # global dicionario
        with open(self.filename, encoding="utf8") as f:
            files = clear_list_strings(f.readlines())
        frase = ""
        for file in files:
            if "MUNICÍPIO: PRESIDENTE PRUDENTE" not in file:
                # print(file)
                if "****" in file:
                    # print(frase)
                    if len(frase) > 0:
                        if len(frase) == 2:
                            self.dicionario = {
                                frase.split("\n")[0]: [
                                    {"localidade": frase.split("\n")[1]},
                                    {"endereco": frase.split("\n")[2].split("end")[1]},
                                    {
                                        "telefone": frase.split("\n")[2].split("end")[
                                                        0
                                                    ][3:]
                                    },
                                ]
                            }
                        elif len(frase) > 3:
                            try:
                                self.dicionario = {
                                    frase.split("\n")[0]: [
                                        {"localidade": frase.split("\n")[1]},
                                        {
                                            "endereco": frase.split("\n")[2].split(
                                                "end"
                                            )[1]
                                        },
                                        {
                                            "telefone": frase.split("\n")[2].split(
                                                "end"
                                            )[0][3:]
                                        },
                                        {"localidade": frase.split("\n")[3]},
                                        {
                                            "endereco": frase.split("\n")[4].split(
                                                "end"
                                            )[1]
                                        },
                                        {
                                            "telefone": frase.split("\n")[4].split(
                                                "end"
                                            )[0][3:]
                                        },
                                    ]
                                }
                            except Exception as err:
                                print(err)
                                self.dicionario = {
                                    frase.split("\n")[0]: [
                                        {"localidade": frase.split("\n")[1]},
                                        {
                                            "endereco": frase.split("\n")[2].split(
                                                "end"
                                            )[1]
                                        },
                                        {
                                            "telefone": frase.split("\n")[2].split(
                                                "end"
                                            )[0][3:]
                                        },
                                        # {'localidade': frase.split('\n')[3]},
                                        # {'endereco': frase.split('\n')[4]},
                                        # {'telefone': frase.split('\n')[4]}
                                    ]
                                }
                        # pprint(dicionario)
                    self.dicionario = {}
                    frase = ""
                else:
                    if "location_on" in file:
                        loc = re.sub(r" , ", " ", file[12:])
                        loc = re.sub(r" {2}", " ", loc)
                        frase += loc + "\n"
                    elif "call" in file:
                        frase += "tel:" + file[5:] + " end:"
                    elif "ESPECIALIDADE" in file:
                        frase += file[15:] + "\n"
                    else:
                        frase += "localidade: " + file + "\n"


if __name__ == "__main__":
    luxu = Luxu()
    luxu.loadArchive()

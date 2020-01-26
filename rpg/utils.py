import os
from rpg import Rpg


class Utils:
    def __init__(self):
        ...

    def validInput(self, tipo, nome, valor, limite, msg):
        if tipo == 'str':
            valor = valor.strip().upper()
            while not valor.isalpha() or valor not in limite or len(valor) == 0:
                print('OPÇÃO INVÁLIDA !!!')
                valor = str(input(msg))
                valor = valor.strip().upper()
        elif tipo == 'int':
            while True:
                valor = valor.strip()
                while not valor.isnumeric() or valor.isalpha() or len(valor) == 0 or int(valor) not in limite:
                    if not valor.isnumeric() or valor.isalpha() or len(valor) == 0:
                        print(' OPÇÃO INVÁLIDA !!!\n')
                        valor = str(input(msg))
                        valor = valor.strip()
                    elif nome == 'inimigo':
                        print(' INIMIGO NÃO SE ENCONTRA NA LISTA !!!\n')
                        valor = str(input(msg))
                        valor = valor.strip()
                    elif nome == 'inimigo_s':
                        print(' INIMIGO NÃO SE ENCONTRA NA LISTA !!!\n')
                        valor = str(input(msg))
                        valor = valor.strip()
                    else:
                        print(' OPÇÃO INVÁLIDA !!!\n')
                        valor = str(input(msg))
                        valor = valor.strip()

                break

        return valor


    def msg(self, opc, rpg=None):
        if opc == 'esc_inicial' :
            return f"\nPressione (C)omeçar ou (I)nstruções:"
        elif opc == 'title':
            return f"{'-'*25} A LENDA DO BESERKER {'-'*24}"
        elif opc == 'escolha_nro_inimigo':
            return f"Escolha o número de inimigos: "
        elif opc == 'selecione_inimigo':
            return f"Selecione um inimigo da lista acima:"
        elif opc == 'invalida':
            return f"Opção Inválida. Redigite!"
        elif opc == 'lista_inimigos':
            print(f"\n-----.::| LISTA DE INIMIGOS |::-----\n")
        elif opc == 'status_heroi':
            print('\n\n=====' + ' STATUS DO HERÓI ' + '=====')
        elif opc == 'nro_inimigos':
            print(f'\nNro de inimigos = {len(rpg.getListaInimigos())}')
        elif opc == 'player_vida':
            print(f'\nVIDA = {rpg.getPlayerVida()}')
        elif opc == 'sp':
            print(f'SP = {rpg.getPlayerSP()}\n')
        elif opc == 'turno_heroi':
            print(f'\n-----.::| TURNO DO HERÓI |::.-----\n')
        elif opc == 'super_cura':
            print(f'-----.::| SUPER-CURA ativada |::.-----\n')
        elif opc == 'ataque_skills':
            return f"Selecione ATACAR (1), SKIlls (2): \n"


    def getValidaNumber(self, number):
        return number.isnumeric()


    def instrucao(self):
        os.system('clear')
        titulo_regra = '.::..::| INSTRUÇÕES/REGRAS |::..::.'
        print('\n{:^40}'.format(titulo_regra))
        # print(f'\n{:^40}{titulo_regra}')
        text_instruction = """
- Escolha o número de inimigos
- Escolha a ação desejada
- ATACAR:
    O Herói SEMPRE acerta o inimigo, infligindo 10-15 de dano ao alvo selecionado
- CURAR:
    Recupera 20-50 pontos de vida do Herói, custo de 10 SP
MODO BESERKER:
    - Ao ter seu limite levado ao extremo, o Herói rompe as barreiras de suas limitações mundanas, elevando-se ao status BESERKER
- SUPER CURA: Recupera 250 pontos de vida do Herói, custo de 50 SP
- ATAQUE INIMIGO: O inimigo terá 25% de chance de errar o ataque
    (50% após o MODO BESERKER), caso contrário, infligirá 1-3 pontos de dano ao Herói
REGRA_Geral:
    - A cada rodada você ganhará 3 de SP, a NÃO ser quando o "MODO BESERKER" for DESATIVADO
REGRAS_Beserker:
    - O MODO BESERKER será ativado 1 VEZ por jogo
    - Contêm DUAS RODADAS
    - Em cada rodada, o heroi irá realizar ATAQUES SUCESSIVOS e ALEATÓRIOS
    - O jogador NÃO poderá escolher o inimigo a ser atacado neste modo.
    - O nro de ataques POR RODADA, será igual à quantidade de inimigo no campo de batalha
    - Cada ataque, gera 20-40 pontos de dano ao inimigo
    - O inimigo NÃO consegue atacar o Herói no MODO BESERKER
    - Ao final das duas rodadas, o MODO BESERKER será DESATIVADO
    - O Herói irá drenar, em forma de pontos de vida, 10% do DANO TOTAL aplicado por ele nas duas rodadas
    - Ao ser DESATIVADO, o Herói terá ZERO de SP
REGRA_Super_Cura:
    - Só existe UMA "SUPER CURA" por JOGO
    - Requisitos para ATIVAR a "SUPER CURA":
        - Nro de inimigos > 10
        - Nro de turnos na partida for múltiplo de 10"""
        print(text_instruction)
        input('\n\n.::| PRESSIONE ENTER PARA COMEÇAR |::.\n')

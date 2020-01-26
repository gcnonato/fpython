from utils import Utils
from rpg import Rpg
from random import randint, choice
from time import sleep
import sys, os

if __name__ =='__main__':
    utils = Utils()
    rpg = Rpg()
    # titulo = f"{'-'*25} A LENDA DO BESERKER {'-'*24}"
    # tam_titulo = len(titulo)
    traco = "="*70
    print(f"\n{traco}\n{utils.msg('title')}\n{traco}")
    # input_instrucoes = f'\nPressione (C)omeçar ou (I)nstruções:'
    iniciar = str(input(utils.msg('esc_inicial')))
    if iniciar.upper() == 'C':
        iniciar = utils.validInput(
            'str',
            'iniciar',
            iniciar,
            'CI',
            utils.msg('esc_inicial')
        )
    elif iniciar.upper() == 'I':
        utils.instrucao()
        os.system('clear')
    else:
        print('Opção Inválida! Saindo...')
        sleep(2)
        os.system('clear')
        sys.exit(0)
    jogando = True
    os.system('clear')
    nro_inimigo = input(utils.msg('escolha_nro_inimigo'))
    while not utils.getValidaNumber(nro_inimigo):
        print(f"\n{utils.msg('invalida')}\n")
        nro_inimigo = input(utils.msg('nro_inimigo'))
    rpg.setNroInimigos(int(nro_inimigo))
    for inimigo in range(rpg.getNroInimigos()):
        rpg.setListaInimigos(inimigo)
    # print(rpg.getNroInimigos())
    while True:
        if rpg.getNRodadaB == 2:
            rpg.setNRodadaB(1)
        utils.msg('lista_inimigos')
        for i in rpg.getListaInimigos():
            print(f' - inimigo ({i[0]}) -- vida = {i[1]}')
            if rpg.getNroInimigos() <= 20:
                sleep(0.25)
            elif rpg.getNroInimigos() <= 50:
                sleep(0.1)
        utils.msg('nro_inimigos', rpg)
        utils.msg('status_heroi')
        # rpg.setNRodadaB(3)
        # print(rpg.getNRodada() % 10 == 0)
        # print(rpg.getPlayerSP())
        if rpg.getNRodadaB == 3:
            if rpg.getNRodada() % 10 == 0:
                if rpg.getPlayerSP() < 25:
                    rpg.setPlayerSP(72)
                    print('\n HERÓI GANHOU 75 SP !!!')
                    sleep(2)
        # print('\n  VIDA = {}'.format(player_vida))
        # print('  SP = {}\n'.format(player_sp))
        # print('-----' + '.::| TURNO DO HERÓI |::.' + '-----' + '\n')
        utils.msg('player_vida', rpg)
        utils.msg('player_sp', rpg)
        utils.msg('turno_heroi', rpg)
        sleep(1.5)
        while rpg.getErroSkill() and rpg.getNRodada() % 10 == 0:
            if rpg.getNRodada() > 0:
                if rpg.getNroInimigos() > 10:
                    utils.msg('super_cura')
            opcao = str(input(utils.msg('ataque_skills')))
            # print(utils.getValidaNumber(opcao))
            if utils.getValidaNumber(opcao):
                if int(opcao) == 1:
                    # rpg.setErroSkill(False)
                    lista_limite = []
                    for name_inimigo in rpg.getListaInimigos():
                        print(name_inimigo[0])
                        # lista_limite.append(inimigo[0])
                    inimigo = input(utils.msg('selecione_inimigo'))
                    # inimigo = validinput('int', 'inimigo', inimigo, lista_limite, ' Selecione um inimigo da lista acima: \n')
                    escolhido = []
                    # for i in rpg.getListaInimigos():
                    #     if i[0] == int(inimigo):
                    #         escolhido = i
                    #         break
                    escolhido = rpg.getListaInimigos()[int(inimigo)-1]
                    dano_player = randint(15, 20)
                    pv_inimigo_antes = escolhido[1]
                    escolhido[1] -= dano_player
                    print(f'Atacando o inimigo {escolhido[0]}')
                    sleep(1.5)
                    print(f"\n Você causou {dano_player} de dano ao inimigo {escolhido[0]} ! ({pv_inimigo_antes} - {dano_player} = {escolhido[1]})")
                    sleep(1.5)
                    if escolhido[1] <= 0:
                        str_inimigo = str(escolhido[0])
                        tam_str_inimigo = len(str_inimigo)
                        msg_morte = f'Voce matou o inimigo {inimigo}!'
                        tam_msg_morte = len(msg_morte)
                        print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1))
                        print(msg_morte)
                        print(' ' + 'x' * (tam_str_inimigo + tam_msg_morte - 1) + '\n')
                        sleep(1.25)
                        # lista_inimigo.remove(escolhido)
                        rpg.getDeleteListaInimigos(escolhido)
                    # print(rpg.getNroInimigos())
                print(rpg.getListaInimigos()[1])

            if len(rpg.getListaInimigos()) <= 0:
                rpg.setErroSkill(False)
            # print(rpg.getErroSkill())
            # os.system('clear')

            # break
        break

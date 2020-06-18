import PySimpleGUI as sg
import math

sg.popup_ok('Atenção!',
            'Não utilizar pontos e vírgulas nos valores recebidos, não deixar valores em branco, pagamento não recebido colocar 0 (zero) !')

sg.theme('DarkAmber')  # Add a touch of color

# All the stuff inside your window.
layout = ([sg.Text('Total recebido em Dinheiro:'), sg.Input(size=(7, 1), key=('valor0'))],
          [sg.Text('Total recebido no Débito:'), sg.Input(size=(7, 1), key=('valor'))],
          [sg.Text('Total recebido no Crédito a vista:'), sg.Input(size=(7, 1), key=('valor1'))],
          [sg.Text('Total recebido Crédito até 6x:'), sg.Input(size=(7, 1), key=('valor2'))],
          [sg.Text('Total recebido Crédito de 7x até 12x:'), sg.Input(size=(7, 1), key=('valor3'))],
          [sg.Text('VALORES CARTÃO ELO', background_color='Black', justification='center4')],
          [sg.Text('Total recebido Débito Elo:'), sg.Input(size=(7, 1), key=('valor4'))],
          [sg.Text('Total recebido Crédito a vista Elo:'), sg.Input(size=(7, 1), key=('valor5'))],
          [sg.Text('Total recebido Crédito Elo até 6x:'), sg.Input(size=(7, 1), key=('valor6'))],
          [sg.Text('Total recebido Crédito Elo de 7x até 12x:'), sg.Input(size=(7, 1), key=('valor7'))],
          [sg.Output(size=(80, 20))],
          [sg.Button('Calcular'), sg.Button('Cancel')])

# Create the Window
window = sg.Window('Calculador porcentagem do Dentista', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break


    # valores recebidos e métodos de pagamentos
    valor0 = values['valor0']
    valor = values['valor']
    valor1 = values['valor1']
    valor2 = values['valor2']
    valor3 = values['valor3']
    valor4 = values['valor4']
    valor5 = values['valor5']
    valor6 = values['valor6']
    valor7 = values['valor7']


    # Aqui é feito o cálculo da porcentagem da maquininha a ser descontada do valor total
    porcent = valor * 0.0178
    porcent1 = valor1 * 0.0294
    porcent2 = valor2 * 0.0350
    porcent3 = valor3 * 0.0370
    porcent4 = valor4 * 0.0304
    porcent5 = valor5 * 0.0409
    porcent6 = valor6 * 0.0462
    porcent7 = valor7 * 0.0509

    # Aqui é feito o desconto da taxa da maquininha do valor total
    desco = valor - porcent
    desco1 = valor1 - porcent1
    desco2 = valor2 - porcent2
    desco3 = valor3 - porcent3
    desco4 = valor4 - porcent4
    desco5 = valor5 - porcent5
    desco6 = valor6 - porcent6
    desco7 = valor7 - porcent7

    # Aqui é feito os 35% a ser repassado para o dentista do valor com a taxa da maquininha descontada
    liq0 = valor0 * 0.35
    liq = desco * 0.35
    liq1 = desco1 * 0.35
    liq2 = desco2 * 0.35
    liq3 = desco3 * 0.35
    liq4 = desco4 * 0.35
    liq5 = desco5 * 0.35
    liq6 = desco6 * 0.35
    liq7 = desco7 * 0.35

    # Extrair dados da tela
    print('Você digitou em dinheiro', values['valor0'], values['valor'], values['valor1'], values['valor2'],
          values['valor3'], values['valor4'], values['valor5'], values['valor6'], values['valor7'])
    # Aqui imprimi na tela o valor total dos 35% a ser repassado ao dentista de todos os pagamentos
    print('Valor liquido a receber é', liq0 + liq + liq1 + liq2 + liq3 + liq4 + liq5 + liq6 + liq7)
    print()
window.close()

"""
while True:
    print('Calculadora % da maqueninha a repassar para Dentista')
    print()
    print(
        'ATENÇÃO! NÃO UTILIZAR PONTOS NEM VÍRGULAS NOS VALORES, VALORES NÃO RECEBIDOS PREENCHER COM 0, NÃO DEIXAR VALOR EM BRANCO')
    print()

    # valores recebidos e métodos de pagamentos
    valor0 = float(input('Valor Total Recebido em Dinheiro:'))
    valor = float(input('Valor Total recebido Debito:'))
    valor1 = float(input('Crédito a vista:'))
    valor2 = float(input('Crédito até 6x:'))
    valor3 = float(input('Crédito de 7x até 12x:'))
    print()
    print('calculadora % Cartão Elo')
    valor4 = float(input('Débito Elo:'))
    valor5 = float(input('Crédito a vista Elo:'))
    valor6 = float(input('Crédito Elo até 6x:'))
    valor7 = float(input('Crédito Elo de 7x até 12x:'))

    # Aqui é feito o cálculo da porcentagem da maquininha a ser descontada do valor total
    porcent = valor * 0.0178
    porcent1 = valor1 * 0.0294
    porcent2 = valor2 * 0.0350
    porcent3 = valor3 * 0.0370
    porcent4 = valor4 * 0.0304
    porcent5 = valor5 * 0.0409
    porcent6 = valor6 * 0.0462
    porcent7 = valor7 * 0.0509

    # Aqui é feito o desconto da taxa da maquininha do valor total
    desco = valor - porcent
    desco1 = valor1 - porcent1
    desco2 = valor2 - porcent2
    desco3 = valor3 - porcent3
    desco4 = valor4 - porcent4
    desco5 = valor5 - porcent5
    desco6 = valor6 - porcent6
    desco7 = valor7 - porcent7

    # Aqui é feito os 35% a ser repassado para o dentista do valor com a taxa da maquininha descontada
    liq0 = valor0 * 0.35
    liq = desco * 0.35
    liq1 = desco1 * 0.35
    liq2 = desco2 * 0.35
    liq3 = desco3 * 0.35
    liq4 = desco4 * 0.35
    liq5 = desco5 * 0.35
    liq6 = desco6 * 0.35
    liq7 = desco7 * 0.35

    # Aqui imprimi na tela o valor total dos 35% a ser repassado ao dentista de todos os pagamentos
    print('Valor liquido a receber é', liq0 + liq + liq1 + liq2 + liq3 + liq4 + liq5 + liq6 + liq7)
    print()
    print()
    print()

"""
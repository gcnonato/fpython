# -*- coding: utf-8 -*-
import pymysql.cursors
import pymysql
import sys
import json
import datetime
import environ

# Carrega as configurações de arquivo externo
environ.Path(__file__)
env = environ.Env()
env.read_env('.envs/.env')


def conexao_local_remoto(conexao):
    if conexao == 'fabrizio':
        connection = pymysql.connect(host=env('HOST_FABRIZIO'),
                                     user=env('USER_FABRIZIO'),
                                     password=env('PASSWORD2_FABRIZIO'),
                                     db=env('DB_FABRIZIO'),
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    elif conexao == 'luciano':
        connection = pymysql.connect(host=env('HOST_LUCIANO'),
                                     user=env('USER_LUCIANO'),
                                     password=env('PASSWORD_LUCIANO'),
                                     db=env('DB_LUCIANO'),
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    else:
        connection = pymysql.connect(host=env('HOST_LOCAL'),
                                     user=env('USER_LOCAL_MYSQL'),
                                     password=env('PASSWORD_LOCAL_MYSQL'),
                                     db=env('DB_LOCAL_MYSQL'),
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    return connection

def conexao(connection, nome_conexao, tbl=None):
    if nome_conexao == 'local':
        db = env('DB_LOCAL_MYSQL')
    elif nome_conexao == 'luciano':
        db = env('DB_LUCIANO')
    else:
        db = env('DB_FABRIZIO')
    try:
        with connection.cursor() as cursor:
            # Read a single record
            # sql = u"SELECT {} FROM {}".format(campos(),tabela())
            if tbl:
                sql = f"SELECT * FROM {tabela(tbl)}"
            else:
                sql = f"SELECT * FROM information_schema.tables WHERE table_schema = '{db}'"
            # sql = "SELECT * FROM `profissionais`" # WHERE `email`=%s"
            # sql = "SELECT * FROM `agendas` WHERE `profissional_ID`=%s"
            # cursor.execute(sql, (216))
            cursor.execute(sql)
            listar_dados_banco = cursor.fetchall()
            return listar_dados_banco
    finally:
        connection.close()

def nomeTabelas(connection, nome_conexao):
    nome = conexao(connection, nome_conexao)
    nome_tabelas = []
    for n in nome:
        nome_tabelas.append(n['TABLE_NAME'])
    salvar = json.dumps(nome_tabelas, indent=4, ensure_ascii=False)
    arquivo = 'TabelasBanco.json'
    with open(arquivo, "w", encoding='utf8') as _json:
        _json.write(salvar)
    # try:
    #     file = open(arquivo, "w", encoding='utf8')
    #     file.write(salvar)
    #     file.close()
    # except Exception as erro:
    #     print("Ocorreu um erro ao carregar o arquivo.")
    #     print(f"O erro é: {erro}")

def tabela(nome):
    print(f"função: Tabela.: {nome}")
    return nome

def cabecalho(listar_dados_banco):
    cabecalho = []
    corpo = []
    for dados in listar_dados_banco:
        for key, value in dados.items():
            corpo.append(f'{key} : {value}')
    return corpo

def consultar(connection,nome_conexao,tbl):
    arquivo = f'Tabela:{tbl.upper()}-{nome_conexao.upper()}.json'
    listar_dados_banco = conexao(connection, tbl)
    corpo = cabecalho(listar_dados_banco)
    campos = []
    # file = open(arquivo, "w", encoding='utf8')
    for dados in listar_dados_banco:
        # print(f'{dados}\n{"*"*50}')
        for k,v in dados.items():
            if not isinstance(v, datetime.datetime):
                print(f'{k} => {v}')
            else:
                print(f'{k} => {v}')
        # print(f'{json.dumps(dados)}\n{"*" * 50}')
        # if dados.startswith("ID"):
        #     print()
            # file.write(u'{"-"*20}\n')
        # file.write(json.dumps(
        #     dados, indent=4, sort_keys=True, ensure_ascii=False, default=str)+'\n')
    # file.close()
    return

if __name__ == "__main__":
    try:
        nome_conexao = sys.argv[1]
        connection = conexao_local_remoto(sys.argv[1])
        # consultar(connection, nome_conexao, sys.argv[2])
        nomeTabelas(connection, nome_conexao)
    except Exception as err:
        # os.system("cls")
        line = '*'*80
        print(f'{line}\n'
              f'Não esqueça de colocar dessa forma: mysql.py <LOCAL, LUCIANO ou FABRIZIO> <TABELA>'
              f'\n{line}')
        print(f'Error.: {err}')
        sys.exit(0)
        # print(nomeTabelas(connection))
# -*- coding: utf-8 -*-
import datetime
import sys

import environ
import pymysql
import pymysql.cursors
from sqlalchemy import create_engine

# Carrega as configurações de arquivo externo
environ.Path(__file__)
env = environ.Env()
env.read_env(".envs/.env")


def conexao_local_remoto(conexao):
    if conexao == "fabrizio":
        connection = pymysql.connect(
            host=env("HOST_FABRIZIO"),
            user=env("USER_FABRIZIO"),
            password=env("PASSWORD2_FABRIZIO"),
            db=env("DB_FABRIZIO"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
    elif conexao == "luciano":
        connection = pymysql.connect(
            host=env("HOST_LUCIANO"),
            user=env("USER_LUCIANO"),
            password=env("PASSWORD_LUCIANO"),
            db=env("DB_LUCIANO"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
    else:
        connection = pymysql.connect(
            host=env("HOST_LOCAL"),
            user=env("USER_LOCAL_MYSQL"),
            password=env("PASSWORD_LOCAL_MYSQL"),
            db=env("DB_LOCAL_MYSQL"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
    return connection


def conexao(connection, nome_conexao, tbl=None):
    if nome_conexao == "local":
        db = env("DB_LOCAL_MYSQL")
    elif nome_conexao == "luciano":
        db = env("DB_LUCIANO")
    else:
        db = env("DB_FABRIZIO")
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
    print(nome)
    for n in nome:
        print(n["TABLE_NAME"])


def tabela(nome):
    print(f"função: Tabela.: {nome}")
    return nome


def cabecalho(listar_dados_banco):
    corpo = []
    for dados in listar_dados_banco:
        for key, value in dados.items():
            corpo.append(f"{key} : {value}")
    return corpo


def consultar(connection, nome_conexao, tbl):
    # arquivo = f"Tabela:{tbl.upper()}-{nome_conexao.upper()}.json"
    listar_dados_banco = conexao(connection, tbl)
    # corpo = cabecalho(listar_dados_banco)
    # file = open(arquivo, "w", encoding='utf8')
    for dados in listar_dados_banco:
        for k, v in dados.items():
            if not isinstance(v, datetime.datetime):
                print(f"{k} => {v}")
            else:
                print(f"{k} => {v}")
    return


def inserir(table, data):
    # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    connect = f"mysql+pymysql://{env('USER_LOCAL_MYSQL')}:{env('PASSWORD_LOCAL_MYSQL')}" \
              f"@localhost/{env('DB_LOCAL_MYSQL')}"
    engine = create_engine(connect)  # connect to server
    sql = "SELECT * FROM django_migrations"
    try:
        resultado = engine.execute(sql)
        print(resultado)
    except pymysql.err.ProgrammingError as e:
        print(e)


if __name__ == "__main__":
    try:
        nome_conexao = sys.argv[1]
        connection = conexao_local_remoto(sys.argv[1])
        # consultar(connection, nome_conexao, sys.argv[2])
        # nomeTabelas(connection, nome_conexao)
        inserir("d", {})
    except Exception as err:
        # os.system("cls")
        line = "*" * 80
        print(
            f"{line}\n"
            f"Não esqueça de colocar dessa forma: mysql.py <local, LUCIANO ou FABRIZIO> <TABELA>"
            f"\n{line}"
        )
        print(f"Error.: {err}")
        sys.exit(0)

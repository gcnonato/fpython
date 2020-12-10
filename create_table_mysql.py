# -*- coding: utf-8 -*-
import datetime
import sys

import pymysql
import pymysql.cursors
from alembic import op
from decouple import config
from sqlalchemy import Column, Integer, String, Boolean, VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import table

Base = declarative_base()


def conexao_local():
    return pymysql.connect(
        host=config("local.host"),
        user=config("local.user"),
        password=config("local.password"),
        db=config("local.db"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def conexao(connection, tbl=None):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            # sql = u"SELECT {} FROM {}".format(campos(),tabela())
            if tbl:
                sql = f"SELECT * FROM {tabela(tbl)}"
            else:
                db = "outpromo_homologacao"
                sql = f"SELECT * FROM information_schema.tables WHERE table_schema = '{db}'"
            # sql = "SELECT * FROM `profissionais`" # WHERE `email`=%s"
            # sql = "SELECT * FROM `agendas` WHERE `profissional_ID`=%s"
            # cursor.execute(sql, (216))
            cursor.execute(sql)
            listar_dados_banco = cursor.fetchall()
            return listar_dados_banco
    except Exception as err:
        print(err)
        return None
    finally:
        connection.close()


def nomeTabelas(connection, nome_conexao):
    nome = conexao(connection, nome_conexao)
    for n in nome:
        # table = nome_tabelas.append(n['TABLE_NAME'])
        print(n["TABLE_NAME"])
    # salvar = json.dumps(nome_tabelas, indent=4, ensure_ascii=False)
    # arquivo = 'TabelasBanco.json'
    # with open(arquivo, "w", encoding='utf8') as _json:
    #     _json.write(salvar)
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
    corpo = []
    for dados in listar_dados_banco:
        for key, value in dados.items():
            corpo.append(f"{key} : {value}")
    return corpo


def consultar(connection, tbl=None):
    if tbl:
        arquivo = f"Tabela:{tbl.upper()}"
        print(arquivo)
        listar_dados_banco = conexao(connection, tbl)
    else:
        listar_dados_banco = conexao(connection)
    if listar_dados_banco:
        for dados in listar_dados_banco:
            # print(f'{dados}\n{"*"*50}')
            for k, v in dados.items():
                if not isinstance(v, datetime.datetime):
                    print(f"{k} => {v}")
                else:
                    print(f"{k} => {v}")
        return
    return None


def inserir(table, data):
    # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    connect = (
        f"mysql+pymysql://"
        f"{config('local.host')}:"
        f"{config('local.password')}@localhost/"
        f"{config('local.db')}"
    )
    # engine.execute("USE outpromo_homologacao")
    engine = create_engine(connect)  # connect to server
    sql = "SELECT * FROM django_migrations"
    try:
        engine.execute(sql)
    except pymysql.err.ProgrammingError as e:
        print(e)


def create_table():
    connect = (
        f"mysql+pymysql://"
        f"{config('local.user')}:"
        f"{config('local.password')}@localhost/"
        f"{config('local.db')}"
    )
    try:
        engine = create_engine(connect, echo=True)
        Base.metadata.create_all(engine)
    except pymysql.err.ProgrammingError as e:
        print(e)


class Empresa(Base):
    __tablename__ = "casting_empresa"

    id = Column(Integer, primary_key=True)
    cnpj = Column(String(14))
    razao_social = Column(String(60))
    cidade = Column(String(20))
    uf = Column(String(2))
    regiao = Column(String(2))
    coligado = Column(Boolean)

    def __repr__(self):
        return f"Empresa {self.razao_social}"


class Rede(Base):
    __tablename__ = "casting_rede"

    id = Column(Integer, primary_key=True)
    rede = Column(String(40))

    def __repr__(self):
        return f"{self.rede}"


class Loja(Base):
    __tablename__ = "casting_loja"

    id = Column(Integer, primary_key=True)
    rede = String(200)  # relationship('Rede')
    razao_social = String(200)
    nome_loja = String(200)
    endereco = String(150)
    complemento = String(60)
    bairro = String(100)
    cep = String(8)
    cidade = String(100)
    uf = String(2)
    pais = String(40)
    ddd = String(5)
    fone = String(25)
    email = String(100)
    site = String(100)
    empresa = String(200)  # relationship('Empresa')
    latlong = String(30)
    inativa = Boolean()

    def __repr__(self):
        return f"{self.razao_social}"


def upgrade():
    op.add_column("casting_loja", Column("razao_social", String(200)))
    loja = table(
        "casting_loja",
        Column("razao_social", VARCHAR(length=200)),
        # Column('stooge', Boolean())
        # Other columns not needed for the data migration
    )
    op.execute(
        loja.update()
        # .where(old_timers.c.name.in_(StoogeNames))
        # .values({'stooge': True})
    )


def downgrade():
    ...


if __name__ == "__main__":
    try:
        upgrade()
        # empresa = Empresa()
        # print(empresa)
        # empresa.create_table()
        # rede = Rede()
        # loja = Loja()
        # create_table()
        # connection = conexao_local()
        # if consultar(connection):
        #     print(consultar(connection))
        # else:
        #     print('Banco vazio!!')
    except Exception as err:
        print(err)
        sys.exit(0)

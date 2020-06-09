import os
import psycopg2
import subprocess
from subprocess import Popen
from pprint import pprint

import pandas as pd

from decouple import config


class Banco:
    def __init__(self, host, db, user, password):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.conn_string = f"host={self.host} port=5432 \
            dbname={self.db} user={self.user} \
            password={self.password}"
        self.con = psycopg2.connect(self.conn_string)

    def load_data(self, schema, table):
        sql_command = f"SELECT * FROM {str(table)}"
        print(sql_command)
        conn = self.con

        # Load the data
        data = pd.read_sql(sql_command, conn)

        print(data.tail())
        return data

        def connect(self):
            """ Connect to the PostgreSQL database server """
            conn = self.con
            try:
                print("Connecting to the PostgreSQL database...")
                cur = conn.cursor()
                print("PostgreSQL database version:")
                cur.execute("SELECT version()")
                db_version = cur.fetchone()
                print(db_version)
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print("Database connection closed.")

    def get_vendors(self, table):
        """ query data from the vendors table """
        conn = self.con
        try:
            cur = conn.cursor()
            # cur.execute("""
            #     SELECT g.id, g.name, c.name FROM website_segmento AS  c, website_gasto AS  g
            #     WHERE g.segmento_id = c.id  ORDER BY g.id DESC
            #     """
            # )
            cur.execute(f"SELECT * FROM {table} AS  c")
            # rows = cur.fetchone()
            rows = cur.fetchall()

            for row in rows:
                print(row)
            print("The number of parts: ", len(rows))
            # print("The number of parts: ", cur.rowcount)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def lastIDinserted(self, table):
        conn = self.con
        sql = f"SELECT MAX(id) FROM {table}"
        # sql = "SELECT currval(pg_get_serial_sequence('website_comercio','id'))"
        # sql = "select nextval('website_gasto_id_seq')"
        # nextval('website_gasto_id_seq'::regclass)
        cur = conn.cursor()
        try:
            print(f"SQL.: {sql}")
            id = cur.execute(sql)
            print(f"ID..: {id}")
        except psycopg2.DatabaseError as error:
            print(f"ERROR..: {error}")
        finally:
            cur.close()
            conn.close()

    def insert_gasto(self, fields):
        id = fields[4]
        name = fields[0]
        slug = fields[1]
        valor = fields[2]
        comercio_id = fields[3]
        """ insert a new vendor into the website_gasto table """
        sql = """INSERT INTO website_gasto(name,slug,valor,comercio_id)
                 VALUES(%s,%s,%s,%s)"""
        conn = self.con
        vendor_id = None
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (name, slug, valor, comercio_id,))
            # get the generated id back
            vendor_id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return vendor_id

    def backup(self, schema, user, server):
        # , server, user, database, password
        homepath = os.path.expanduser(os.getenv("USERPROFILE"))
        desktoppath = "Desktop"
        os.chdir('/'.join((homepath, desktoppath)))
        os.chdir('C:/Program Files/PostgreSQL/10/bin')
        filename = "backup.sql"
        dado = f"pg_dump  -f {filename} -h {server} -U {user} {schema}"
        popen = subprocess.Popen(dado, stdout=subprocess.PIPE, universal_newlines=True)
        popen.stdout.close()
        popen.wait()

    def getTables(self):
        conn = self.con
        cursor = conn.cursor()
        cursor.execute(
            "select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';"
        )
        tables = []
        for table in cursor.fetchall():
            tables.append(table[0])
        return tables

    def getReadTable(self, table):
        conn = self.con
        try:
            cur = conn.cursor()
            # cur.execute("""
            #     SELECT g.id, g.name, c.name FROM website_segmento AS  c, website_gasto AS  g
            #     WHERE g.segmento_id = c.id  ORDER BY g.id DESC
            #     """
            # )
            cur.execute(f"SELECT * FROM {table} AS  c")
            # rows = cur.fetchone()
            for row in cur.fetchall():
                pprint(row)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()

    def getReadColumnTable(self, table):
        conn = self.con
        try:
            cur = conn.cursor()
            # cur.execute("""
            #     SELECT g.id, g.name, c.name FROM website_segmento AS  c, website_gasto AS  g
            #     WHERE g.segmento_id = c.id  ORDER BY g.id DESC
            #     """
            # )
            cur.execute(f"SELECT * FROM {table} AS  c")
            # rows = cur.fetchone()
            for row in cur.fetchall():
                pprint(row)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()

    def version(self):
        conn = self.con
        cursor = conn.cursor()
        cursor.execute(
            "SELECT version();"
        )
        row = cursor.fetchone()
        print(row)
        cursor.close()

    def dump_schema(self, host, dbname, user, password, **kwargs):
        command = f'pg_dump --host="{host}" ' \
                  f'--dbname={"deo6ap8jo3oe95"} ' \
                  f'--username={user} ' \
                  f'--no-password ' \
                  f'--format=c ' \
                  f'--file=e:\schema.dmp '
        os.chdir('C:/Program Files/PostgreSQL/10/bin')
        try:
            proc = Popen(command, shell=True, env={
                'PGPASSWORD': password
            })
            proc.wait()
        except Exception as err:
            print(err)


if __name__ == "__main__":
    table = "django_migrations"
    host = config('HEROKU_POSTRGRES_HOST')
    schema = 'deo6ap8jo3oe95'
    # config('HEROKU_POSTRGRES_DB')
    user = config('HEROKU_POSTRGRES_USER')
    password = config('HEROKU_POSTRGRES_PASSWORD')
    banco = Banco(host, schema, user, password)
    # banco.version()
    banco.backup(host, user, schema)
    # banco.dump_schema(host, banco, user, password)
    # host, dbname, user, password,
    # load_data(schema,table)
    # get_vendors(table)
    # list_tables = banco.getTables()
    # pprint(list_tables)
    # getReadTable(list_tables[0])
    # banco.getReadColumnTable(table)
    # pprint(banco.getTables())
    # connect()
    # banco.lastIDinserted(list_tables[0])

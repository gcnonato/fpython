# -*- coding: utf-8 -*-
import os
import subprocess
from pprint import pprint

import environ
import pandas as pd
import psycopg2

ROOT_DIR = environ.Path(__file__)
env = environ.Env()
env.read_env()


class Banco:
    """docstring for ."""

    def __init__(self):
        conn_string_local = f"host={env.ENVIRON['PGHOST']} port=5432 \
            dbname={env.ENVIRON['PGDATABASE']} user={env.ENVIRON['PGUSER']} \
            password={env.ENVIRON['PGPASSWORD']}"
        # conn_string_aws = f"host={creds.RDS_HOSTNAME} port=5432 \
        #     dbname={creds.RDS_DB_NAME} user={creds.RDS_USERNAME} \
        #     password={creds.RDS_PASSWORD}"
        self.con = psycopg2.connect(conn_string_local)

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
        # id = fields[4]
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

    def backup(self, server, user, database, password):
        print(password)
        os.chdir("C:\\Users\\luxu\\Desktop")
        filename = "backup.sql"
        dado = f"pg_dump  -f {filename} -h {server} -U {user} {database}"
        # print(dado)
        popen = subprocess.Popen(dado, stdout=subprocess.PIPE, universal_newlines=True)
        popen.stdout.close()
        popen.wait()

    def getTables(self,):
        conn = self.con
        # conn = psycopg2.connect(conn_string)
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


if __name__ == "__main__":
    schema = "recrutamento"
    table = "django_migrations"
    banco = Banco()
    # load_data(schema,table)
    # get_vendors(table)
    list_tables = banco.getTables()
    # pprint(list_tables[0])
    # getReadTable(list_tables[0])
    # getReadColumnTable(list_tables[0])
    # connect()
    banco.lastIDinserted(list_tables[0])

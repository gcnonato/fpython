#!/usr/bin/env python3
import psycopg2
from sshtunnel import SSHTunnelForwarder
import time
from decouple import config


with SSHTunnelForwarder(
         (config('INTEGRATOR_POSTRGRES_HOST'), 22),
         ssh_password=config('INTEGRATOR_POSTRGRES_PASSWORD'),
         ssh_username=config('INTEGRATOR_POSTRGRES_USER'),
         remote_bind_address=('127.0.0.1', 5432)) as server:

    conn = psycopg2.connect(
        database=config('INTEGRATOR_POSTRGRES_DB'),
        port=config('server.local_bind_port'),
        user=config('INTEGRATOR_POSTRGRES_USER'),
        password=config('INTEGRATOR_POSTRGRES_PASSWOR')
    )
    # conn_string = f"host={host} port=5432 \
    #             dbname={db} user={user} \
    #             password={password}"
    # conn = psycopg2.connect(conn_string)
    curs = conn.cursor()
    # sql = "select * from tabelka"
    sql = "SELECT version();"
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)

#
# server = SSHTunnelForwarder(
#     INTEGRATOR_POSTRGRES_HOST,
#     ssh_username=INTEGRATOR_POSTRGRES_USER,
#     ssh_password=INTEGRATOR_POSTRGRES_PASSWORD,
#     remote_bind_address=('127.0.0.1', 8080)
# )
#
# server.start()
#
# print(server.local_bind_port)  # show assigned local port
# # work with `SECRET SERVICE` through `server.local_bind_port`.
#
# server.stop()
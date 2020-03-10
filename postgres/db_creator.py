import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import environ
from config import config
from pprint import pprint

env = environ.Env()
env.read_env('../.env')

# useful info for psycopg2:
# https://stackoverflow.com/questions/34484066/create-a-postgres-database-using-python


class MyDB(object):
    def __init__(self):
        self.params = config()

    def create_new_db(self, newdb):
        user, host, port = self.params['user'], self.params['host'], self.params['port']
        pw = self.params['password']
        url = 'postgresql://{user}:{pw}@{host}:{port}/{newdb}'
        # url = url.format(, , , , )
        self.engine = create_engine(url, client_encoding='utf8')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        # print(database_exists(engine.url))

def df2postgres(engine, df=None):
    con = engine.connect()
    # df.to_sql(name='records', con=con, if_exists='replace', index=True, chunksize=10)
    return con

if __name__ == '__main__':
    testdb = MyDB()
    testdb.create_new_db('testdb')
    engn = testdb.engine
    # df = pd.read_csv('100_recs.csv')
    # with open('100_recs.csv', encoding="utf8") as _file:
        # texto = _file.readlines()
        # print(texto)
    # df = pd.read_csv('100_recs.csv', encoding='cp1252', delimiter=';', quotechar='"')
    con = df2postgres(engine=engn)
    # con = df2postgres(engine=engn, df)
    dta = con.execute('SELECT * FROM records LIMIT 5;')
    for rows in dta.fetchall():
        # pprint(rows)
        for row in rows:
            try:
                for f in row.split(','):
                    print(f)
                    print(f'{"*"*30}')
            except:
                ...
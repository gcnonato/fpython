from pprint import pprint

import pymysql
import pymysql.cursors


class Connection:
  def __init__(self):
    ...

  def openConnection(self):
    return pymysql.connect(
      host='localhost',
      user='root',
      password='iu00q71o',
      db='financas',
      charset='utf8mb4',
      cursorclass=pymysql.cursors.DictCursor
    )

  def close(self):
    return self.openConnection().close()

  def list(self, table):
    sql = f'SELECT * FROM {table}'
    try:
      with self.openConnection().cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
      self.close()

  def listTables(self):
    sql = 'SELECT * FROM information_schema.tables'
    try:
      with self.openConnection().cursor() as cursor:
        tables = cursor.execute("show databases")
    finally:
      self.close()

    return tables


c = Connection()
# pprint(c.listTables())
# listCategory = c.list('categorias')
listContasPagar = c.list('contas_pagar')
pprint(listContasPagar)

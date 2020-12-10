# -*- coding: utf-8 -*-
import os
import sqlite3


class Dao:
    conn = None
    cursor = None

    def __init__(self):
        os.chdir("DataBase")
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()

    def getConn(self):
        return self.conn

    def getCursor(self):
        return self.cursor

    def listar(self):
        return self.conn.execute("SELECT MAX (id) from agend")

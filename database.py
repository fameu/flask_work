# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 23:12 10:08
# @Author  : FAMU
# @File    : database.py
# @Software: PyCharm


from define import *
from database_def import *
from flask import Flask
import sqlite3
app = Flask(__name__)



def _execute(sql):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def InitDB(dtype):
    sql = GetCreateTableSql(dtype)
    _execute(sql)


def InsertDB():
    print(123)

if __name__ == '__main__':
    InitDB(TABLE_STOCK_OUT)





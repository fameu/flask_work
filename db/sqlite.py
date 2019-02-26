# -*- coding: gbk -*-
# @Time    : 2019/2/20 10:43
# @Author  : famu
# @File    : sqlite.py
# @Software: PyCharm


# 实现SQLite的连接
import sqlite3

DB_NAME	= "db/db_sqlite3.db"


def New(sql):
	print(sql)
	con = sqlite3.connect(DB_NAME)
	c = con.cursor()
	c.execute(sql)
	c.close()
	con.commit()
	con.close()

def Save(sql):
	con = sqlite3.connect(DB_NAME)
	c = con.cursor()
	c.execute(sql)
	c.close()
	con.commit()
	con.close()

def Query(sql):
	con = sqlite3.connect(DB_NAME)
	c = con.cursor()
	c.execute(sql)
	data = c.fetchall()
	c.close()
	con.commit()
	con.close()
	return data


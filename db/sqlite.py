# -*- coding: gbk -*-
# @Time    : 2019/2/20 10:43
# @Author  : famu
# @File    : sqlite.py
# @Software: PyCharm


# 实现SQLite的连接
import sqlite3

DB_NAME	= "db_zqq.db"

if not globals().has_key("g_Connect"):
	g_Connect = sqlite3.connect(DB_NAME)

def New(sql):
	c = g_Connect.cursor()
	c.execute(sql)
	c.close()
	g_Connect.commit()

def Save(sql):
	c = g_Connect.cursor()
	c.execute(sql)
	c.close()
	g_Connect.commit()

def Query(sql):
	c = g_Connect.cursor()
	c.execute(sql)
	data = c.fetchall()
	c.close()
	g_Connect.commit()
	return data


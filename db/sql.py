# -*- coding: gbk -*-
# @Time    : 2019/2/18 16:52
# @Author  : famu
# @File    : sql.py
# @Software: PyCharm

# 根据数据库类型不同，这里的sql语句也不一样
# 所有的sql的操作都通过这里来中转
# 并且这里只做保存和查询
# 更新也当作一次保存
# 删除则使用修改一个字段来实现
# 先实现SQLite的语句，相对幻境容易搭建

from define import *
import sqlite


SQL_TYPE	= SSQL_SQLITE

# 这里需要有个防注入功能，因为是一个直接的sql语句，需要避免sql注入

# 主要为了避免select 和 insert 语句放开的话出现异步问题，所以这里选择只设置一次
def _SInsert(tid, id, data):
	fields = ""
	values = ""

	for k, v in data.iteritems():
		fields += k + ","
		print(k, v, isinstance(v, str))
		if isinstance(v, str):
			s = "\"%s\","%(v)
		elif v == None:
			s = "NULL,"
		else:
			s = str(v) + ","
		values += s

	if len(s) > 0:
		if id > 0:
			return "insert into %s(%s, %s) values(%s, %s)"%(
				DTABLE_NAME[tid], DTABLE_PRIMARYKEY[tid], fields,
				id, values
			)
		else:
			return "insert into %s(%s, %s) select ifnull(max(%s), 0)+1, %s from %s;"%(
				DTABLE_NAME[tid],
				DTABLE_PRIMARYKEY[tid], fields[:-1],
				DTABLE_PRIMARYKEY[tid],	values[:-1],
				DTABLE_NAME[tid]
			)
	return ""

def _SMaxID(tid):
	return "select max(%s) from %s"%(DTABLE_PRIMARYKEY[tid], DTABLE_NAME[tid])

def _SSaveSql(tid, id, data):
	s = ""
	for k, v in data.iteritems():
		if isinstance(v, str):
			s += "%s = \"%s\","%(k, v)
		elif v == None:
			s += "%s = NULL,"%k
		else:
			try:
				s += "%s = %d,"%(k, v)
			except:
				ERROR("save error tid = %d, id = %d, key = %s, v = %s"%(tid, id, k, str(v)))
	if len(s) > 0:
		return "update %s set %s where %s = %d"%(DTABLE_NAME[tid], s[:-1], DTABLE_PRIMARYKEY[tid], id)

	return ""

def _SQuery(tid, id):
	return "select * from %s where %s = %d"%(DTABLE_NAME[tid], DTABLE_PRIMARYKEY[tid], id)

# 新建
def SNew(tid, id, data):
	sql = _SInsert(tid, id, data)
	if SQL_TYPE == SSQL_SQLITE:
		sqlite.New(sql)
		return id or  SMaxID(tid)

def SMaxID(tid):
	maxsql = _SMaxID(tid)
	if SQL_TYPE == SSQL_SQLITE:
		return sqlite.Query(maxsql)[0][0] or 0
# 保存
def SSave(tid, id, data):
	sql = _SSaveSql(tid, id, data)

	if SQL_TYPE == SSQL_SQLITE:
		return sqlite.Save(sql)

# 查询
def SQuery(tid, id):
	sql = _SQuery(tid, id)

	if SQL_TYPE == SSQL_SQLITE:
		return sqlite.Query(sql)
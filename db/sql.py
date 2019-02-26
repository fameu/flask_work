# -*- coding: gbk -*-
# @Time    : 2019/2/18 16:52
# @Author  : famu
# @File    : sql.py
# @Software: PyCharm

# �������ݿ����Ͳ�ͬ�������sql���Ҳ��һ��
# ���е�sql�Ĳ�����ͨ����������ת
# ��������ֻ������Ͳ�ѯ
# ����Ҳ����һ�α���
# ɾ����ʹ���޸�һ���ֶ���ʵ��
# ��ʵ��SQLite����䣬��Իþ����״

from define import *
import sqlite


SQL_TYPE	= SSQL_SQLITE

# ������Ҫ�и���ע�빦�ܣ���Ϊ��һ��ֱ�ӵ�sql��䣬��Ҫ����sqlע��

# ��ҪΪ�˱���select �� insert ���ſ��Ļ������첽���⣬��������ѡ��ֻ����һ��
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

# �½�
def SNew(tid, id, data):
	sql = _SInsert(tid, id, data)
	if SQL_TYPE == SSQL_SQLITE:
		sqlite.New(sql)
		return id or  SMaxID(tid)

def SMaxID(tid):
	maxsql = _SMaxID(tid)
	if SQL_TYPE == SSQL_SQLITE:
		return sqlite.Query(maxsql)[0][0] or 0
# ����
def SSave(tid, id, data):
	sql = _SSaveSql(tid, id, data)

	if SQL_TYPE == SSQL_SQLITE:
		return sqlite.Save(sql)

# ��ѯ
def SQuery(tid, id):
	sql = _SQuery(tid, id)

	if SQL_TYPE == SSQL_SQLITE:
		return sqlite.Query(sql)
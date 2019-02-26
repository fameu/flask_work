# -*- coding: gbk -*-
# @Time    : 2019/2/18 16:51
# @Author  : famu
# @File    : base.py.py
# @Software: PyCharm

from define import *
from sql import *

class CSaveObject(object):
	m_DataTable = None

	# 用来标记类的属性，没有特殊定义，就是对应数据库里面的列
	# 直接保存的  int, string 等简单结构
	m_EasySave	= {}

	# 需要转换格式的 (), [], {} 等复杂结构
	m_DiffSave	= {}

	# 特殊对应到数据库列
	m_SubSave	= {}
	m_SubSaveKey	= {}


	# 初始化 - 从0新建，或者读取数据库
	def __init__(self, id):
		self.m_ID = id
		self.Data = {}		# 存数据库的数据
		self.ApplyData = {}	# 不存数据库的数据

		# 根据ID是否有来判断是新建还是查询
		if id == 0:
			self.m_New = True
		else:
			self.Load()

	# ------------- 辅助函数 ------------
	# 从数据库数据到内存数据的转换
	def _Sql2Data(self, data):
		pd = {}
		for k, v in self.m_EasySave.iteritems():
			pd[v] = data.get(k)

		for k, v in self.m_DiffSave.iteritems():
			pd[v] = evalstring(data.get(k))

		for k, vlst in self.m_SubSaveKey.iteritems():
			d = evalstring(data.get(k))
			for v in vlst:
				pd[v] = d.get(v)
		self.Data.update(pd)

	# 从内存数据到数据库数据的转换
	def _Data2Sql(self):
		d = {}
		for k, v in self.m_EasySave.iteritems():
			if k not in self.m_SubSave:
				d[k] = self.Data.get(v)

		for k, v in self.m_DiffSave.iteritems():
			if k not in self.m_SubSave:
				d[k] = formatstring(self.Data.get(v))

		if len(self.m_SubSaveKey):
			for k, vlst in self.m_SubSaveKey.iteritems():
				dk = {}
				for v in vlst:
					dk[k] = self.Data.get(v)
				d[k] = formatstring(dk)
		return d
	# ------------- 辅助函数 ------------

	# ------------- 功能 ---------------
	def IsNew(self):
		return self.m_New

	# ------------- 功能 ---------------

	# ------------- 数据库操作 ------------
	# 保存
	def Save(self):
		data = self._Data2Sql()
		if self.IsNew():
			# 这里用SNew 是担心多并发情况下，select 和 insert 对应不上
			nid = SNew(self.m_DataTable, self.m_ID, data)
			self.m_ID = nid
			self.m_New = False
		else:
			SSave(self.m_DataTable, self.m_ID, data)

	# 查询所有列
	def Query(self):
		dct = {}
		ridx = {}
		rows, data = SQuery(self.m_DataTable, self.m_ID)
		for idx, rdata in enumerate(rows):
			_, name, _, _, _, _ = rdata
			ridx[idx] = name
		return dict(zip([name for _,name,_, _, _, _ in rows], data[0]))

	@classmethod
	def QueryMax(cls):
		return SMaxID(cls.m_DataTable)
	# ------------- 数据库操作 ------------

	# 逻辑处理
	def Load(self):
		data = self.Query()
		self._LoadData(data)

	def _LoadData(self, data):
		if data == None:
			self.__New = True
		else:
			self._Sql2Data(data)

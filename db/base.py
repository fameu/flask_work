# -*- coding: gbk -*-
# @Time    : 2019/2/18 16:51
# @Author  : famu
# @File    : base.py.py
# @Software: PyCharm

from define import *
from sql import *



class CSaveObject(object):
	m_DataTable = None

	m_EasySave	= {}
	# 直接保存的  int, string 等简单结构

	m_DiffSave	= {}
	# 需要转换格式的 (), [], {} 等复杂结构


	# 初始化 - 从0新建，或者读取数据库
	def __int__(self, id):
		self.m_ID = id
		self.__Callback = []	# 回调
		self.Data = data.CData()

		# 根据ID是否有来判断是新建还是查询
		if id:
			self.m_New = True
		else:
			self._Loading = True
			self.Load()

	# ------------- 辅助函数 ------------
	# 从数据库数据到内存数据的转换
	def _Sql2Data(self, data):
		pd = {}
		for k, v in self.m_EasySave:
			pd[v] = data.get(k)
		self.Data.update(pd)




	# 从内存数据到数据库数据的转换
	def _Data2Sql(self):
		d = {}
		for k, v in self.m_EasySave:
			d[k] = self.Data.get(v)
		for k, v in self.m_DiffSave:
			d[k] = formatstring(self.Data.get(v))
		return {}
	# ------------- 辅助函数 ------------

	# ------------- 数据库操作 ------------
	# 保存
	def Save(self):
		data = self._Data2Sql()
		return SSave(data)
	# 查询
	def Query(self):
		return SQuery(self.m_ID)
	# ------------- 数据库操作 ------------

	# 逻辑处理
	def Load(self):
		# 这里会不会存在异步的问题存在呢
		data = self.Query()
		self._LoadData(data)

	def _LoadData(self, data):
		if data == None:
			self.__New = True
		else:
			self._Sql2Data(data)

		self._Loading = False

		for cb in self.__Callback:
			cb(self)

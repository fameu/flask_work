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
	# ֱ�ӱ����  int, string �ȼ򵥽ṹ

	m_DiffSave	= {}
	# ��Ҫת����ʽ�� (), [], {} �ȸ��ӽṹ


	# ��ʼ�� - ��0�½������߶�ȡ���ݿ�
	def __int__(self, id):
		self.m_ID = id
		self.__Callback = []	# �ص�
		self.Data = data.CData()

		# ����ID�Ƿ������ж����½����ǲ�ѯ
		if id:
			self.m_New = True
		else:
			self._Loading = True
			self.Load()

	# ------------- �������� ------------
	# �����ݿ����ݵ��ڴ����ݵ�ת��
	def _Sql2Data(self, data):
		pd = {}
		for k, v in self.m_EasySave:
			pd[v] = data.get(k)
		self.Data.update(pd)




	# ���ڴ����ݵ����ݿ����ݵ�ת��
	def _Data2Sql(self):
		d = {}
		for k, v in self.m_EasySave:
			d[k] = self.Data.get(v)
		for k, v in self.m_DiffSave:
			d[k] = formatstring(self.Data.get(v))
		return {}
	# ------------- �������� ------------

	# ------------- ���ݿ���� ------------
	# ����
	def Save(self):
		data = self._Data2Sql()
		return SSave(data)
	# ��ѯ
	def Query(self):
		return SQuery(self.m_ID)
	# ------------- ���ݿ���� ------------

	# �߼�����
	def Load(self):
		# ����᲻������첽�����������
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

# -*- coding: gbk -*-
# @Time    : 2019/2/18 16:51
# @Author  : famu
# @File    : base.py.py
# @Software: PyCharm

from define import *
from sql import *



class CSaveObject(object):
	m_DataTable = None

	# �������������ԣ�û�����ⶨ�壬���Ƕ�Ӧ���ݿ��������
	# ֱ�ӱ����  int, string �ȼ򵥽ṹ
	m_EasySave	= {}

	# ��Ҫת����ʽ�� (), [], {} �ȸ��ӽṹ
	m_DiffSave	= {}

	# �����Ӧ�����ݿ���
	m_SubSave	= {}
	m_SubSaveKey	= {}


	# ��ʼ�� - ��0�½������߶�ȡ���ݿ�
	def __int__(self, id):
		self.m_ID = id
		self.__Callback = []	# �ص�
		self.Data = {}		# �����ݿ������
		self.ApplyData = {}	# �������ݿ������

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

		for k, v in self.m_DiffSave:
			pd[v] = evalstring(data.get(k))

		for k, vlst in self.m_SubSaveKey:
			d = evalstring(data.get(k))
			for v in vlst:
				pd[v] = d.get(v)
		self.Data.update(pd)


	# ���ڴ����ݵ����ݿ����ݵ�ת��
	def _Data2Sql(self):
		d = {}
		for k, v in self.m_EasySave:
			if k not in self.m_SubSave:
				d[v] = self.Data.get(k)

		for k, v in self.m_DiffSave:
			if k not in self.m_SubSave:
				d[v] = formatstring(self.Data.get(k))

		if len(self.m_SubSaveKey):
			for k, vlst in self.m_SubSaveKey:
				dk = {}
				for v in vlst:
					dk[v] = self.Data.get(v)
				d[k] = formatstring(dk)
		return d
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

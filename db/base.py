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
	def __init__(self, id):
		self.m_ID = id
		self.Data = {}		# �����ݿ������
		self.ApplyData = {}	# �������ݿ������

		# ����ID�Ƿ������ж����½����ǲ�ѯ
		if id == 0:
			self.m_New = True
		else:
			self.Load()

	# ------------- �������� ------------
	# �����ݿ����ݵ��ڴ����ݵ�ת��
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

	# ���ڴ����ݵ����ݿ����ݵ�ת��
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
	# ------------- �������� ------------

	# ------------- ���� ---------------
	def IsNew(self):
		return self.m_New

	# ------------- ���� ---------------

	# ------------- ���ݿ���� ------------
	# ����
	def Save(self):
		data = self._Data2Sql()
		if self.IsNew():
			# ������SNew �ǵ��Ķಢ������£�select �� insert ��Ӧ����
			nid = SNew(self.m_DataTable, self.m_ID, data)
			self.m_ID = nid
			self.m_New = False
		else:
			SSave(self.m_DataTable, self.m_ID, data)

	# ��ѯ������
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
	# ------------- ���ݿ���� ------------

	# �߼�����
	def Load(self):
		data = self.Query()
		self._LoadData(data)

	def _LoadData(self, data):
		if data == None:
			self.__New = True
		else:
			self._Sql2Data(data)

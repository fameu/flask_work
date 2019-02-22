# -*- coding: gbk -*-
# @Time    : 2019/2/21 14:32
# @Author  : famu
# @File    : product.py
# @Software: PyCharm

from db.base import *


PRODUCT_MAX	= 500	# ��ౣ��500����Ʒ

class CProduct(CSaveObject):
	m_DataTable = DTABLE_PRODUCT
	m_EasySave = {
		"pid"	: "m_ID",
		"name"	: "m_Name",
	}
	m_DiffSave = {
		"info"	: "m_Info",
	}

class CProductList(object):
	def __init__(self):
		self.Products = []	# ��Ʒ�б�
		self.LoadProducts()

		# ����{}������
		# ������ÿ�����һ���Զ�������
		# ���Զ�����дһЩ�Զ���ķ���
		# �����ѯ���޸�
		# self.NameProduct = {}	# ����Ϊ����

	def IsOverload(self):
		return len(self.Products) >= PRODUCT_MAX

	def LoadProducts(self):
		for id in xrange(1, Product.QueryMax()):
			pob = CProduct(id)
			self.Products.append(pob)

	def NewProduct(self, data):
		pob = CProduct(0)
		pob.Data.update(data)
		pob.Save()
		self.Products.append(pob)

if not globals().has_key("g_Products"):
	g_Products = CProductList()



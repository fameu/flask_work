# -*- coding: gbk -*-
# @Time    : 2019/2/21 14:32
# @Author  : famu
# @File    : product.py
# @Software: PyCharm

from db.base import *


PRODUCT_MAX	= 500	# 最多保存500个产品

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
		self.Products = []	# 产品列表
		self.LoadProducts()

		# 先用{}来保存
		# 这里最好可以做一个自定义容器
		# 可以对容器写一些自定义的方法
		# 方便查询，修改
		# self.NameProduct = {}	# 名字为索引

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



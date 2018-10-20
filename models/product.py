# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 14:14 10:08
# @Author  : FAMU
# @File    : product.py
# @Software: PyCharm

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from db.database import *

class Product(DataBase):
    def __init__(self, name, info):
        self.name, self.info = name, info

    def _class_str_(self):
        return "Product"

    def _info_str_(self):
        return "name:%s info:%s"%(self.name, self.info)

product = Table("product", metaData,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String(50)),
        Column("info", String(200)),
    )
mapper(Product, product)
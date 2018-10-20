# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 14:13 10:08
# @Author  : FAMU
# @File    : company.py
# @Software: PyCharm

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from db.database import *

class Company(DataBase):
    def __init__(self, name):
        self.name = name

    def _class_str_(self):
        return "Company"

    def _info_str_(self):
        return "name:%s"%(self.name)

company = Table("company", metaData,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String(50)),
    )
mapper(Company, company)


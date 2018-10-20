# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 13:33 10:08
# @Author  : FAMU
# @File    : user.py
# @Software: PyCharm

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from db.database import *

class User(DataBase):
    def __init__(self, name):
        self.name = name

    def _class_str_(self):
        return "User"

    def _info_str_(self):
        return "name:%s"%(self.name)

users = Table("user", metaData,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String(50)),
    )

mapper(User, users)


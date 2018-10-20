# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 14:37 10:08
# @Author  : FAMU
# @File    : stockin.py
# @Software: PyCharm


from sqlalchemy import Table, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapper
from datetime import datetime
from db.database import *


class StockIn(DataBase):
    def __init__(self, uid, pid, cid, cnt):
        self.uid, self.pid, self.cid, self.cnt = uid, pid, cid, cnt

    def _class_str_(self):
        return "StockIn"

    def _info_str_(self):
        return "Date:%s uid:%d pid:%d cid:%d cnt:%d" % (self.data, self.uid, self.pid, self.cid, self.cnt)

stockin = Table(
    "stockin", metaData,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("date", DateTime, default=datetime.now()),
    Column("uid", Integer, ForeignKey("user.id")),
    Column("pid", Integer, ForeignKey("product.id")),
    Column("cid", Integer, ForeignKey("company.id")),
    Column("cnt", Integer),
)

mapper(StockIn, stockin)

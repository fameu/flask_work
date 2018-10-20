# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 23:12 10:08
# @Author  : FAMU
# @File    : database.py
# @Software: PyCharm


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///db/db_zqq.db")
metaData = MetaData()
dbSession = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
    metaData.create_all(bind=engine)


class DataBase(object):
    query = dbSession.query_property()

    def _class_str_(self):
        return "_class_str_"

    def _info_str_(self):
        return "_info_str_"

    def __repr__(self):
        return "<%s> %d, %s" % (self._class_str_(), self.id, self._info_str_())





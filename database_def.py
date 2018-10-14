# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 23:17 10:08
# @Author  : FAMU
# @File    : database_def.py
# @Software: PyCharm


DATABASE = "zqq"
SQL_TYPE    = {
    "create"    : "create table %s %s;",
}


TABLE_STOCK_OUT = 0
TABLE_STOCK_IN  = 1

TABLE_NAME  = {
    TABLE_STOCK_OUT : "stock_out",  #出库单
    TABLE_STOCK_IN : "stock_in",    #入库单
}


TYPE_INT    = "int"
TYPE_TEXT   = "text"

TABLE_ROW   = {
    TABLE_STOCK_OUT : {
        "id"    : TYPE_INT,
        "name"    : TYPE_TEXT,
    },
    TABLE_STOCK_OUT : {
        "id"    : TYPE_INT,
        "name"    : TYPE_TEXT,
        "cnt"   : TYPE_INT,
    },
}

def GetCreateTableSql(dname):
    table_rows = TABLE_ROW[dname]
    sql = SQL_TYPE["create"]
    sql = sql % (TABLE_NAME[dname], "(%s)" % (",".join("%s %s" % (k, v) for k, v in table_rows.items())))
    return sql


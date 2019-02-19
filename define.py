# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 23:37 10:08
# @Author  : FAMU
# @File    : define.py.py
# @Software: PyCharm

# 数据库连接类型
SSQL_MYSQL          = 1
SSQL_SQLITE         = 2
SSQL_HBASE          = 3

# 表序号
DTABLE_COMPANY      = 1
DTABLE_PRODUCT      = 2
DTABLE_STOCKIN      = 3
DTABLE_STOCKOUT     = 4

# 主键
DTABLE_PRIMARYKEY   = {
    DTABLE_COMPANY  : "id",
    DTABLE_PRODUCT  : "id",
    DTABLE_STOCKIN  : "id",
    DTABLE_STOCKOUT  : "id",
}

# 表名
DTABLE_NAME         = {
    DTABLE_COMPANY  : "tbl_company",
    DTABLE_PRODUCT  : "tbl_product",
    DTABLE_STOCKIN  : "tbl_stockin",
    DTABLE_STOCKOUT  : "tbl_stockout",
}

def ERROR(msg):
    print(msg)


def formatstring(data):
    return str(data)

def evalstring(str):
    return eval(str)

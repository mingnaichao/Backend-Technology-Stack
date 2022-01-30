# -*- coding: utf-8 -*-
# @author : MingNC
# @date : 2019/12/1
# @time : 19:49
import pymongo

conn = pymongo.Connect('localhost', 27017)
db = conn.example or conn['example']  # 获取数据库对象，无则创建
db.connection_names()  # 获取集合列表

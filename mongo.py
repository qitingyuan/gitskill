# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:49:44 2017

@author: sgd
"""

import pymongo
client = pymongo.MongoClient("192.168.8.13", 27017)
db = client.museum_demo
#查看test数据库中集合信息

#插入1000000条文档信息
for i in  range(10):
    db.pppp.insert({"test":"tnt","index":i})


#显示my_collection集合中文档数目
print  ('插入完毕，当前文档数目：')
print (db.pppp.find().count())
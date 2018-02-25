# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: test
@ time: 17-12-25
"""
import requests

# data = {'data':'test','busLine':145}
# # r = requests.get('127.0.0.1:8000/save/businfo',params=data)
# # print r.content
# res = requests.get('http://127.0.0.1:8000/save/businfo',params=data)
# print res.content
data_list = []
for i in range(0,24):
    data_list.append((str(i) + u'时').encode('utf-8'))
print data_list

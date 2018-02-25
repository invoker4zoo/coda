# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: busline_union
@ time: 18-1-12
"""
import os
import sys
import json

PATH = './busline'
list = os.listdir(PATH)
line_list = []
for item in list:
    path = os.path.join(PATH, item)
    if os.path.isfile(path):
        with open(path, mode='r') as f:
            print path
            data = json.loads(f.read())
            line_list.append(data['linePoints'])

with open('./busline/union/lineUnion.json','w') as f:
    f.write(json.dumps(line_list,ensure_ascii=False,indent=4))

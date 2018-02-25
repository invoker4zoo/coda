# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: generate_point
@ time: 18-1-24
"""
import numpy
import json
import random
# [106.373000,29.753000] [106.703000,29.753000]
# [106.373000,29.423000] [106.703000,29.423000]
# 0.3300
# 0.0025
# 132*132 3769
points = []
for i in range(0, 132):
    list_1 = []
    for j in range(0, 132):
        list_1.append([106.373000 + i * 0.0025, 29.423 + j * 0.0025, 0])
    points.append(list_1)

sample_points = random.sample(range(0, 132*132), 3769)
for item in sample_points:
    row = item/132
    col = item%132
    points[row][col][2] = random.randrange(0,10)

with open('./busline/union/randomPoints.json','w') as f:
    _points = []
    for _list in points:
        _points += _list
    f.write(json.dumps(_points,ensure_ascii=False,indent=2))
# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: stations_union
@ time: 18-1-22
"""
import os
import sys
import json

PATH = '/home/showlove/coda/POI_TEST'
list = os.listdir(PATH)
stations_dict = {}
line_list = []
for item in list:
    path = os.path.join(PATH, item)
    if os.path.isfile(path):
        with open(path, mode='r') as f:
            point_list = []
            data = json.loads(f.read())
            for data_item in data['features']:
                point_list.append([float(data_item['geometry']['x']), float(data_item['geometry']['y']), 1])

            with open(os.path.join(PATH + '/trans', '_'+item), 'w') as f:
                f.write(json.dumps(point_list, ensure_ascii=False, indent=2))

# with open('./busline/union/lineUnion.json','w') as f:
#     f.write(json.dumps(line_list,ensure_ascii=False,indent=4))
# staions_list = []
# for key in stations_dict.keys():
#     staions_list.append({
#         'name':key,
#         'location':stations_dict[key]['location'],
#         'count':stations_dict[key]['count']
#     })

# with open('./busline/union/stationUnion.json','w') as f:
#     f.write(json.dumps(stations_dict,ensure_ascii=False,indent=2))
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

def generate_station_union():
    PATH = './busline'
    list = os.listdir(PATH)
    stations_dict = {}
    line_list = []
    for item in list:
        path = os.path.join(PATH, item)
        if os.path.isfile(path):
            with open(path, mode='r') as f:
                print path
                data = json.loads(f.read())
                staions_info = data['stations']
                for station_item in staions_info:
                    station_name = station_item['name'].encode('utf-8')
                    staions_location = station_item['value']
                    if station_name not in stations_dict.keys():
                        stations_dict[station_name] = {
                            'location':staions_location,
                            'count':1
                        }
                    else:
                        stations_dict[station_name]['count'] += 1

    # with open('./busline/union/lineUnion.json','w') as f:
    #     f.write(json.dumps(line_list,ensure_ascii=False,indent=4))
    # staions_list = []
    # for key in stations_dict.keys():
    #     staions_list.append({
    #         'name':key,
    #         'location':stations_dict[key]['location'],
    #         'count':stations_dict[key]['count']
    #     })

    with open('./busline/union/stationUnion.json','w') as f:
        f.write(json.dumps(stations_dict,ensure_ascii=False,indent=2))

def generate_station_point():
    PATH = './busline'
    file_list = os.listdir(PATH)
    staion_list = list()
    for item in file_list:
        path = os.path.join(PATH, item)
        if os.path.isfile(path):
            with open(path, mode='r') as f:
                print path
                data = json.loads(f.read())
                staions_info = data['stations']
# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: do_with_region
@ time: 18-2-25
"""
import json

file_list = ['主城分区.json', '组团.json', '主城小区.json']
output_file = ['region_1.json', 'region_2.json', 'region_3.json']

with open(file_list[0],'r') as f:
    data = json.loads(f.read())
    trans_data = []
    for region_item in data['features']:
        trans_data.append({
            'name': region_item['attributes']['F'],
            'area': region_item['attributes']['AREA'],

        })
# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechat: whatshowlove
@ software: PyCharm
@ file: net_line
@ time: 18-3-5
"""
# import xlrd
import json
net_info = []
with open('线路优化_1.csv','r') as f:
    table_net = f.readlines()
for row in range(1, 43):
    net_name = table_net[row].split(',')[12]
    station_list = []
    for col in range(0, 12):
        station_list.append(table_net[row].split(',')[16 + col * 4])
    net_info.append({
        'lineName': net_name,
        'stationList': station_list
    })
with open('net_line.json', 'w') as f:
    f.write(json.dumps(net_info, ensure_ascii=False, indent=1))
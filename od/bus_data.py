# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechat: whatshowlove
@ software: PyCharm
@ file: bus_data
@ time: 18-2-27
"""
import json
import os
import xlrd
with open('公交上下客.csv','r') as f:
    table_od=f.readlines()
# table_od = xlrd.open_workbook('公交上下客.xls').sheets()[0]
table_id = xlrd.open_workbook('线路编号.xls').sheets()[0]
od_range = [2,16303]# col 0,5
id_range = [2,19960]# col 0,1
station_dict = {}
up_list = []
down_list = []
#table.cell(row,col).value
for row in range(2,16302):
    try:
        up_list.append(int(table_od[row].split(',')[0]))
    except:
        continue
    try:
        down_list.append(int(table_od[row].split(',')[5]))
    except:
        continue
for row in range(2,19960):
    if table_id.cell(row, 1).value not in station_dict.keys() and table_id.cell(row, 1).value!='':
        station_dict[table_id.cell(row, 1).value] = [int(table_id.cell(row, 0).value)]
    elif table_id.cell(row, 1).value!='':
        station_dict[table_id.cell(row, 1).value].append(int(table_id.cell(row, 0).value))

station_info = []
for station_name in station_dict.keys():
    try:
        check_list = station_dict[station_name]
        up_count = len([idx for idx,val in enumerate(up_list) if val in check_list])
        down_count = len([idx for idx,val in enumerate(down_list) if val in check_list])
        station_info.append({
            'name':station_name.encode('utf-8'),
            'up':up_count,
            'down':down_count
        })
    except:
        continue

with open('staion_info.json','w') as f:
    f.write(json.dumps(station_info,ensure_ascii=False,indent=1))
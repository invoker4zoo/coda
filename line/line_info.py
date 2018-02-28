# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechat: whatshowlove
@ software: PyCharm
@ file: line_info
@ time: 18-2-28
"""
import json
line_data = [175096.8810776,304773.2743975,1371013.9639066,458643.507844799,157305.9112169,123780.0036951,\
497575.329284,542030.449455001,496218.2102355,100380.5318414,255485.1921874,\
 422755.3188372,196040.1283567,628014.7537218,549183.6644059,566730.692388,429787.1752102,223198.2927855,356281.4485926]

bus_line_data = [609590.1967781,
                11862.3598633,
                1917461.1508799,
                142176.7114258,
                42932.0996094,
                43188.2402344,
                312479.1747438,
                2898432.2338561,
                3683935.2539082,
                594821.8359378,
                1768696.2021497,
                263495.7995606,
                307870.3237306,
                475693.8514268,
                1785960.7507334,
                1855099.2177744,
                734804.2529302,
                365057.5996095,
                832072.412030001]

unit_name = ['渝中组团',
            '鱼嘴组团',
            '西永组团',
            '西彭组团',
            '唐家沱组团',
            '水土组团',
            '沙坪坝组团',
            '人和组团',
            '南坪组团',
            '李家沱组团',
            '礼嘉组团',
            '空港组团',
            '界石组团',
            '观音桥组团',
            '大杨石组团',
            '大渡口组团',
            '茶园组团',
            '蔡家组团',
            '北碚组团']

unit_info = []
for index in range(len(unit_name)):
    unit_info.append([round(line_data[index],3),round(bus_line_data[index],3),\
                      round(bus_line_data[index]/(line_data[index]+bus_line_data[index]),3)])
with open('unit_info.json', 'w') as f:
    f.write(json.dumps(unit_info,ensure_ascii=False,indent=1))
with open('unit_name.json', 'w') as f:
    f.write(json.dumps(unit_name,ensure_ascii=False,indent=1))
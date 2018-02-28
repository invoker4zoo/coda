# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechat: whatshowlove
@ software: PyCharm
@ file: od_data
@ time: 18-2-27
"""
import xlrd
import json


def region_od():
    """

    :return:
    """
    self_od = []
    link_od = []
    node_list = []
    region_list = ['巴南区','北碚区',	'大渡口区','江北区','九龙坡区','南岸区','沙坪坝区','渝北区','渝中区']
    for region in region_list:
        node_list.append({
            'name': region
        })
        node_list.append({
            'name': region + ' '
        })
    table = xlrd.open_workbook('主城OD.xls').sheets()[0]
    for row in range(0, 9):
        for col in range(0, 9):
            if row == col:
                self_od.append({
                    'name': region_list[row],
                    'value': int(table.cell(row,col).value)
                })
            else:
                link_od.append({
                    'source': region_list[row],
                    'target': region_list[col] + ' ',
                    'value': int(table.cell(row,col).value)
                })
    with open('region_od_node.json', 'w') as f:
        f.write(json.dumps(node_list,ensure_ascii=False,indent=1))
    with open('region_od_self.json', 'w') as f:
        f.write(json.dumps(self_od,ensure_ascii=False,indent=1))
    with open('region_od_link.json', 'w') as f:
        f.write(json.dumps(link_od,ensure_ascii=False,indent=1))

region_od()

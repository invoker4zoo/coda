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

from util.point_trans import wgs84tobd09

file_list = ['主城分区.json', '组团.json', '主城小区.json']
output_file = ['region_1.json', 'region_2.json', 'region_3.json']


def find_center_point(point_list):
    """

    :param point_list: ring point list
    :return: center point
    """
    length = len(point_list)
    return [sum([item[0] for item in point_list])/length, sum([item[1] for item in point_list])/length]


def trans_point(point_list):
    """

    :param point_list:
    :return:
    """
    return [wgs84tobd09(item[0], item[1]) for item in point_list]


def initial_region_json():
    """

    :return: write initial json file
    """
    with open(file_list[0], 'r') as f:
        data = json.loads(f.read())
        trans_data = []
        for region_item in data['features']:
            trans_data.append({
                'name': region_item['attributes']['F'].encode('utf-8'),
                'area': region_item['attributes']['AREA'],
                'pointRing': trans_point(region_item['geometry']['rings'][0]),
                'center': find_center_point(trans_point(region_item['geometry']['rings'][0]))
            })
        with open(output_file[0],'w') as g:
            g.write(json.dumps(trans_data, ensure_ascii=False, indent=4))

    with open(file_list[1],'r') as f:
        data1 = json.loads(f.read())
        trans_data = []
        for region_item in data1['features']:
            trans_data.append({
                'name': region_item['attributes']['F1'].encode('utf-8'),
                'area': region_item['attributes']['AREA'],
                'pointRing': trans_point(region_item['geometry']['rings'][0]),
                'center': find_center_point(trans_point(region_item['geometry']['rings'][0]))
            })
        with open(output_file[1],'w') as g:
            g.write(json.dumps(trans_data, ensure_ascii=False, indent=1))

    with open(file_list[2],'r') as f:
        data2 = json.loads(f.read())
        trans_data = []
        for region_item in data2['features']:
            trans_data.append({
                'name': region_item['attributes']['ID'],
                'area': region_item['attributes']['AREA'],
                'pointRing': trans_point(region_item['geometry']['rings'][0]),
                'center': find_center_point(trans_point(region_item['geometry']['rings'][0]))
            })
        with open(output_file[2],'w') as g:
            g.write(json.dumps(trans_data, ensure_ascii=False, indent=1))


def cal_center_point():
    """

    :return: add center point of all region
    """
    pass


initial_region_json()
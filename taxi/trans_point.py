# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechat: whatshowlove
@ software: PyCharm
@ file: trans_point
@ time: 18-2-26
"""
import os
import json

lng_range = [106.2700, 106.7000]
lat_range = [29.3200, 29.7500]
step = 0.0010
side = int((lng_range[1] - lng_range[0])/step)


def generate_grid():
    """
    创建网格,range 不支持float数据类型
    :return:
    """
    grid = list()
    for row in range(0, side):
        for col in range(0, side):
            grid.append([lng_range[0] + row * step, lat_range[0] + col * step, 0])
    return grid


def put_point_in_grid(point_list):
    """

    :param point_list:
    :return:
    """
    grid = generate_grid()
    for point in point_list:
        index = int((point[0]-lng_range[0])/step) * side + int((point[1]-lat_range[0])/step)
        grid[index][2] += 1
    return grid


def check_point_range(point):
    return True if point[1]>=lat_range[0] and point[1]<=lat_range[1] and point[0]>=lng_range[0] and point[0]<=lng_range[1] else False


def main():
    base_path = './data'
    file_list = ['begin_position.txt', 'end_position.txt', 'up_position.txt', 'down_position.txt', 'stop_position.txt']
    for file_name in file_list:
        base_name = file_name.split('.')[0]
        with open(os.path.join(base_path, file_name), 'r') as f:
            point_list = list()
            for line in f.readlines():
                point = [float(line.split(',')[0]), float(line.split(',')[1])]
                if check_point_range(point):
                    point_list.append(point)
            trans_grid = put_point_in_grid(point_list)
            with open(os.path.join(base_path, ('taxi_' + base_name + '.json')), 'w') as g:
                g.write(json.dumps(trans_grid,ensure_ascii=False, indent=1))
                

if __name__ == '__main__':
    main()
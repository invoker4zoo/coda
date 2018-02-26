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


lng_range = [106.2700, 106.7000]
lat_range = [29.3200, 29.7500]
step = 0.0025
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
        index = int((point[0]-lng_range[0])/0.0025) * side + int((point[1]-lat_range[0])/0.0025)
        grid[index][2] += 1
    return grid


def check_point_range(point):
    return True if point[0]>=lat_range[0] and point[0]<=lat_range[1] and point[1]>=lng_range[0] and point[1]<=lng_range[1] else False


def main():
    file_list = ['begin_position.txt', 'end_position', 'up_position.txt', 'down_position.txt', 'stop_position.txt']
    for file in file_list:
        with open(file, 'r') as f:
            point_list = list()
            for line in f.readlines():
                point = [float(line.split(',')[0]), float(line.split(',')[1])]
                

if __name__ == '__main__':
    pass
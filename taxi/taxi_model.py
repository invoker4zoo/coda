# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: taxi_model
@ time: 18-2-7
"""
from db_tool import PgUtil
# init
pg = PgUtil()
DATE_LIST = ['20170301','20170302','20170303','20170304','20170305','20170306','20170307']
# 硬盘空间
# DATE_LIST = ['20170301','20170302','20170303','20170304']
# BEGIN_POSITON = []
# END_POSITION = []
# UP_POSITION = []
# DOWN_POSITION = []
# STOP_POSITION = []
BEGIN_POSITION_FILE = 'begin_position.txt'
END_POSITION_FILE = 'end_position.txt'
UP_POSTION_FILE = 'up_position.txt'
DOWN_POSITION_FILE = 'down_position.txt'
STOP_POSITION_FILE = 'stop_position.txt'
TAXI_ID_FILE = 'taxi_id.txt'


def search_taxi_id():
    """
    查询出租车id列表
    result format:[{dict},]
    :return: taxi_id list
    """
    sql = "select distinct(taxi_id) from taxi"
    result = pg.query_all_sql(sql)
    return [item['taxi_id'] for item in result]


def write_taxi_id(id_list):
    """

    :param id_list:
    :return:
    """
    with open(TAXI_ID_FILE,'w') as f:
        for id in id_list:
            f.write(id + '\n')

def find_up_down_index(result):
    """
    通过一天内车行状态列表，得出上下车位置
    :param result: 查询结果（1天出租车运行情况）
    :return: up_index_list, down_index_list
    """
    status_list = [item['status'] for item in result]
    diff_list =[status_list[1:][i]-status_list[0:-1][i] for i in range(len(status_list[0:-1]))]
    _up_index_list = [index for index,item in enumerate(diff_list) if item==1]
    up_index_list = [item + 1 for item in _up_index_list]
    _down_index_list = [index for index,item in enumerate(diff_list) if item==-1]
    down_index_list = [item + 1 for item in _down_index_list]
    return up_index_list,down_index_list


def find_series_num(num_list,step=3):
    index_list = []
    for index in num_list:
        for i in range(1, step):
            if i+index in num_list:
                tag = i+index
            else:
                tag = i + index
                break
        if (tag - index + 1)==step and len(index_list)<>0 and (index - index_list[-1])>step:
            index_list.append(index)
        if (tag - index + 1)==step and len(index_list)==0:
            index_list.append(index)
    return index_list


def find_stop_position_index(result, step=10):
    """
    找到处于连续停车状态的index
    :param result:
    :return: stop_index
    """
    index_list = []
    stop_index_list = [index for index,item in enumerate(result) if item['status']==0 and item['speed']==0]
    return find_series_num(stop_index_list,step=step)


def find_time_part(i,max):
    return i/(max/3)


def search_taxi_position_by_taxi_id(taxi_id):
    """
    查询出租车每天的GPS点列表
    :param taxi_id:
    :return:
    """
    sql = """
            select * from taxi where taxi_id=%s and data_date=%s
            order by gps_time
          """
    for date in DATE_LIST:
        result = pg.select_all_sql(sql,(taxi_id, date))
        if len(result)>0:
            up_index_list, down_index_list = find_up_down_index(result)
            stop_index_list = find_stop_position_index(result,step=15)
            result_length = len(result)
            with open(BEGIN_POSITION_FILE,'a+') as f:
                f.write(str(result[0]['longitude']) + ',' + str(result[0]['latitude']) + '\n')
            with open(END_POSITION_FILE, 'a+') as f:
                f.write(str(result[-1]['longitude']) + ',' + str(result[-1]['latitude']) + '\n')
            with open(UP_POSTION_FILE,'a+') as f:
                for index in up_index_list:
                    f.write(str(result[index]['longitude']) + ',' + str(result[index]['latitude']) + ',' + str(find_time_part(index, result_length)) + '\n')
            with open(DOWN_POSITION_FILE, 'a+') as f:
                for index in down_index_list:
                    f.write(str(result[index]['longitude']) + ',' + str(result[index]['latitude']) + ',' + str(find_time_part(index, result_length)) + '\n')
            with open(STOP_POSITION_FILE, 'a+') as f:
                for index in stop_index_list:
                    f.write(str(result[index]['longitude']) + ',' + str(result[index]['latitude']) + ',' + str(find_time_part(index, result_length)) + '\n')
        else:
            pass


if __name__=='__main__':
    # id_list = search_taxi_id()
    # write_taxi_id(id_list)
    # for id in id_list:
    #     search_taxi_position_by_taxi_id(id)
    # No.2262 2018-2-11
    with open(TAXI_ID_FILE,'r') as f:
        id_list = f.readlines()

        for index,id in enumerate(id_list):
            if index<11:
                pass
            else:
                print 'parse NO.%d taxi %s' %(index, id)
                id = id.strip()
                search_taxi_position_by_taxi_id(id)
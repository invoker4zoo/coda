# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechat: whatshowlove
@ software: PyCharm
@ file: generate_data
@ time: 18-3-1
"""
import json
import random
seed_list = [[0.4,0.5],[0.2,0.3],[0.15,0.18],[0.13,0.15],[0.15,0.18],[0.18,0.2],[0.2,0.3],[0.5,0.7],[0.8,0.9],[0.8,0.9],[0.7,0.85],[0.65,0.7],[0.65,0.7],\
        [0.6,0.7], [0.6, 0.7],[0.6,0.7],[0.6,0.7],[0.8,0.9],[0.8,0.9],[0.7,0.9],[0.6,0.7],[0.6,0.7],[0.5,0.6],[0.5,0.6]]
random_seed = [[random.random()]]

def gene_random_series_num(seed_list=seed_list,max=0,is_int=True):
    if is_int:
        return [int(random.uniform(seed[0],seed[1])*max) for seed in seed_list]
    else:
        return [round(random.uniform(seed[0], seed[1]) * max,2) for seed in seed_list]


def gene_random_series_num_reversal(seed_list=seed_list,max=0,is_int=True):
    if is_int:
        return [int((1-random.uniform(seed[0],seed[1]))*max) for seed in seed_list]
    else:
        return [round((1-random.uniform(seed[0], seed[1])) * max,2) for seed in seed_list]


def gene_car_count():
    for idx,count in enumerate(gene_random_series_num(max=150000)):
        print "{x: '%d时', y: %d}"%(idx,count) + ','


def gene_car_speed():
    for idx,count in enumerate(gene_random_series_num_reversal(max=80,is_int=False)):
        print "{ x: '%d时', y: %.2f }"%(idx,count) + ','


def gene_lag_time():
    for idx,count in enumerate(gene_random_series_num(max=400,is_int=False)):
        print "{ x: '%d时', y: %.2f }"%(idx,count) + ','


def gene_traff_index():
    for idx,count in enumerate(gene_random_series_num_reversal(max=1,is_int=False)):
        print "{ x: '%d时', y: %.2f }"%(idx,count) + ','


def gene_station_dis(seed_list=seed_list,max=0,is_rev=False):
    _seed_list = [1- random.uniform(seed[0], seed[1]) for seed in seed_list] if is_rev else [random.uniform(seed[0], seed[1]) for seed in seed_list]
    _seed_list = [0,0,0,0,0,0] + _seed_list[6:22] +[0,0]
    return [int(_seed/sum(_seed_list) * max) for _seed in _seed_list]


def gene_taxi_speed():
    info_list = gene_random_series_num(max=50,is_int=False)
    for idx,count in enumerate(info_list):
        print "{ x: '%d时', y: %.2f }"%(idx,count) + ','
        sum_count = 0
    for idx, count in enumerate(info_list):
        sum_count += count
        print "{ x: '%d时', y: %.2f}"%(idx,sum_count) + ','

def gene_station_info():
    station_info = []
    station_list = ['南湖支路', '南坪中学后门', '绿洲龙城', '南坪南路', '大礼堂', '两江幸福广场']
    staus = ['正常', '拥挤', '满载']
    station_conut = [[991,671],[843,890],[235,301],[1092,888],[666,555],[555,333],[1111,943]]
    for i in range(len(station_list)):
        station_info.append({
            'name':station_list[i],
            'staus': random.choice(staus),
            'up': gene_station_dis(max=station_conut[i][0]),
            'down':gene_station_dis(max=station_conut[i][1])
        })
    with open('staion_monitor.json','w') as f:
        f.write(json.dumps(station_info,ensure_ascii=False,indent=1))

def gene_bus_station_info():
    info_list = [
                       0,
                       0,
                       0,
                       0,
                       0,
                       0,
                       23,
                       57,
                       75,
                       80,
                       72,
                       60,
                       59,
                       55,
                       58,
                       56,
                       61,
                       72,
                       75,
                       71,
                       55,
                       55,
                       0,
                       0
                      ]


    for idx, count in enumerate(info_list):
        print "{ x: '%d时', y: %d }" % (idx, count) + ','
        sum_count = 0
    for idx, count in enumerate(info_list):
        sum_count += count
        print "{ x: '%d时', y: %d }" % (idx, sum_count) + ','

def gene_unit_info():
    unit_info = []
    unit_list = [
                 "渝中组团",
                 "鱼嘴组团",
                 "西永组团",
                 "西彭组团",
                 "唐家沱组团",
                 "水土组团",
                 "沙坪坝组团",
                 "人和组团",
                 "南坪组团",
                 "李家沱组团",
                 "礼嘉组团",
                 "空港组团",
                 "界石组团",
                 "观音桥组团",
                 "大杨石组团",
                 "大渡口组团",
                 "茶园组团",
                 "蔡家组团",
                 "北碚组团"
                ]
    living_count = [0.75, 0.68,0.82,0.78,0.69,0.35,0.67,0.42,0.68,0.65,0.42,0.77,0.55,0.68,0.68,0.63,0.66,0.34,0.81]
    params = [1.2,0.8,0.6,0.55,0.49,0.3,1.1,1.2,0.9,0.8,0.7,0.6,0.4,1.5,0.6,0.66,0.8,0.4,1]
    for i,unit in enumerate(unit_list):
        unit_info.append({
            'name':unit,
            'value':[0,0,0,0,0,0] + [round(random.uniform(seed[0], seed[1]),2)*params[i] for seed in seed_list][6:22]+[0,0],
            'prop':living_count[i]
        })
    with open('unit_dis.json', 'w') as f:
        f.write(json.dumps(unit_info, ensure_ascii=False, indent=1))

# gene_car_count()
# gene_car_speed()
# gene_lag_time()
# gene_traff_index()
# print gene_station_dis(max=650)
# print sum(gene_station_dis(max=650))
# gene_station_info()
# gene_unit_info()
gene_taxi_speed()
# gene_bus_station_info()
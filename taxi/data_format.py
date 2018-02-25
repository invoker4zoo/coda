# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: data_format
@ time: 18-2-6
"""
import os
BASE_PATH = '/mnt/coda/运管局--出租车/出租车GPS-201703/07'
data_list = os.listdir(BASE_PATH)
for data_file in data_list:
    with open(os.path.join(BASE_PATH,data_file),'r') as f:
        first_line = f.readline()
        _char = first_line.split(',')[3][0:2]
        total = f.read()
        _total = total.replace(_char,'')
        with open(os.path.join(BASE_PATH, data_file), 'w') as g:
            print 'copy taxi from ' + "'" + os.path.join(BASE_PATH, data_file) + "'" + " with delimiter ',';"
            g.write(_total)
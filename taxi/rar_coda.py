# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: rar_coda
@ time: 18-2-6
"""
import os


# PATH = '/mnt/coda/运管局--出租车/出租车GPS-201703'
# file_list = os.listdir(PATH)
# for file in file_list:
#     if file.endswith('.rar'):
#         os.system('cd '+ PATH + '|rar x ' + file)
list = range(4,32)
command = ''
for item in list:
    if item <10:
        command+= 'rar x 0'+ str(item) + '.rar&&'
    else:
        command += 'rar x ' + str(item) + '.rar&&'
print command
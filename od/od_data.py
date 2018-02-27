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
region_list = ['巴南区','北碚区',	'大渡口区','江北区','九龙坡区','南岸区','沙坪坝区','渝北区','渝中区']

import xlrd
table = xlrd.open_workbook('主城OD.xls').sheets()[0]
for row in range(0,9):
  for col in range(0,9):
      print int(table.cell(row,col).value)

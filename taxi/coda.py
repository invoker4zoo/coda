# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: coda
@ time: 18-2-6
"""
from psycopg2.pool import  ThreadedConnectionPool
from singleton import Singleton
from psycopg2.extras import DictCursor, RealDictCursor
import sys
import os

class PgUtil():
    __metaclass__ = Singleton

    def __init__(self):
        self.conn_pool = ThreadedConnectionPool(
            minconn=4,
            maxconn=100,
            database='coda',
            user='postgres',
            password='1qaz2wsx',
            host='127.0.0.1',
            port=5432
        )

    def get_conn(self):
        conn = self.conn_pool.getconn()
        return conn

    def put_conn(self, conn):
        self.conn_pool.putconn(conn)

    def execute_insert_sql(self, sql, values):
        conn = self.get_conn()
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(sql,values)
        cur.close()
        conn.commit()
        self.put_conn(conn)

BASE_PATH = '/mnt/coda/运管局--出租车/出租车GPS-201703/'
file_list = os.listdir(BASE_PATH)
# print file_list
pg = PgUtil()
# PATH = '/mnt/coda/运管局--出租车/出租车GPS-201703/01'
INSERT_SQL = """
              INSERT INTO taxi(
              data_date,
              gps_time,
              taxi_char,
              taxi_id,
              longitude,
              latitude,
              speed,
              otientation,
              status,
              useful
              )  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
             """
# file_list = os.listdir(BASE_PATH)
# for file in file_list:
#     if file.endswith('.rar'):
#         pass
#     else:
#         PATH = os.path.join(BASE_PATH, file)
#         data_list = os.listdir(PATH)
#         for data_file in data_list:
#             with open(os.path.join(PATH,data_file), 'r') as f:
#                 for line in f.readlines():
#                     print line
#                     data = line.split(',')
#                     insert_data = (data[0],data[1],data[2],data[3][2:],float(data[4]),float(data[5]),float(data[6]),float(data[7]),int(data[8]),int(data[9].strip()))
#                     pg.execute_insert_sql(INSERT_SQL,insert_data)
PATH = os.path.join(BASE_PATH, '01')
data_list = os.listdir(PATH)
for data_file in data_list:
    with open(os.path.join(PATH, data_file), 'r') as f:
        for line in f.readlines():
            print line
            data = line.split(',')
            insert_data = (
            data[0], data[1], data[2], data[3][2:], float(data[4]), float(data[5]), float(data[6]), float(data[7]),
            int(data[8]), int(data[9].strip()))
            pg.execute_insert_sql(INSERT_SQL, insert_data)
# coding=utf-8
"""
@ license: Apache Licence
@ github: invoker4zoo
@ author: invoker/cc
@ wechart: whatshowlove
@ software: PyCharm
@ file: db_tool
@ time: 18-2-7
"""
from psycopg2.pool import  ThreadedConnectionPool
# from singleton import Singleton
from psycopg2.extras import DictCursor, RealDictCursor
import sys
import os

class PgUtil():
    # __metaclass__ = Singleton

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

    def query_all_sql(self, sql):
        conn = self.get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql)
        result_list = []
        for row in cur.fetchall():
            result_list.append(row)
        conn.commit()
        self.put_conn(conn)
        return result_list

    def query_one_sql(self, sql):
        conn = self.get_conn()
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.commit()
        self.put_conn(conn)
        return dict(row) if row else {}

    def execute_sql(self, sql):
        conn = self.get_conn()
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(sql)
        cur.close()
        conn.commit()
        self.put_conn(conn)

    def select_sql(self, sql, values):
        conn = self.get_conn()
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(sql, values)
        res = cur.fetchone()
        cur.close()
        conn.commit()
        self.put_conn(conn)
        return res

    def select_all_sql(self, sql, values):
        conn = self.get_conn()
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(sql, values)
        res = cur.fetchall()
        cur.close()
        conn.commit()
        self.put_conn(conn)
        return res

    def execute_update_sql(self, sql, values):
        conn = self.get_conn()
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(sql, values)
        cur.close()
        conn.commit()
        self.put_conn(conn)
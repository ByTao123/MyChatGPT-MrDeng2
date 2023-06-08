import pymysql
from pymysql.cursors import DictCursor
from dbutils.pooled_db import PooledDB


class MySQLPool:
    """
    数据访问类，使用连接池进行数据库操作
    """

    config = {
        'host': 'rm-bp1g52e6iz58p6204ho.mysql.rds.aliyuncs.com',
        'port': 3306,
        'username': 'chatgpt',
        'password': 'chatgpt888@',
        'database': 'gpt'
    }

    pool = PooledDB(
        creator=pymysql,
        maxconnections=5,  # 连接池最大连接数
        host='rm-bp1g52e6iz58p6204ho.mysql.rds.aliyuncs.com',
        port=3306,
        user='chatgpt',
        password='chatgpt888@',
        database='gpt',
        cursorclass=DictCursor
    )

    @classmethod
    def execute_query(cls, sql, *args):
        """
        查询数据
        """
        conn = cls.pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        return result

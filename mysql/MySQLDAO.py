from MySQLPool import MySQLPool


class MyDAO:
    """
    数据访问类，使用连接池进行数据库操作
    """

    config = {
        'host': 'rm-bp1g52e6iz58p6204ho.mysql.rds.aliyuncs.com',
        'port': 3306,
        'user': 'chatgpt',
        'password': 'chatgpt888@',
        'database': 'gpt'
    }

    pool = MySQLPool(**config)

    @classmethod
    def execute_query(cls, sql, *args):
        """
        查询数据
        """
        result = cls.pool.execute_query(sql, args)
        return result

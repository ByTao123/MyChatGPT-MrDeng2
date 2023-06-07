import pymysql
from pymysql.cursors import DictCursor
from pymysql import Error


class MySQLPool:
    """
    MySQL连接池类
    """

    def __init__(self, host, port, username, password, database, pool_name="mypool", pool_size=10):
        """
        初始化连接池
        :param host: MySQL服务器地址
        :param port: MySQL端口号
        :param username: MySQL用户名
        :param password: MySQL密码
        :param database: 数据库名称
        :param pool_name: 连接池名称
        :param pool_size: 连接池大小
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.pool_name = pool_name
        self.pool_size = pool_size
        self.pool = None

        self._create_pool()

    def _create_pool(self):
        """
        创建连接池
        """
        try:
            self.pool = pymysql.pool.PersistentDB(
                creator=pymysql,
                maxusage=None,
                # 连接池大小
                maxconnections=self.pool_size,
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                charset="utf8mb4",
                cursorclass=DictCursor,
                autocommit=True
            )
        except Error as e:
            print("Error while connecting to MySQL using connection pool", e)

    def execute_query(self, query, *args):
        """
        执行查询语句并返回结果
        :param query: 查询语句
        :param args: 查询参数
        :return: 查询结果元组
        """
        connection = self.pool.connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                result = cursor.fetchall()
                return tuple(result)
        except Error as e:
            print("Error while executing MySQL query", e)
        finally:
            if connection is not None:
                connection.close()

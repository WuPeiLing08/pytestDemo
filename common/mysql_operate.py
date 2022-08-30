import pymysql
import os
from common.read_data import data
from common.logger import log

setting_file = os.path.join(os.path.dirname(os.path.dirname(__name__)), "config", "setting.ini")
data = data.load_ini(setting_file).get("mysql")

DB_CONF = {
    "host": data["host"],
    "port": data["port"],
    "name": data["name"],
    "password": data["password"],
    "database": data["db"]
}


class Mysqldb:
    def __init__(self):
        # autocommit=True 每次执行sql后，都自动commit
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # python回收对象时，会执行__del__方法
        self.cursor.close()
        self.conn.close()

    def select_db(self, query_sql):
        """查询"""
        try:
            # 检查连接是否断开，断开就重连
            self.conn.ping()
            self.cursor.execute(query_sql)
            query_data = self.cursor.fetchall()
            return query_data
        except Exception as e:
            log.error("执行sql查询出错，错误信息:{}".format(e))

    def execute_db(self, execute_sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，断开就重连
            self.conn.ping()
            self.cursor.execute(execute_sql)
            self.conn.commit()
        except Exception as e:
            log.error("执行sql出错，错误信息:{}".format(e))
            self.conn.rollback()






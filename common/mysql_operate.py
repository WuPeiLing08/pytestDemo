import pymysql
import os
from common.read_data import data

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
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def select_db(self):
        pass

    def execute_db(self):
        pass





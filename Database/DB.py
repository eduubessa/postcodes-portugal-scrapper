from Database.MySql import MySql
from App.Helpers.Config import Config
from Database.SqlServer import SqlServer

class DB:

    __driver = None

    def __init__(self):
        self.__driver = Config.get('database.driver')
        if self.__driver == "mysql":
            self.__database = MySql()
        elif self.__driver == "sqlserve":
            self.__database = MySql()
        else:
            self.__database = MySql()

    def table(self, table):
        self.__database.table(table)
        return self

    def insert(self, data):
        return self.__database.insert(data)


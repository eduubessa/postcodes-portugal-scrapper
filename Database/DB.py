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

    def select(self, columns = '*'):
        self.__query = self.__database.select(columns);
        return self

    def where(self, field, value, condition = "LIKE"):
        self.__query = self.__query.where(field, value, condition)
        return self

    def orderBy(self, field, order = "ASC"):
        self.__query = self.__query.orderBy(field, order)
        return self

    def get(self):
        return self.__query.fetchall()

    def all(self):
        return self.__database.select().fetchall()

    def first(self):
        return self.__query.fetchone()

    def last(self):
        return self.__query.orderBy('id', 'DESC').fetchone()

    def insert(self, data):
        return self.__database.insert(data)

    def update(self, data):
        self.__query = self.__query.update(data)


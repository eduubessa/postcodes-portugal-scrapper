import pymysql.cursors
from App.Helpers.Config import Config


class MySql:


    __connection = None
    __table = None
    __sql = None
    __values = []

    def __init__(self):
        try:
            self.__connection = pymysql.connect(port=Config.get('database.port', 3306),
                                                host=Config.get('database.host', 'localhost'),
                                                user=Config.get('database.username', 'root'),
                                                password=Config.get('database.password', ''),
                                                database=Config.get('database.database'),
                                                cursorclass=pymysql.cursors.DictCursor)
        except Exception as ex:
            print("MySql Connection Error:")
            print(ex)

    def table(self, table):
        self.__table = table
        return self

    def insert(self, data):
        values = []

        try:
            if self.__table is None:
                raise ValueError("No table selected, use table method first")
            with self.__connection:
                with self.__connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `{}` (".format(self.__table)

                    for i, x in enumerate(data):
                        sql += "`{}`".format(x[0])
                        if i < len(data) - 1:
                            sql += ", "

                    sql += ") VALUES ("

                    for i, y in enumerate(data):
                        sql += "%s"
                        values.append(y[1])
                        if i < len(data) - 1:
                            sql += ", "

                    sql += ");"

                    cursor.execute(sql, values)
                    self.__connection.commit()

                with self.__connection.cursor() as cursor:
                    # Read a new record
                    sql = "SELECT * FROM `{}` ORDER BY `id` DESC;".format(self.__table)
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    print(row)
        except Exception as ex:
            print("MySql Error Insert")
            print(ex)

    def update(self, data):
        values = []

        try:
            if self.__table is None:
                raise ValueError("No table selected, use table method first")
            with self.__connection:
                with self.__connection.cursor() as cursor:
                    if "WHERE" in self.__sql:
                        # Create a new record
                        sql = "UPDATE `{}` SET ".format(self.__table)

                        for i, x in enumerate(data):
                            sql += "`{}` = %s".format(x[0])
                            values.append(x[1])
                            if i < len(data) - 1:
                                sql += ", "

                        sql += self.__sql.replace("SELECT * FROM `{}`".format(self.__table), "")
                        return self
                    else:
                        raise ValueError("You need WHERE method first")
        except Exception as ex:
            print("MySql Error Update")
            print(ex)

    def select(self, columns = '*'):
        try:
            if self.__table is None:
                raise ValueError("No table selected, use table method first")
            self.__sql = "SELECT {} FROM `{}`".format(columns, self.__table)
            return self
        except Exception as ex:
            print(ex)

    def where(self, field, value, condition="LIKE"):
        try:
            if self.__table is None:
                raise ValueError("No table selected, use table method first")

            if "SELECT" in self.__sql or "UPDATE" in self.__sql or "DELETE" in self.__sql:
                if "WHERE" in self.__sql:
                    self.__sql += " AND {0}".format(field)
                else:
                    self.__sql += " WHERE {0}".format(field)

                if condition == "LIKE" or condition == "=":
                    if isinstance(value, int) or isinstance(value, float):
                        self.__sql += " = %s"
                    else:
                        self.__sql += " LIKE %s"
                elif condition == "NOT LIKE" or condition == "!=":
                    if isinstance(value, int) or isinstance(value, float):
                        self.__sql += " != %s"
                    else:
                        self.__sql += "NOT LIKE %s"
                else:
                    self.select().where(field, value, condition)
                self.__values.append(value)
                return self
            else:
                raise ValueError("Where working only select, update and delete")
        except Exception as ex:
            print("MySql Where Error")
            print(ex)

    def orderBy(self, field, order = 'ASC'):
        if "SELECT" in self.__sql:
            self.__sql += " ORDER BY {} {}".format(field, order)
        return self

    def fetchone(self):
        print(self.__sql)
        with self.__connection.cursor() as cursor:
            # Read single record
            cursor.execute(self.__sql, self.__values)
            row = cursor.fetchone()
            return row

    def fetchall(self):
        with self.__connection.cursor() as cursor:
            # Read fetch all rows
            cursor.execute(self.__sql, self.__values)
            rows = cursor.fetchall()
            self.__values = []
            print(self.__values)
            return rows

    def __del__(self):
        self.__values = []

import pymysql.cursors
from App.Helpers.Config import Config

class MySql:

    __connection = None
    __table = None
    __sql = None

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
                        if i < len(data)-1:
                            sql += ", "

                    sql += ") VALUES ("

                    for i, y in enumerate(data):
                        sql += "%s"
                        values.append(y[1])
                        if i < len(data)-1:
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
            print("Error MySql Insert:")
            print(ex)
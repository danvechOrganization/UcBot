import sqlite3


class Database:

    def __init__(self, path = "codes.db"):
        self.path = path

    @property
    def connection(self):
        return sqlite3.connect(self.path)

    def execute(self, sql:str, parameters:tuple=None, fetchone:bool=False, fetchall:bool=False):
        data = None

        connection = self.connection
        cursor = connection.cursor()
        if(parameters == None):
            cursor.execute(sql)
        else:
            cursor.execute(sql, parameters)

        if(fetchone):
            data = cursor.fetchone()

        if(fetchall):
            data = cursor.fetchall()

        cursor.close()
        connection.commit()
        connection.close()

        return data

    def create_table(self):
        sql1 = "CREATE TABLE IF NOT EXISTS CODES (id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT NOT NULL, IsUse BOOL NOT NULL)"
        sql2 = "CREATE TABLE IF NOT EXISTS ACCOUNTS (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT NOT NULL, pass TEXT NOT NULL)"

        self.execute(sql1)
        self.execute(sql2)


    def delete_codes(self):
        sql = "DELETE FROM CODES WHERE IsUse=True"

        self.execute(sql)
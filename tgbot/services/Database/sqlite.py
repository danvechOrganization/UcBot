import sqlite3


class Database:

    def __init__(self, path = "codes.db"):
        self.path = path

    @property
    def connection(self):
        return sqlite3.connect(self.path)

    def execute(self, sql:str, fetchone:bool=False, fetchall:bool=False, commit:bool=True):
        data = None

        cursor = self.connection.cursor()
        cursor.execute(sql)

        if(commit):
            self.connection.commit()

        if(fetchone):
            data = cursor.fetchone()

        if(fetchall):
            data = cursor.fetchall()

        self.connection.close()
        return data

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS CODES (id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT NOT NULL, IsUse BOOL NOT NULL)"

        self.execute(sql)

    def delete_codes(self):
        sql = "DELETE FROM CODES WHERE IsUse=True"

        self.execute(sql)
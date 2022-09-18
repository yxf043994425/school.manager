import sqlite3

class DbSqlite:
    _conn = None

    def __init__(self, database):
        self._conn = sqlite3.connect(database)

    def create(self, sql):
        cursor = self._conn.cursor()
        cursor.execute(sql)
        cursor.close()

    def select(self, sql, args = []):
        cursor = self._conn.cursor()
        cursor.execute(sql, args)
        data = cursor.fetchall()
        cursor.close()
        return data
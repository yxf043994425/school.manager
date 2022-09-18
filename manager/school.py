from utils import db
from utils import excel

class School:

    _database = None

    def __init__(self):
        self._database = db.DbSqlite('./db/school.db')

    def init_table(self):
        self._database.create('''
            CREATE TABLE IF NOT EXISTS school_teacher
            (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                name     TEXT,
                group_id INTEGER
            );
        ''')
        self._database.create('''
            CREATE TABLE IF NOT EXISTS school_group
            (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT
            );
        ''')
        self._database.create('''
            CREATE TABLE IF NOT EXISTS school_class
            (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT
            );
        ''')
        print("init table success!")

    def init_teacher(self):
        book = excel.ExcelWings('./data/全教职工名单.xls')
        result = book.range(0, 'B3:B98')
        print(result)

    

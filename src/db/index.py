import sqlite3


class Database:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    is_done INTEGER NOT NULL,
                    date TEXT NOT NULL
                )
            ''')

    def execute(self, query, *args):
        with self.conn:
            return self.conn.execute(query, args)

    def __del__(self):
        self.conn.close()

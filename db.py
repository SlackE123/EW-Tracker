import sqlite3

class Database:
    def __init__(self, url):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS ew (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                subject TEXT NOT NULL,
                beak TEXT NOT NULL,
                dueDate DATE NOT NULL
            );
            """
            cursor.execute(sql)

            sql_insert = """
            INSERT INTO ew (task, subject, beak, dueDate) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, ('Stupid long ew', 'Computer Science', 'MC', '2024-10-09'))
            db.commit()


    def get_ews(self):
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            sql = """
            SELECT id, task, subject, beak, dueDate FROM ew
            """
            cursor.execute(sql)
            
            return cursor.fetchall()

    def create_ew(self, task, subject, beak, dueDate):

        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            sql = """
            INSERT INTO ew (task, subject, beak, dueDate)
            VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql, (task, subject, beak, dueDate))
            db.commit()

        


    # EXTRA CREDIT
    def get_ew(self, id):
        """
        TO IMPLEMENT
        """
        pass

import sqlite3

class BD:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        ''')
        self.connection.commit()

    def get_user(self, username):
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone()

    def create_user(self, username, password):
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.connection.commit()

    def close(self):
        self.connection.close()

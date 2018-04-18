import sqlite3, time, json

class database():
    def __init__(self):
        self.db = sqlite3.connect("./database.db")
    def is_user(self, username):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM `users` WHERE `username`=?", (username,))
        row = cursor.fetchone()

        if row is None:
            return False
        else: 
            return True
    def get_user_info(self, username):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM `users` WHERE `username`=?", (username,))
    def register_user(self, username, password):
        pass
    def get_user_posts(self, username):
        pass

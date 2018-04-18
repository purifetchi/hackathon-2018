import sqlite3, time, json, hashlib

class Database():
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
        
        row = cursor.fetchone()

        if row is None:
            return None
        else: 
            return {"username":row[0], "password":row[1], "avatar":row[2], "follows":row[3]}
    def register_user(self, username, password):
        cursor = self.db.cursor()
        passwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, passwd))
        if cursor.rowcount > 0:
            self.db.commit()
            return True
        else:
            self.db.commit()
            return False

    def auth_user(self, username, password):
        cursor = self.db.cursor()
        passwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if cursor.fetchone() is None:
            return True
        else:
            return False    

    def get_user_posts(self, username):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM `posts` WHERE `author`=?", (username,))
        
        row = cursor.fetchall()

        if row is None:
            return None
        else: 
            return row

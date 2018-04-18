import sqlite3, time, json

class database():
    def __init__(self):
        self.db = sqlite3.connect("./database.db")

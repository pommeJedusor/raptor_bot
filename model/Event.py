import sqlite3


class Event:
    def __init__(self, id:int, name: str, description: str, date: int):
        self.id = id
        self.name = name
        self.description = description
        self.date = date

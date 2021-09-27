import sqlite3
from Parlor import Parlor
from Building import Building
class ALL:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getALL(self):
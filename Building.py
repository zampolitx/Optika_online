import sqlite3
from Parlor import Parlor
class Building:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getBuilding(self):
        my_dbase = Parlor(self.__db)
        sql = """SELECT * FROM building"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                d = {}
                for i in res:                   #Для каждой строки, извлеченной из БД
                    d[i[1]] = my_dbase.getParlor(i[0])      # d{'Корпус1':[
                return d
        except:
            print("Ошибка чтения базы данных")
        return [1]

    def addBuilding(self, building_name):
        try:
            self.__cur.execute("INSERT INTO building(title) VALUES(?)", (building_name, ))
            self.__db.commit()
            print(building_name)
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]
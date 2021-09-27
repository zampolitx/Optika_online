import sqlite3
from Parlor import Parlor
class Building:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getBuilding(self, build_name=False):
        my_dbase = Parlor(self.__db)
        sql_all = """SELECT * FROM building"""
        sql_some = "SELECT id FROM building where title = ?"
        if build_name:  # Если указано название здания, возвращаем его id
            try:
                self.__cur.execute(sql_some, (build_name, ))
                res = self.__cur.fetchall()
                print(res[0][0])
                if res:
                    return res[0][0]
            except:
                print("Ошибка чтения базы данных ALL==False")
            return False
        else:   # Если не указано название здания, возвращаем список зданий
            try:
                self.__cur.execute(sql_all)
                res = self.__cur.fetchall()     # Получаем список строк из БД
                if res:
                    return res
            except:
                print("Ошибка чтения базы данных ALL==False")
            return False

    def addBuilding(self, building_name):
        try:
            self.__cur.execute("INSERT INTO building(title) VALUES(?)", (building_name, ))
            self.__db.commit()
            print(building_name)
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД : "+str(e))
        return [1]
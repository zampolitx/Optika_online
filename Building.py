import sqlite3
from Parlor import Parlor
class Building:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getBuilding(self, build_name=False, ALL=False):
        my_dbase = Parlor(self.__db)
        sql_all = """SELECT * FROM building"""
        sql_some = "SELECT id FROM building where title = ?"
        if ALL==False:
            #print(build_name)
            try:
                self.__cur.execute(sql_some, (build_name, ))
                res = self.__cur.fetchall()
                print(res[0][0])
                if res:
                    return res[0][0]
            except:
                print("Ошибка чтения базы данных ALL==False")
            return False
        elif ALL==True and build_name==False:
            try:
                self.__cur.execute(sql_all)
                res = self.__cur.fetchall()
                print(res[0][0])
                if res:
                    return res[0][0]
            except:
                print("Ошибка чтения базы данных ALL==False")
            return False
        else:
            try:
                self.__cur.execute(sql_all)
                res = self.__cur.fetchall()
                if res:
                    d = {}
                    for i in res:                   #Для каждой строки, извлеченной из БД
                        d[i[1]] = my_dbase.getParlor(building_id=i[0], ALL=True, parlor_id=False)      # d{'Корпус1':[
                    return d
            except:
                print("Ошибка чтения базы данных ALL==True")
            return [1]

    def addBuilding(self, building_name):
        try:
            self.__cur.execute("INSERT INTO building(title) VALUES(?)", (building_name, ))
            self.__db.commit()
            print(building_name)
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД : "+str(e))
        return [1]
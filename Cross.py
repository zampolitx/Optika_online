import sqlite3
from Cable import Cable
class Cross:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getCross(self, panel_id, ALL=False):
        my_dbase = Cable(self.__db)
        sql_some = "SELECT * FROM fiber_cross where panel_id = ?"
        sql_all = "SELECT * FROM fiber_cross where panel_id = ?"
        if ALL==False:
            try:
                self.__cur.execute(sql_some, (panel_id, ))
                res = self.__cur.fetchall()
                if res:
                    l = []
                    for elem in res:
                        p = dict(title=elem[2], number=elem[1], child=my_dbase.getCable(elem[0]))
                        l.append(p)
                    return l
            except:
                print("Ошибка чтения базы данных")
            return [1]
        else:
            try:
                self.__cur.execute(sql_all, (panel_id, ))
                res = self.__cur.fetchall()
                if res:
                    l = []
                    for elem in res:
                        p = dict(title=elem[2], number=elem[1], child=my_dbase.getCable(elem[0]))
                        l.append(p)
                    return l
            except:
                print("Ошибка чтения базы данных")
            return [1]
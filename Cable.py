import sqlite3
from Fiber import Fiber
class Cable:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getCable(self, fiber_cross_id, ALL=False):
        my_dbase = Fiber(self.__db)
        sql = "SELECT * FROM cable where fiber_cross_id = ?"
        try:
            self.__cur.execute(sql, (fiber_cross_id, ))
            res = self.__cur.fetchall()
            if res:
                l = []
                for elem in res:
                    p = dict(title=elem[2], number=elem[3], child=my_dbase.getFiber(elem[0], ALL=True))
                    l.append(p)
                return l
        except:
            print("Ошибка чтения базы данных cable.py")
        return [1]
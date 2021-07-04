from Fiber import Fiber
class Cable:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getCable(self, cross_id):
        my_dbase = Fiber(self.__db)
        sql = "SELECT * FROM cable where cross_id = ?"
        try:
            self.__cur.execute(sql, (cross_id, ))
            res = self.__cur.fetchall()
            if res:
                p = {}
                for elem in res:
                    p[elem[1]] = my_dbase.getFiber(elem[0])
                return p
        except:
            print("Ошибка чтения базы данных")
        return [1]
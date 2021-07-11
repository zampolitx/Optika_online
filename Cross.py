from Cable import Cable
class Cross:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getCross(self, panel_id):
        my_dbase = Cable(self.__db)
        sql = "SELECT * FROM fiber_cross where panel_id = ?"
        try:
            self.__cur.execute(sql, (panel_id, ))
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
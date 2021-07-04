from Cross import Cross
class Panel:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getPanel(self, parlor_id):
        my_dbase = Cross(self.__db)
        sql = "SELECT * FROM panel where parlor_id = ?"
        try:
            self.__cur.execute(sql, (parlor_id, ))
            res = self.__cur.fetchall()
            if res:
                p = {}
                for elem in res:                   #Для каждой строки, извлеченной из БД
                    p[elem[1]] = my_dbase.getCross(elem[0])
                print(p)
                return p
        except:
            print("Ошибка чтения базы данных")
        return [1]
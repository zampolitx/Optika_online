class Parlor:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getParlor(self, id, title):
        sql="""SELECT * FROM parlor where building_id = '1'"""
        try:
            self.__cur.execute(sql)
            res=self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения базы данных")
        return [1]

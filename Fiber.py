class Fiber:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getFiber(self, cable_id, ALL=False):
        sql = "SELECT * FROM fiber where cable_id = ?"
        try:
            self.__cur.execute(sql, (cable_id, ))
            res = self.__cur.fetchall()
            if res:
                l = []
                for elem in res:                   #Для каждой строки, извлеченной из БД
                    p = dict(id=elem[0], number=elem[1], title=elem[2], num_of_conn=elem[3], type_of_conn=elem[4], cable_id=elem[5])
                    l.append(p)
                return l
        except:
            print("Ошибка чтения базы данных Fiber.py")
        return [1]
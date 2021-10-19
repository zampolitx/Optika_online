import sqlite3

class Unit:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getUnit(self, panel_id, unit_id):
        #my_dbase = Panel(self.__db)
        sql_all = "SELECT * FROM unit where panel_id = ?"   # Все юниты в этой панели
        sql_one = "SELECT * FROM unit where id = ?"
        if panel_id:
            try:
                self.__cur.execute(sql_all, (panel_id, ))
                res = self.__cur.fetchall()
                if res:
                    unit_list = []
                    for elem in res:
                        p = dict(id=elem[0], number=elem[1], panel_id=elem[2])
                        unit_list.append(p)
                    return unit_list
            except:
                print("Ошибка чтения базы данных для unit=panel_id", panel_id)
            return ['']
        elif unit_id:
            print("id in BD is", unit_id)
            try:
                self.__cur.execute(sql_one, (unit_id, ))
                res = self.__cur.fetchall()
                print(res)
                if res:
                    for elem in res:
                        print(elem[1])
                        p=dict(number=elem[1], title=elem[2], length=elem[3], width=elem[4], height=elem[5])
                    return p
            except:
                print("Ошибка чтения базы данных для parlor 2")
            return ['']

    def addUnit(self, panel_id, numOfUnits):       # numOfUnits - количество юнитов, введенное в процессе создания панели
        try:
            #self.__cur.execute("SELECT id FROM building WHERE title=?", (parent_item,))        # из таблицы building получить id записи из чекбокса
            #res = self.__cur.fetchall()
            #for elem in res:
            #    print(elem[0])      # в elem[0] находится id здания/территории куда добавляем кабинет
            for i in range(int(numOfUnits)*2, 0, -1):   # в бд добавляем количество юнитов умноженное на два (спереди и сзади)
                print(i)
                self.__cur.execute("INSERT INTO unit(number, panel_id) VALUES(?, ?)", (i, panel_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления записи в БД: "+str(e))
        return [1]
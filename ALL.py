import sqlite3
from Building import Building
from Parlor import Parlor
# Должна получиться такая структура:
# {'Корпус1': [{'id': 1, 'title': 'ПСВ-и', 'number': 'КП-2', 'child': [1]}, {'id': 2, 'title': 'Серверная 2 этаж', 'number': '102', 'child': [{'title': 'Панель оптических штук1', 'number': '5Р7', 'child': [{'title': 'Оптический Кросс', 'number': '1', 'child': [{'title': 'Опт. кабель', 'number': 'ДПМ-24-ММ', 'child': [{'id': 1, 'number': '1', 'title': 'Moxa11111111111111122222222222', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 2, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 3, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 4, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 5, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 6, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 7, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 8, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 9, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}, {'id': 10, 'number': '1', 'title': 'Moxa1', 'num_of_conn': '1', 'type_of_conn': 'LC', 'cable_id': 1}]}]}, {'title': 'Оптический Кросс', 'number': '2', 'child': [1]}]}, {'title': 'Панель оптических штук1', 'number': '5Р7', 'child': [{'title': 'Оптический Кросс', 'number': '3', 'child': [1]}]}, {'title': 'Панель оптических штук2', 'number': '5Р7', 'child': [{'title': 'Оптический Кросс', 'number': '4', 'child': [1]}]}, {'title': 'Панель оптических штук2', 'number': '5Р7', 'child': [{'title': 'Оптический Кросс', 'number': '5', 'child': [1]}]}, {'title': 'Панель оптических штук3', 'number': '5Р7', 'child': [{'title': 'Оптический Кросс', 'number': '6', 'child': [1]}]}]}]}

class ALL:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getALL(self):
        my_dbase = Parlor(self.__db)
        sql_all = """SELECT * FROM building"""
        try:
            self.__cur.execute(sql_all)
            res = self.__cur.fetchall()
            #print(res)
            if res:
                d = {}
                for i in res:  # Для каждой строки, извлеченной из БД
                    d[i[1]] = my_dbase.getParlor(building_id=i[0], ALL=True, parlor_id=False)  # d{'Корпус1':[
                return d
        except:
            print("Ошибка чтения базы данных ALL==False")
        return False
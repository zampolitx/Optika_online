from flask import Flask, render_template, request, flash, g, url_for, json, jsonify
import sqlite3, os, re, json
from FDataBase import FDataBase
from Building import Building
from Parlor import Parlor
from Panel import Panel
# Конфигурация приложения
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = ';askldjfa;skdljfas;kldfj'
# Конец конфигурации
app = Flask(__name__)
app.config.from_object(__name__)                                                # Загружаем конфигурацию из текущего модуля
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))      # Переопределяем путь к БД
# Функция подключения к БД
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn
# Функция для создания БД
def create_db():
    db=connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db

@app.route("/")
def index():
    db = get_db()
    dbase=FDataBase(db)                 #FDataBase - это класс, dbase - экземляр класса FDataBase
    mydbase=Building(db)
    building2=mydbase.getBuilding(build_name=False, ALL=True)       # Возвращает коллекцию из словарей

    return render_template('index.html', title="Optika-главная", menu=dbase.getMenu(), building=building2)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        if len(request.form['add_items']) > 2:  # Отображение подсказок
            flash('Данные отправлены', category='success')
        else:
            flash('Слишком короткое имя', category='error')
        #print(request.form)
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add.html', title="Optika-add", menu=dbase.getMenu(), add_items=dbase.getItems())

@app.route("/add_building", methods=['GET', 'POST'])
def add_building():
    db = get_db()
    dbase=FDataBase(db)
    Buld_base=Building(db)
    if request.method == "POST":
        if len(request.form['building_name']) > 1:  # Отображение подсказок
            flash('Данные отправлены', category='success')
        else:
            flash('Слишком короткое имя', category='error')
        Buld_base.addBuilding(request.form['building_name'])
    return render_template('add_building.html', title="Добавить здание", menu=dbase.getMenu())

@app.route("/add_room", methods=['GET', 'POST'])
def add_room():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Parlor(db)
    parent_item = []                                                          # Пустой список (в него далее добавляем из БД здания и территории предприятия)
    for d in dbase.getBuilding():                                           # В d находятся строки из БД с зданиями
        parent_item.append(d[1])                                              # Список далее передаем на страницу add_room в качестве родителя для комнаты или участка
    if request.method == "POST":
        print(request.form)
        if len(request.form['room_name']) > 1:                          # Отображение подсказок
            res = Par_base.addParlor(request.form['parent_item'], request.form['room_name'], request.form['room_number'])
            if not res:
                flash('Ошибка', category='error')
            else:
                flash('Нет ошибки', category='success')
    return render_template('add_room.html', title="Добавить помещение", menu=dbase.getMenu(), parent_item=parent_item)

@app.route("/add_panel", methods=['GET', 'POST'])
def add_panel():
    db = get_db()
    dbase = FDataBase(db)
    Par_base = Panel(db)
    Build_base = Building(db)
    parent_building = []
    for d in Build_base.getBuilding():
        parent_building.append(d)
    if request.method == "POST":
        print(request.form)
        if len(request.form['panel_name']) > 1:
            res = Par_base.addPanel(request.form['parent_parlor'], request.form['panel_name'], request.form['panel_number'], request.form['units_number'])
            if not res:
                flash('Ошибка', category='error')
            else:
                flash('Добавлено', category='success')
    return render_template('add_panel.html', title="Добавить панель", menu=dbase.getMenu(), parent_building=parent_building)

@app.route("/add_cross", methods=['GET', 'POST'])
def add_cross():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        print(request.form)
    return render_template('add_cross.html', title="Добавить кросс", menu=dbase.getMenu())

@app.route("/add_cable", methods=['GET', 'POST'])
def add_cable():
    if request.method == "POST":
        print(request.form)
    return render_template('add_cable.html', title="Добавить кабель", menu=menu)

@app.route("/add_opt_coupler", methods=['GET', 'POST'])
def add_opt_coupler():
    if request.method == "POST":
        print(request.form)
    return render_template('add_opt_coupler.html', title="Добавить муфту", menu=menu)

@app.route("/find")
def find():
    return render_template('find.html', title="Optika-find", menu=menu)

@app.route("/proba", methods=['GET', 'POST'])
def proba():
    return render_template('proba.html')

@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    print(request.form)
    name = request.form['parent_building']
    return json.dumps({'len': len(name)})

# Обработчик функции AJAX add_panel.js
@app.route('/get_parlor', methods=['GET', 'POST'])
def get_parlor():
    #print(request.form)
    par_building = request.form['parent_building']  #Из js получаем название здания, в котором находится кабинет
    db = get_db()
    mydbase = Building(db)
    building_id = mydbase.getBuilding(par_building)  # Обращаемся к БД и получаем id здания, в котором находится кабинет
    mydbase_par = Parlor(db)
    parlor_list = mydbase_par.getParlor(building_id)
    return json.dumps({'par_buld_resp': parlor_list})

# Обработчик функции AJAX add_building.js
# Проверяет введенные данные в форму и то, что есть в базе данных
@app.route('/get_building', methods=['GET', 'POST'])
def get_building():
    print(request.form)
    build_name = request.form['building_name']
    db = get_db()
    mydbase = Building(db)
    building_id = mydbase.getBuilding(build_name, ALL=False)
    print('new_building', build_name)
    print('building_id', building_id)
    if (building_id):
        print('Уже есть')
        return json.dumps({'resp': "Old"})
    else:
        print('Новое здание')
        return json.dumps({'resp': "New"})

#Закрываем соединение с БД
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__=="__main__":
    app.run(debug=True)

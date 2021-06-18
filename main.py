from flask import Flask, render_template, request, flash, g, url_for
import sqlite3, os, re
from FDataBase import FDataBase
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

menu = [{"name": "Главная", "url": "/"},
        {"name": "Добавить", "url": "add"},
        {"name": "Добавить здание", "url": "add_building"},
        {"name": "Добавить помещение", "url": "add_room"},
        {"name": "Добавить панель", "url": "add_panel"},
        {"name": "Добавить кросс", "url": "add_cross"},
        {"name": "Добавить кабель", "url": "add_cable"},
        {"name": "Добавить муфту", "url": "add_opt_coupler"},
        {"name": "Поиск", "url": "find"}]
systems = ('Система1', 'Система2', 'Система3')
facility = ('Помещение1', 'Помещение2', 'Помещение3', 'Помещение4')
volokno = ('1', 'волокно 1')
@app.route("/")
def index():
    db = get_db()
    dbase=FDataBase(db)
    xxx=dbase.getFacility()
    for m in xxx:
        print(m)
    return render_template('index.html', title="Optika-главная", menu=dbase.getMenu(), systems=systems, facility=dbase.getFacility())

@app.route("/add", methods=['GET', 'POST'])
def add():
    db = get_db()
    dbase=FDataBase(db)
    colours = ['Здание', 'Помещение', 'Панель', 'Кабель', 'Кросс', 'Муфта']
    return render_template('add.html', title="Optika-add", menu=dbase.getMenu(), colours=colours)

@app.route("/add_building", methods=['GET', 'POST'])
def add_building():
    if request.method == "POST":
        if len(request.form['building_name']) > 1:  # Отображение подсказок
            flash('Данные отправлены', category='success')
        else:
            flash('Слишком короткое имя', category='error')
    return render_template('add_building.html', title="Добавить здание", menu=menu)

@app.route("/add_room", methods=['GET', 'POST'])
def add_room():
    if request.method == "POST":
        print(request.form)
    return render_template('add_room.html', title="Добавить помещение", menu=menu)

@app.route("/add_panel", methods=['GET', 'POST'])
def add_panel():
    if request.method == "POST":
        print(request.form)
    return render_template('add_panel.html', title="Добавить панель", menu=menu)

@app.route("/add_cross", methods=['GET', 'POST'])
def add_cross():
    if request.method == "POST":
        print(request.form)
    return render_template('add_cross.html', title="Добавить кросс", menu=menu)

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

#Закрываем соединение с БД
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__=="__main__":
    app.run(debug=True)

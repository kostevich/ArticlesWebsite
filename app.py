#!/usr/bin/env python

#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from datetime import datetime
from dublib.Methods import CheckPythonMinimalVersion
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

# Проверка поддержки используемой версии Python.
CheckPythonMinimalVersion(3, 11)

# Создаем основной объект класса Flask.
app = Flask(__name__)

# Настройки бд c названием sqlite:///blog.bd.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blog.db'

# Создание бд.
db = SQLAlchemy(app)

# Создание всех данных приложения.
with app.app_context():
     db.create_all()

#==========================================================================================#
# >>>>> СОЗДАНИЕ ПОЛЕЙ ТАБЛИЦЫ СТАТЕЙ <<<<< #
#==========================================================================================#   

# Создадим класс, на основе которого, будет создаваться поля таблицы.
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    # Получение данных объекта базы данных в виде строки.
    def __repr__(self):
        return '<Article %r>' % self.id

#==========================================================================================#
# >>>>> ВСЕ СТАТЬИ БЛОГА <<<<< #
#==========================================================================================#

@app.route('/WatchArticles')
def watch_articles():
    # Создаем объект, в котором находится данные всех полей класса Article.
    articles = Article.query.order_by(Article.create_on.desc()).all()

    # Возвращаем статьи на страницу.
    return render_template("WatchArticles.html", articles=articles)

#==========================================================================================#
# >>>>> ДЕТАЛЬНЫЙ ПРОСМОТР СТАТЬИ <<<<< #
#==========================================================================================#

@app.route('/WatchArticles/<int:id>')
# Функция для детального просмотра статьи.
def watch_detailarticles(id):
    # Сохраняем объект, в котором находится данные выбранной статьи.
    article = Article.query.get(id)

    # Возвращаем подробную статью на страницу.
    return render_template("WatchDetailarticles.html", article=article)

#==========================================================================================#
# >>>>> УДАЛЕНИЕ СТАТЬИ <<<<< #
#==========================================================================================#

@app.route('/WatchArticles/<int:id>/delete')
# Функция для вывода удаления статей.
def delete_detailarticles(id):
    # Ищем объект, который надо удалить или 404.
    article = Article.query.get_or_404(id)

    try:
        # Удаление объекта класса Article и добавление в сессию.
        db.session.delete(article)

        # Удаление статьи в базе данных.
        db.session.commit()

        # Возвращение на страницу со всеми статьями.
        return redirect('/WatchArticles')
    
    # Исключение.
    except:
        # Возвращаем ошибку: "Не удалось удалить статью".
        return "Не удалось удалить статью."
    
    # Возвращаем статьи на страницу.
    return render_template("WatchArticles.html", article=article)

#==========================================================================================#
# >>>>> РЕДАКТИРОВАНИЕ СТАТЬИ <<<<< #
#==========================================================================================#

@app.route('/WatchArticles/<int:id>/edit', methods=['POST', 'GET'])
# Функция для вывода всех статей.
def edit_detailarticles(id):
    article = Article.query.get(id)

    if request.method == 'POST':
        # Сохраняем в переменную значение из поля формы.
        article.tag = request.form['tag']
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']  

        # Попробуем добавить значения в базу данных.
        try:
            # Сохранение в базе данных.
            db.session.commit()

            # Возвращение на страницу со всеми статьями.
            return redirect('/WatchArticles') 
        
        # Исключение.
        except:
            # Возвращаем ошибку: "Не удалось добавить статью".
            return "Не удалось добавить статью." 
        
    article = Article.query.get(id)

    return render_template("EditArticles.html", article=article)    

#==========================================================================================#
# >>>>> СОЗДАНИЕ СТАТЬИ <<<<< #
#==========================================================================================#

# Декоратор, который регистрирует URL-адрес, и отслеживающий методы POST и GET.
@app.route('/CreateArticles', methods=['POST', 'GET'])
# Функция для вывода информации по ссылке.
def create_articles():
    # Если запрос с методом POST.
    if request.method == 'POST':
        # Сохраняем в переменную значение из поля формы.
        tag = request.form['tag']
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        # Сохраняем объект класса Article с данными из переменных, записанных в нужные поля)
        article = Article(title=title, tag=tag, intro=intro, text=text)

        # Попробуем добавить значения в базу данных.
        try:
            # Добавление объекта класса Article в сессию.
            db.session.add(article)

            # Сохранение в базе данных.
            db.session.commit()

            # Возвращение на страницу со всеми статьями.
            return redirect('/WatchArticles')
        
        # Исключение.
        except:
            # Возвращаем ошибку: "Не удалось изменить статью".
            return "Не удалось изменить статью."
        
    # Если запрос с методом POST.
    else:
        # Возвращаемся на страницу.
        return render_template("CreateArticles.html")
    

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

# Проверка правильности запуска проекта через файл с названием app.
if __name__ == '__main__':
    # Запуск приложения и отслеживание ошибок.
    app.run(debug=True)

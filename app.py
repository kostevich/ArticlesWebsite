# Импортируем класс Flask из модуля flask.
from flask import Flask
# Импортируем модуль render_template для работы шаблонов.
from flask import render_template
# Импортируем модуль request получения запросов.
from flask import request
# Импортируем модуль redirect для перенаправления на другую страницу.
from flask import redirect
# Импортируем модуль SQLAlchemy для работы с базой данных.
from flask_sqlalchemy import SQLAlchemy
# Импортируем модуль datetime для работы с полем дата базы данных.
from datetime import datetime

# Создаем основной объект app класса Flask.
app = Flask(__name__)
# Настройки бд c названием sqlite:///blog.bd.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# Создание бд.
db = SQLAlchemy(app)


# Создадим класс, на основе которого, будет создаваться таблица.
class Article(db.Model):
    # Добавим поле id, уникальное.
    id = db.Column(db.Integer, primary_key=True)
    # Добавим поле тег, не может быть пустым.
    tag = db.Column(db.String(20), nullable=False)
    # Добавим поле название, не может быть пустым.
    title = db.Column(db.String(50), nullable=False)
    # Добавим поле вводный текст, не может быть пустым.
    intro = db.Column(db.String(200), nullable=False)
    # Добавим поле основного текста артикула, не может быть пустым.
    text = db.Column(db.Text, nullable=False)
    # Добавим поле время создания, значение по умолчанию время сейчас.
    create_on = db.Column(db.DateTime, default=datetime.utcnow)
    # Добавим поле время изменения, значение по умолчанию время сейчас, и оно обновляется при обновлении информации в базе данных.
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    # Получение данных объекта базы данных в виде строки.
    def __repr__(self):
        return '<Article %r>' % self.id


# Декоратор, который регистрирует URL-адрес.
@app.route('/')
# Функция для вывода информации по ссылке.
def index():
    # Возвращаем на страницу текст.
    return render_template("index.html")


# Декоратор, который регистрирует URL-адрес.
@app.route('/about')
# Функция для вывода информации по ссылке.
def about():
    # Возвращаем на страницу текст.
    return render_template("about.html")


# Декоратор, который регистрирует URL-адрес.
@app.route('/watch_articles')
# Функция для вывода всех статей.
def watch_articles():
    # Создаем объект, в котором находится данные всех полей класса Article.
    articles = Article.query.order_by(Article.create_on.desc()).all()
    # Возвращаем статьи на страницу.
    return render_template("watch_articles.html", articles=articles)


@app.route('/watch_articles/<int:id>')
# Функция для детального просмотра статьи.
def watch_detailarticles(id):
    # Сохраняем объект, в котором находится данные выбранной статьи.
    article = Article.query.get(id)
    # Возвращаем подробную статью на страницу.
    return render_template("watch_detailarticles.html", article=article)


@app.route('/watch_articles/<int:id>/delete')
# Функция для вывода всех статей.
def delete_detailarticles(id):
    # Ищем объект, который надо удалить или 404.
    article = Article.query.get_or_404(id)
    try:
        # Удаление объекта класса Article и добавление в сессию.
        db.session.delete(article)
        # Удаление статьи в базе данных.
        db.session.commit()
        # Возвращение на страницу со всеми статьями.
        return redirect('/watch_articles')
    # Исключение.
    except:
        # Возвращаем ошибку: "Не удалось удалить статью".
        return "Не удалось удалить статью."
    # Возвращаем статьи на страницу.
    return render_template("watch_articles.html", article=article)


# Декоратор, который регистрирует URL-адрес, и отслеживающий методы POST и GET.
@app.route('/create_articles', methods=['POST', 'GET'])
# Функция для вывода информации по ссылке.
def create_articles():
    # Если запрос с методом POST.
    if request.method == 'POST':
        # Сохраняем в переменную text значение из поля формы text.
        tag = request.form['tag']
        # Сохраняем в переменную title значение из поля формы title.
        title = request.form['title']
        # Сохраняем в переменную intro значение из поля формы intro.
        intro = request.form['intro']
        # Сохраняем в переменную text значение из поля формы text.
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
            return redirect('/watch_articles')
        # Исключение.
        except:
            # Возвращаем ошибку: "Не удалось добавить статью".
            return "Не удалось добавить статью."
    # Если запрос с методом POST.
    else:
        # Возвращаемся на страницу.
        return render_template("create_articles.html")


# Проверка правильности запуска проекта через файл с названием app.
if __name__ == '__main__':
    # Запуск приложения и отслеживание ошибок.
    app.run(debug=True)

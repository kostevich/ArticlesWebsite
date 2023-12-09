# ArticlesWebsite
**ArticlesWebsite** – учебный проект на Flask, представляющий собой блог, имеется функция редактирования и просмотра статей автора.
# Порядок установки и использования
1. Загрузить репозиторий. Распаковать.
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [dublib](https://github.com/DUB1401/dublib), [flask](https://github.com/pallets/flask?ysclid=lpxvt6k9hy682670415), [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/latest/).
```
pip install flask
pip install flask-sqlalchemy
pip install git+https://github.com/DUB1401/dublib
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. В среде исполнения запустить файл _app.py_ командой:
```
 flask run
```
5. Перейти по ссылке (пример: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)).

# Отслеживание в базе данных.
Откройте файл Blog.db в программе для открытия баз данных (пример: [SQLiteStudio](https://sqlitestudio.pl/)).

# Пример работы
**Статьи блога:**

![image](https://github.com/kostevich/ArticlesWebsite/assets/109979502/1e8f6711-90f8-4c47-874b-98de3e521f09)

**Детальный просмотр статьи блога:**

![image](https://github.com/kostevich/ArticlesWebsite/assets/109979502/db782eef-afff-47f2-a063-9a1ef7150bb1)

**Добавление статьи:**

![image](https://github.com/kostevich/ArticlesWebsite/assets/109979502/a47bb6b6-278c-43a5-a47b-8a16c1ca3c4f)

**Обновление статьи:**

![image](https://github.com/kostevich/ArticlesWebsite/assets/109979502/e3cae48e-304e-4709-b28a-c2cde7d14641)

_Copyright © Kostevich Irina. 2023._

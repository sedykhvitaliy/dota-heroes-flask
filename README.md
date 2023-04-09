# База данных героев из Dota 2 на FLASK
Эта программа может добавлять, изменять, удалять героев из базы данных. Присутсвует регистрация и авторизация пользователей.
## Установка
```
git clone https://github.com/sedykhvitaliy/dota-heroes-flask.git
cd dota-heroes-flask
pip install -r requirements.txt
```
### Настройка переменных окружения 
Для Windows: 
```
setx DATABASE_URL postgresql://postgres:postgres@localhost:5432/your_db
```
Для Linux:
```
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/your_db
```
### Создание таблиц в базе данных:
```
flask shell
from app import db
db.create_all()
quit()
```
### Endpoints
#### Авторизация и регистрация
```
/registration/
/login/
/logout/
```
#### Работа с героями
Список героев
```
GET /heroes_list
```
# My Project API #

REST API для управления пользователями и их предметами. Реализована регистрация, авторизация по JWT-токенам, а также CRUD-операции для предметов (с привязкой к конкретному пользователю).

## Живая демонстрация ##

Проект задеплоен и доступен по ссылке:
[https://my-project-hf9p.onrender.com/docs](https://my-project-hf9p.onrender.com/docs)

(Примечание: используется бесплатный тариф Render, поэтому первый запрос может занять 30–60 секунд для «пробуждения» сервера).

## Стек технологий ##

- **Python 3.11**
- **FastAPI** — веб-фреймворк
- **SQLAlchemy** — ORM для работы с БД
- **PostgreSQL** — база данных
- **Alembic** — миграции
- **JWT (python-jose)** — авторизация
- **Passlib** — хеширование паролей
- **Docker** — контейнеризация (локально)

## Как запустить локально ##

1. Клонируйте репозиторий:
```bash
git clone https://github.com/XiaoShougeZhe/my_project.git
cd my_project

2. Создайте виртуальное окружение и активируйте его:
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

3. Установите зависимости:
pip install -r requirements.txt

4. Создайте файл .env в корне проекта:
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql://postgres:password@localhost:5432/my_project_db

5. Примените миграции:
alembic upgrade head

6. Запустите сервер:
uvicorn app.main:app --reload

7. Откройте Swagger UI:
http://127.0.0.1:8000/docs

## Основные эндпоитны ##

# Метод #	  # Путь # 	     # Описание #
POST	     /users/register   	Регистрация
POST	    /users/login	        Логин (получение JWT)
GET	     /users/me	        Информация о текущем пользователе
POST	    /items	               Создать предмет
GET	    /items	              Список предметов
GET	    /items/{id}	         Получить предмет
PUT	    /items/{id}	         Обновить предмет
DELETE   /items/{id}	         Удалить предмет
GET	   /items/search	        Поиск по названию

## Авторизация ##

Для доступа к защищённым эндпоинтам передавайте токен в заголовке:
Authorization: Bearer <ваш_токен>
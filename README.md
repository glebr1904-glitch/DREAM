# DREAM

Интернет-магазин светодиодной продукции и осветительных товаров.

## Возможности

- Просмотр каталога и карточек товаров
- Поиск товаров
- Регистрация и вход пользователей
- Профиль пользователя

## Технологии

- Python
- Django
- PostgreSQL
- HTML, CSS, Bootstrap

## Требования

- Python 3.13.1
- PostgreSQL 17.10

## Установка и запуск

1. Склонируйте репозиторий и перейдите в его папку.
2. Создайте и активируйте виртуальное окружение.
3. Установите зависимости.
4. Настройте подключение к базе данных.
5. Выполните миграции.
6. Запустите сервер разработки.

Пример команд для Windows Bash:

```bash
python -m venv venv
. venv/Scripts/activate
#библиотеки вирт. окружения 
Package                 Version
----------------------- -------
asgiref                 3.11.1
asttokens               3.0.1
colorama                0.4.6
decorator               5.2.1
Django                  5.2.11
django-debug-toolbar    6.3.0
executing               2.2.1
ipython                 9.13.0
ipython_pygments_lexers 1.1.1
jedi                    0.20.0
matplotlib-inline       0.2.2
parso                   0.8.7
pillow                  12.2.0
pip                     24.3.1
prompt_toolkit          3.0.52
psutil                  7.2.2
psycopg2-binary         2.9.12
pure_eval               0.2.3
Pygments                2.20.0
sqlparse                0.5.5
stack-data              0.6.3
traitlets               5.15.0
tzdata                  2025.3
wcwidth                 0.7.0
cd my_shop/
ls #проверка есть ли manage.py
#создаешь базу данных в PostgreSQL(pgadmin4). Порт и названия должны совпадать с тем что написанно в settings.
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
# Название проекта
Добавьте краткое описание проекта, опишите какую задачу он решает. 1-3 предложения будет достаточно. Добавьте бейджи для важных статусов проекта: статус разработки (в разработке, на поддержке и т.д.), статус билда, процент покрытия тестами и тд.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-ci/cd)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- [Python 3.12.4](https://www.python.org/downloads/release/python-3124/)
- [Django 5.1.1](https://docs.djangoproject.com/en/5.1/)
- [PostgresQL 16.3](https://www.postgresql.org/docs/16/index.html)
- [Pytest 8.3.3](https://docs.pytest.org/en/stable/contents.html)

## Использование
Для запуска приложения необходимо скачать PostgreSQL и создать базу данных (на [Linux](https://www.nic.ru/help/kak-ustanovit6-postgresql_11163.html) на [Windows](https://docs.rkeeper.ru/rk7/7.7.0/ru/ustanovka-postgresql-na-windows-29421153.html)).
После создания базы данных и пользователя нужно внести настройки БД в settings.py для подключения к БД приложением

settings.py
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "your_name_DB",
        "USER": "your_name_user_in_DB",
        "PASSWORD": "your_password_user_in_DB",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

Создайте виртульное окружение и установите зависимости из requirements.txt:
```shell
$ pip install -r requirements.txt
```

Выполните все миграции:
```shell
$ python manage.py migrate
```

## Разработка

### Запуск сервера
Чтобы запустить сервер выполните команду:
```shell
$ python manage.py runserver
```

## Тестирование
Проект покрыт юнит-тестами Pytest. Для их запуска выполните команду:
```shell
$ pytest
```

### Зачем вы разработали этот проект?
Для отработки следующих навыков:
- работа фреймворком Django
- создание и подключение базы данных PostgreSQL
- написание тестов с использованием фреймворка Pytest

Также проект является пет-проектом

## Команда проекта
Оставьте пользователям контакты и инструкции, как связаться с командой разработки.

- [Быков Владимир](https://t.me/ReBiwer) — Back-End Engineer
 
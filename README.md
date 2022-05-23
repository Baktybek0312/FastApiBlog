# FastApiBlog


## Настройка перед запуском

1. Первое, что нужно сделать, это клонировать репозиторий:
```sh
$ git clone https://github.com/Baktybek0312/FastApiBlog
```

2. Создайте виртуальную среду для установки зависимостей и активируйте ее:

```sh
$ virtualenv env
$ source env/bin/activate
```

3. Затем установите зависимости:

```sh
(env)$ pip install -r requirements/base.txt
```

4. У вас должен быть установлен PostgreSQL, здесь краткое описания для установки PostgreSQL в Linux [Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart-ru), а для  [Windows](https://www.postgresql.org/download/windows/) здесь
+ создайте [БД](https://www.vultr.com/docs/how-to-install-configure-backup-and-restore-postgresql-on-ubuntu-20-04-lts)
+ и также создаем [схему](https://postgrespro.ru/docs/postgrespro/9.5/ddl-schemas) в БД

5. Создайте файл .env и пропишите как примере свои параметры
```sh
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_SERVER=host_db
POSTGRES_PORT=5432
POSTGRES_DB=database_name

SECRET_KEY="b79dfa0ead657661e874c8a4756b96d2c29fdd9e6e44abf33d7de5600615760d"
ALGORITHM="HS256"
#openssl rand -hex 32

TEST_SQLALCHEMY_DATABASE_URL="postgresql://user:password@host:port/database_name"
```
6. Проверьте базу, так как все миграции проходят через [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html), также в проекте мы используем [автоматическое создание миграции](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
```sh
$ alembic init migration
$ alembic revision --autogenerate -m "text" 
$ alembic upgrade head
```
8. Запускаем сервер:

```sh
(env)$ uvicorn main:app --reload
```
* Навигация для API *`http://127.0.0.1:8000/docs` и также по адресу `http://127.0.0.1:8000/redoc`,
вы можете ссалыться на автоматическая генерация документации в соответствии с OpenAPI с помощью интерактивного интерфейса Swagger и работать с endpoint(urls)

7. Установите [Postman](https://www.postman.com/downloads/) для работы с эндпоинтами FastApi
- импортируйте файл ***BlogFastApi.postman_collection.json***
  - Эндпоинты для Юзера
    ```sh
    http://127.0.0.1:8000/users/create # для создание пользователя
    http://127.0.0.1:8000/users/token  # для получение токена
    http://127.0.0.1:8000/users/me # Возвращает информацию о пользователе
    ```
  - Эндпоинты для Постов 
    ```sh
    http://127.0.0.1:8000/posts/create # для создание постов
    http://127.0.0.1:8000/posts/list  # для получение всех постов
    http://127.0.0.1:8000/posts/{'post_id'} # для получение детальную информацию одного поста
    ```
  - Эндпоинты для Комментарии
    ```sh
    http://127.0.0.1:8000/posts/{post_id}/comments # для создание комментариев
    ```

8. Последний штрих это тестирование проекта
- создаем БД, как и ранее в файле .env мы передали параметры **TEST_SQLALCHEMY_DATABASE_URL**
- запускаем [Pytest](https://docs.pytest.org/en/6.2.x/contents.html)
```sh
$ pytest tests
```

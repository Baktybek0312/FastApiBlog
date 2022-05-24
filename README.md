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
   $ alembic revision --autogenerate -m "text_commit" 
   $ alembic upgrade head
   ```
7. Запускаем сервер:
   ```sh
   (env)$ uvicorn main:app --reload
   ```
   
   * Навигация для API *`http://127.0.0.1:8000/docs` и также по адресу `http://127.0.0.1:8000/redoc`,
   вы можете ссалыться на автоматическая генерация документации в соответствии с OpenAPI с помощью интерактивного интерфейса Swagger и работать с endpoint(urls)

8. Установите [Postman](https://www.postman.com/downloads/) для работы с эндпоинтами FastApi
   - импортируйте файл ***BlogFastApi.postman_collection.json***
   - Эндпоинты для Юзера
   ##### http://127.0.0.1:8000/users/create  Для создание пользователя
   <details>
      <summary>Show more</summary>
      input:
      {
         'username': 'test_user',
         'email': 'test_user@example.com',
         'password': 'test_password_hash'
      }
      output:
         "you have successfully sign up test_user"
   </details>

   ##### http://127.0.0.1:8000/users/token  Для получение токена

   <details>
      <summary>Show more</summary>
      input:
      username: test_user
      password: test_password_hash
      output: 
      {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjUzMzA0NjcwfQ.g4wLtG2wceZLaydoVFbVghFTGt27Qxqb3bAQ010Q6D8",
      "token_type": "bearer"
      }
   </details>
   
   ##### http://127.0.0.1:8000/users/me  Возвращает информацию о пользователе
      <details>
      <summary>Show more</summary>
      <p>input:<br>
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjUzMzA0NjcwfQ.g4wLtG2wceZLaydoVFbVghFTGt27Qxqb3bAQ010Q6D8",<br>
      
      output:<br>
      {<br>
         "email": "user1@gmail.com",<br>
         "hashed_password": "$2b$12$/Xo7FRTI5TwBFuFK4MQ/s.PKIIIAUVlQQ36EMmKItEkEUN4GL/kFK",<br>
         "id": 3,<br>
         "created_date": "2022-05-10T05:43:56.400840",<br>
         "username": "user",<br>
         "is_active": true<br>
      }</p>
      </details>

- Эндпоинты для Постов 

   ##### http://127.0.0.1:8000/posts/create  Для создание постов
   <details>
      <summary>Show more</summary>
      <p>input:<br>
         {<br>
            "title": " Test title",<br>
            "description": " Hello World!"<br>
         }<br>
      output:<br>
      {<br>
         "id": 20,<br>
         "description": " Hello World!",<br>
         "title": " Test title",<br>
         "owner_id": 3<br>
      }</p>
   </details>
      
   ##### http://127.0.0.1:8000/posts/list Для получение всех постов
   <details>
      <summary>Show more</summary>
      <p>
      output:<br>
      [<br>
    {<br>
        "id": 1,<br>
        "description": "adnqwmdmwq;",<br>
        "title": "asdqwwqwd",<br>
        "owner_id": 2,<br>
        "owner": {<br>
            "email": "admin@gmail.com",<br>
            "id": 2,<br>
            "username": "admin"<br>
        }<br>
    },<br>
    {<br>
        "id": 6,<br>
        "description": "adnqwmdmwq;",<br>
        "title": "asdqwwqwd",<br>
        "owner_id": 2,<br>
        "owner": {<br>
            "email": "admin@gmail.com",<br>
            "id": 2,<br>
            "username": "admin"<br>
        }<br>
    },<br>
    {<br>
        "id": 7,<br>
        "description": "adnqwmdmwq;",<br>
        "title": "asdqwwqwd",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user",<br>
        }<br>
    },<br>
    {<br>
        "id": 8,<br>
        "description": "adnqwmdmwq;",<br>
        "title": "asdqwwqwd",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 9,<br>
        "description": "adnqwmdmwq;",<br>
        "title": "asdqwwqwd",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 10,<br>
        "description": "dwqdqwdw;",<br>
        "title": "awdww",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 11,<br>
        "description": "dwqdqwdw;",<br>
        "title": "awdww",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 12,<br>
        "description": "dwqdqwdw;",<br>
        "title": "awdww",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user",<br>
        }<br>
    },<br>
    {<br>
        "id": 13,<br>
        "description": "dwqdqwdw;",<br>
        "title": "awdww",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 14,<br>
        "description": "dwqdqwd;",<br>
        "title": "asdqwddsvwemclsa",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 15,<br>
        "description": "dwqdqwd;",<br>
        "title": "asdqwddsvwemclsa",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 16,<br>
        "description": "dwqdqwd;",<br>
        "title": "asdqwddsvwemclsa",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 17,<br>
        "description": "вфывйцвйц;",<br>
        "title": "Еуфвй",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 18,<br>
        "description": "",<br>
        "title": "Еуфвй",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 19,<br>
        "description": "",<br>
        "title": "",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    },<br>
    {<br>
        "id": 20,<br>
        "description": " Hello World!",<br>
        "title": " Test title",<br>
        "owner_id": 3,<br>
        "owner": {<br>
            "email": "user1@gmail.com",<br>
            "id": 3,<br>
            "username": "user"<br>
        }<br>
    }<br>
  ]</p>
   </details>
  
  ##### http://127.0.0.1:8000/posts/{'post_id'} Для получение детальную информацию одного поста
    <details>
      <summary>Show more</summary>
      <p>input:<br>
         }<br>
      output:<br>
      {<br>
    "post_app": {<br>
        "id": 1,<br>
        "description": "adnqwmdmwq;",<br>
        "title": "asdqwwqwd",<br>
        "owner_id": 2,<br>
        "owner": {<br>
            "email": "admin@gmail.com",<br>
            "id": 2,<br>
            "username": "admin"<br>
        }<br>
    },
    "comments": [<br>
        {
            "id": 1,<br>
            "created_date": "2022-05-10T05:46:23.173248",<br>
            "message": "asdqwdqwdqwdqd",<br>
            "post_id": 1,<br>
            "is_active": true,<br>
            "owner_id": 3,<br>
            "owner_comment": {<br>
                "email": "user1@gmail.com",<br>
                "id": 3,<br>
                "username": "user"<br>
            }<br>
        }<br>
    ]<br>
   }<br>
         "owner_id": 3<br>
      }</p>
   </details>
  
- Эндпоинты для Комментарии
   #####              http://127.0.0.1:8000/posts/{post_id}/comments Для создание комментариев

   <details>
      <summary>Show more</summary>
      <p>input:<br>
         {<br>
         "message": "asdqwdqwdqwdqd"<br>
         }<br>
      output:<br>
      {<br>
         "message": "asdqwdqwdqwdqd",<br>
         "id": 2,<br>
         "post_id": 1,<br>
         "owner_comment": {<br>
        "username": "user",<br>
        "id": 3,<br>
        "is_active": true<br>
    },<br>
    "created_date": "2022-05-24T05:18:54.658754"<br>
   }</p><br>
   </details>
9. Последний штрих это тестирование проекта
- создаем БД, как и ранее в файле .env мы передали параметры **TEST_SQLALCHEMY_DATABASE_URL**
- запускаем [Pytest](https://docs.pytest.org/en/6.2.x/contents.html)
```sh
$ pytest tests
```

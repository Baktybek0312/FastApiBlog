from sqlalchemy import true

from tests.conftest import BaseConfig


class TestPost(BaseConfig):

    def test_create_post(self, client, authorized_client):
        """
        для создание тестовых постов
        """
        data = {
            'title': 'Testing Title',
            'description': 'Hello!',
        }
        response = client.post('/posts/create', json=data, headers=authorized_client)
        assert response.status_code == 201
        return response.json() == {
            "id": 1,
            "description": " Hello!",
            "title": " Test title",
            "owner_id": 1
        }

    def test_get_id_post(self, client):
        """
        Для получение одного поста
        """
        post_id = 1
        response = client.get(f'/posts/{post_id}')
        assert response.status_code == 200
        return response.json() == {
            "description": "adnqwmdmwq;",
            "id": 1,
            "title": "asdqwwqwd",
            "owner_id": 1,
            "owner": {
                "id": 1,
                "email": "admin@gmail.com",
                "username": "admin"
            }
        }

    def test_comment_create(self, client, authorized_client):
        """
        тест для проверки комметрии к посту
        """
        post_id = 1
        data = {'message': 'Hello World!'}
        response = client.post(f'/posts/{post_id}/comments', json=data, headers=authorized_client)
        assert response.status_code == 200
        return response.json() == {
            "message": "asdqwdqwdqwdqd",
            "id": 2,
            "post_id": 1,
            "owner_comment": {
                "username": "user",
                "id": 3,
                "is_active": true
            },
            "created_date": "2022-05-24T05:18:54.658754"
        }

    def test_posts_list(self, client):
        """
        Для вывода всех тестовых постов
        """
        response = client.get('/posts/list')
        assert response.status_code == 200
        return response.json() == {
            "description": "adnqwmdmwq;",
            "id": 1,
            "title": "asdqwwqwd",
            "owner_id": 1,
            "owner": {
                "id": 1,
                "email": "admin@gmail.com",
                "username": "admin"
            }
        }

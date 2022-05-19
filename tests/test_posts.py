import json

from sqlalchemy import true

from tests.conftest import BaseConfig


class TestPost(BaseConfig):

    def test_get_id_post(self, client, create_test_post):
        """
        Для получение одного поста
        """
        response = client.get('/posts/1', json=json.dumps(create_test_post))
        assert response.status_code == 200
        return response.json() == {
            "post_app": {
                "description": "adnqwmdmwq;",
                "id": 1,
                "title": "asdqwwqwd",
                "owner_id": 2,
                "owner": {
                    "id": 2,
                    "email": "admin@gmail.com",
                    "username": "admin"
                }
            },
            "comments": [
                {
                    "is_active": true,
                    "id": 1,
                    "owner_id": 3,
                    "created_date": "2022-05-10T05:46:23.173248",
                    "message": "asdqwdqwdqwdqd",
                    "post_id": 1,
                    "owner_comment": {
                        "id": 3,
                        "email": "user1@gmail.com",
                        "username": "user"
                    }
                }
            ]
        }

    def test_post_list(self, client):
        """
        Для вывода всех тестовых постов
        """
        response = client.get('/posts/list')
        assert response.status_code == 200
        return response.json()


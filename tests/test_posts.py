from tests.conftest import BaseConfig


class TestPost(BaseConfig):

    def test_create_post(self, client, authorized_client):
        """
        для создание тестовых постов
        """
        data = {
            'title': 'Testing Title',
            'description': 'Hello',
        }
        response = client.post('/posts/create', json=data, headers=authorized_client)
        assert response.status_code == 201, response.json() == 'successfully created'

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

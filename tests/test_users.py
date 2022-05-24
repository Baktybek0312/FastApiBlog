from sqlalchemy import true

from tests.conftest import BaseConfig


class TestUser(BaseConfig):
    def test_create_user(self, client):
        """
        проверка создание полььзователя
        """
        data = {'username': 'leodoe', 'email': 'leodoe@exapml.com', 'password': 'leodoepass'}
        response = client.post('/users/create', json=data)
        assert response.status_code == 201
        return response.json() == 'success user'

    def test_check_create_user(self, client):
        data = {'username': 'leodoe', 'email': 'leodoe@exapml.com', 'password': 'leodoepass'}
        response = client.post('/users/create', json=data)
        assert response.status_code == 400, response.json() == 'already registered'

    def test_get_token(self, client):
        """
        проверка для получение токена
        """
        response = client.post('/users/token', data={'username': 'leodoe', 'password': 'leodoepass'})
        assert response.status_code == 200, response.json() == 'SUCCESSFULLY autorised'

    def test_check_get_token(self, client):
        response = client.post('/users/token', data={'username': 'leodoe', 'password': 'qda'})
        assert response.status_code == 401, response.json() == 'the username or password is not correct'

    def test_get_current_user(self, client, authorized_client):
        """
        проверка для получение информацию о пользователя
        """
        response = client.get('/users/me', headers=authorized_client)
        assert response.status_code == 200, response.json() == {
            "email": "user1@gmail.com",
            "hashed_password": "$2b$12$/Xo7FRTI5TwBFuFK4MQ/s.PKIIIAUVlQQ36EMmKItEkEUN4GL/kFK",
            "id": 3,
            "created_date": "2022-05-10T05:43:56.400840",
            "username": "user",
            "is_active": true
        }

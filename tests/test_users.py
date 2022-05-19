from tests.conftest import BaseConfig


class TestUser(BaseConfig):

    def test_premissions_user(self, client, create_user, authorized_client):

        # Создание пользователя
        response = client.post(
            '/users/create',
            json={'username': 'User12', 'email': 'User12@gmail.com', 'password': 'user_admin12345'}
        )
        assert response.status_code == 201, response.text

        # Отображение пользователя
        response = client.get(
            '/users/me', headers=authorized_client
        )
        assert response.status_code == 200, response.text

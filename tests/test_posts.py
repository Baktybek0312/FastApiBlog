from tests.conftest import BaseConfig


class TestPost(BaseConfig):
    def test_create_post(self, client, authorized_client):
        data = {"title": "asdqwwqwd", "description": "adnqwmdmwq"},

        response = client.post('/posts/create', json=data, headers=authorized_client)
        assert response.status_code == 201
        return response.json()

    def test_post_list(self, client):
        response = client.get('/posts/list')
        assert response.status_code == 200



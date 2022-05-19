from tests.conftest import BaseConfig


class TestComment(BaseConfig):

    def test_comments(self, client, create_test_post, authorized_client):
        """
        тест для проверки комметрии к посту
        """
        data = {"message": "Hello World!"}
        response = client.post('/posts/1/comments', json=data, headers=authorized_client)
        assert response.status_code == 200
        return response

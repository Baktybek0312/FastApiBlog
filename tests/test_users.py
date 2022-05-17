import json

from tests.conftest import BaseConfig


class TestUser(BaseConfig):

    def test_premissions_user(self, client, create_user, authorized_client):
        # Create user
        response = client.post(
            "/users/create",
            json=create_user
        )
        assert response.status_code == 201

        # Get user
        response = client.get(
            "/users/me", headers=authorized_client
        )
        assert response.status_code == 200, response.text

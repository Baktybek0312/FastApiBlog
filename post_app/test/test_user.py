from .. import schemas


def test_create_user(client):
    response = client.post(
        "http://127.0.0.1:8000/user/users/",
        json={
            "username": "Harry213", "email": "harrystyles@england.com",
            "password": "user_admin12345"
        }
    )

    assert response.status_code == 201
    assert response.json() == {'message': 'Success created'}

def test_create_user(client):
    response = client.post(
        "/user/users/",
        json={
            "username": "Harry213", "email": "harrystyles@england.com",
            "password": "user_admin12345"
        }
    )

    assert response.json() != {'message': 'Success created'}
    assert response.status_code == 201


def test_authorized_client(client, authorized_client, create_access_token):
    response = client.post(
        "/user/token", json={
            "username": "Harry213",
            "email": "harrystyles@england.com",
            "password": "user_admin12345"
        }
    )

    assert response.status_code == 200
    return {"access_token": create_access_token, "token_type": "bearer"}

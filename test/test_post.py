from db import schemas


def test_get_all_posts(client):
    response = client.get("/posts/all")

    def validate(post):
        return schemas.PostList(**post)

    map(validate, response.json())
    assert response.status_code == 200


def test_create_post(client, create_user, create_access_token, create_test_posts):
    response = client.post("/posts/create")
    assert response.status_code == 201
    assert response.json() == response

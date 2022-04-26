from .. import schemas


def test_get_all_posts(authorized_client, create_test_posts):
    response = authorized_client.get("/posts/all")

    def validate(post):
        return schemas.PostList(**post)

    map(validate, response.json())
    assert response.status_code == 200


def test_unauthorized_user_get_all_posts(client, create_test_posts):
    response = client.get("/posts/create")
    assert response.status_code == 201
    assert response.json() == response

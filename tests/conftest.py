import pytest
from starlette.testclient import TestClient

from .test_database import TestingSessionLocal, engine
from db.database import Base, get_db
from main import app
from db.models import models
from services import oauth2


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def create_user(client):
    response = client.post(
        "/user/users/",
        json={"username": "Harry213", "email": "harrystyles@england.com",
              "password": "harrypassword"}
    )
    new_user = response.json()
    return new_user


@pytest.fixture
def create_access_token(create_user):
    return oauth2.create_access_token({"user_id": create_user["id"]})


@pytest.fixture
def authorized_client(client, create_access_token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {create_access_token}"
    }
    return client


@pytest.fixture
def create_test_posts(create_user, session):
    data = [{
        "title": "First Post",
        "description": "First Post Content",
        "owner_id": create_user["id"]
    },
        {
            "title": "Second Post",
            "description": "Second Post Content",
            "owner_id": create_user["id"]
        },
        {
            "title": "Third Post",
            "description": "Third Post Content",
            "owner_id": create_user["id"]
        }]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, data)
    posts = list(post_map)
    session.add_all(posts)
    session.commit()

    posts = session.query(models.Post).all()
    return posts

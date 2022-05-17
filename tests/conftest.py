import pytest
from fastapi.testclient import TestClient

from .test_database import TestingSessionLocal, engine
from db.database import Base, get_db
from main import app
from core.settings import settings


class BaseConfig:

    @pytest.fixture
    def session(self):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    @pytest.fixture
    def client(self, session) -> TestClient:
        def override_get_db():
            try:
                yield session
            finally:
                session.close()

        app.dependency_overrides[get_db] = override_get_db
        yield TestClient(app)

    @pytest.fixture
    def create_user(self, client):
        data = {
            'username': settings.TEST_USERNAME,
            'email': settings.TEST_USER_PASSWORD,
            'password': settings.TEST_USER_PASSWORD
        }
        response = client.post('/users/create', json=data)
        return response.json()

    @pytest.fixture
    def authorized_client(self, client, create_user):
        data = {"username": settings.TEST_USERNAME, "password": settings.TEST_USER_PASSWORD}
        r = client.post("/users/token", data=data)
        response = r.json()
        auth_token = response["access_token"]
        headers = {"Authorization": f"Bearer {auth_token}"}
        return headers

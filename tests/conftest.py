import pytest
from fastapi.testclient import TestClient

from .test_database import TestingSessionLocal, engine
from db.database import Base, get_db
from main import app


class BaseConfig:

    @pytest.fixture(scope='session')
    def session(self):
        """
        Создаем базу данных
        """
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    @pytest.fixture
    def client(self, session):
        """
        Переопределение зависимостей
        """

        def override_get_db():
            try:
                yield session
            finally:
                session.close()

        app.dependency_overrides[get_db] = override_get_db

        yield TestClient(app)

    @pytest.fixture
    def create_user(self, client):
        """
        для создание тестового пользователя
        """
        data = {
            'username': 'admin12',
            'email': 'admin12@example.com',
            'password': 'admin_user12345'
        }
        response = client.post('/users/create', json=data)
        return response.json()

    @pytest.fixture
    def authorized_client(self, client, create_user):
        """
        для прохождения авторизации тестовых запросах
        """
        data = {"username": 'admin12', "password": 'admin_user12345'}
        r = client.post("/users/token", data=data)
        response = r.json()
        auth_token = response["access_token"]
        headers = {"Authorization": f"Bearer {auth_token}"}
        return headers
    #
    # @pytest.fixture
    # def create_test_post(self, session):
    #     """
    #     для создание тестовых постов
    #     """
    #     data = [{
    #         "title": "First Post",
    #         "description": "First Post Content",
    #     },
    #         {
    #             "title": "Second Post",
    #             "description": "Second Post Content",
    #         },
    #         {
    #             "title": "Third Post",
    #             "description": "Third Post Content",
    #         }]
    #
    #     def create_post_model(post):
    #         return models.Post(**post)
    #
    #     post_map = map(create_post_model, data)
    #     posts = list(post_map)
    #     session.add_all(posts)
    #     session.commit()
    #
    #     posts = session.query(models.Post).all()
    #     return posts

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

    @classmethod
    def setup_class(cls):
        "Выполняется один раз за класс"
        print('START')

    @classmethod
    def teardown_class(cls):
        "Запуск в конце класса"
        print('END')

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


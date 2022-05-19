from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import settings

engine = create_engine(settings.TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

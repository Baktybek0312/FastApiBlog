from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import TEST_SQLALCHEMY_DATABASE_URL


engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


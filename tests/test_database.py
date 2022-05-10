from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost:5432/blog_db"

engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

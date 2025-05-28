import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.database import Base


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:Emma@2025@localhost:5432/health_simplified_db"
)

@pytest.fixture(scope="function")
def session():
    engine = create_engine(DATABASE_URL)
    TestingSessionLocal = sessionmaker(bind=engine)


    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


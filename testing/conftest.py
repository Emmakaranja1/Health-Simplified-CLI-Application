import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.database import Base
from models import users, goals, food_entries, meals_plans

# Create a separate engine for testing (you should use a separate test DB in .env)
TEST_DATABASE_URL="postgresql://postgres:Emma2025@localhost:5432/health_simplified_db_test"


engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    # Create tables before any test
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after all tests complete
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()

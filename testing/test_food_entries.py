import pytest
from datetime import date, datetime
from models.food_entries import FoodEntry, FoodEntryModel
from db.database import SessionLocal, Base, engine
from models.users import UserModel  # Use the ORM class, not the dataclass

@pytest.fixture(scope="module")
def session():
    # Create tables based on ORM models
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)

def test_create_food_entry(session):
    from models.food_entries import FoodEntryModel

    user = UserModel(name="George")
    session.add(user)
    session.commit()  # To generate user.id

    # Create a FoodEntryModel instance
    entry = FoodEntryModel(
        user_id=user.id,
        food="Apple",
        calories=95,
        entry_date=date.today()
    )
    session.add(entry)
    session.commit()

    # Fetch and verify
    fetched = session.query(FoodEntryModel).filter_by(food="Apple").first()
    assert fetched is not None
    assert fetched.calories == 95

def test_update_food_entry(session):
    from models.food_entries import FoodEntryModel

    # Create and add a user
    user = UserModel(name="Hannah")
    session.add(user)
    session.commit()

    # Create and add a food entry as ORM model
    entry = FoodEntryModel(
        user_id=user.id,
        food="Banana",
        calories=100,
        entry_date=date.today()
    )
    session.add(entry)
    session.commit()

    # Update the ORM object
    entry.calories = 105
    session.commit()

    # Fetch and verify the update
    updated = session.query(FoodEntryModel).filter_by(id=entry.id).first()
    assert updated.calories == 105



import pytest
from datetime import datetime
from models.meals_plans import MealPlan
from controllers import meals_plans
from db.database import SessionLocal, Base, engine
from models.users import User


@pytest.fixture(scope="module")
def session():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    # Drop all tables after tests
    Base.metadata.drop_all(bind=engine)

def test_create_meal_plan(test_db_session, Base):
    # ... (your test code) ...
    user = User(name="Test User")  # Create a User object
    test_db_session.add(user)
    test_db_session.commit()

    meal_plan = MealPlan(user_id = user.id, name="Test Meal Plan") # Important: Use user.id, not a hardcoded ID.
    test_db_session.add(meal_plan)
    test_db_session.commit()


def test_update_meal_plan(session):
    # Create a user
    user = User(name="Eve")
    session.add(user)
    session.commit()

    # Create a meal plan
    plan = MealPlan(user_id=user.id, week_number=2)
    session.add(plan)
    session.commit()

    # Update the plan
    plan.description = "Updated description"
    session.commit()

    # Verify update
    updated = session.query(MealPlan).filter_by(id=plan.id).first()
    assert updated.description == "Updated description"

def test_delete_meal_plan(session):
    # Create a user
    user = User(name="Frank")
    session.add(user)
    session.commit()

    # Create a meal plan
    plan = MealPlan(user_id=user.id, week_number=3)
    session.add(plan)
    session.commit()

    # Delete the plan
    session.delete(plan)
    session.commit()

    # Verify deletion
    deleted = session.query(MealPlan).filter_by(id=plan.id).first()
    assert deleted is None
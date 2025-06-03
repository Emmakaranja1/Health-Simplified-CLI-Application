import pytest
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from models.meals_plans import MealPlan
from models.users import User
from controllers import users
from db.database import SessionLocal, Base, engine


@pytest.fixture(scope="module")
def session():
    # Create all tables in the test database
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    # Drop all tables after tests
    Base.metadata.drop_all(bind=engine)

def test_create_meal_plan(session):
    # Create a user
    user = User(name="Dana")
    session.add(user)
    session.commit()  # Save user to generate ID

    # Create a meal plan linked to the user
    plan = MealPlan(user_id=user.id, week_number=1, description="Plan 1")
    session.add(plan)
    session.commit()

    # Verify creation
    result = session.query(MealPlan).filter_by(user_id=user.id).first()
    assert result is not None
    assert result.week_number == 1
    assert result.description == "Plan 1"


def test_update_meal_plan(session):
    # ... (code to create a user and meal plan)

    # Update the meal plan
    meal_plan = session.query(MealPlan).filter_by(user_id=user.id).first()
    meal_plan.description = "Updated plan"
    session.add(meal_plan)
    session.commit()

    # Verify the update
    updated_plan = session.query(MealPlan).filter_by(user_id=user.id).first()
    assert updated_plan.description == "Updated plan"



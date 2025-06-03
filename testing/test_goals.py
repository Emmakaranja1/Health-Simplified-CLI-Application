import pytest
from psycopg2._psycopg import IntegrityError

from models.goals import Goal, GoalModel
from controllers import goals
from db.database import SessionLocal, Base, engine
from models.users import User, UserModel


@pytest.fixture(scope="module")
def session():
    # Create tables
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_goal(session):
    # Create a user (crucial for the foreign key constraint)
    user = UserModel(name="Test User")
    session.add(user)
    session.commit()  # Commit to create the user in the database


    try:
        new_goal = GoalModel(user_id=user.id, daily_goal="Daily Task")
        session.add(new_goal)
        session.commit()
        assert new_goal.id is not None  # Check if the goal was created successfully
    except IntegrityError as e:
        pytest.fail(f"Failed to create goal: {e}")
    finally:
        try:
            session.rollback()  # Crucial for cleanup in case of failure
        except Exception as e:
            print(f"Error during rollback: {e}")



def test_update_goal(session):
    # 1. Create a user (Crucial!)
    user = UserModel(name="Test User")
    session.add(user)
    session.commit()

    # 2. Create a goal for that user
    goal = GoalModel(user_id=user.id, daily_goal="Original Task")
    session.add(goal)
    session.commit()

    # 3. Update the goal
    goal.daily_goal = "Updated Task"
    session.add(goal)  # Important: Add the updated object
    session.commit()

    # 4. Verify the update
    updated_goal = session.query(GoalModel).get(goal.id)
    assert updated_goal.daily_goal == "Updated Task"



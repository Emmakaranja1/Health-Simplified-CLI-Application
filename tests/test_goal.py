from models.goal import GoalModel
from services.goal_service import create_goal, get_goal
from models.user import UserModel
from dataclasses import asdict

def test_create_and_get_goal(session):
    user = UserModel(name="Bob").create(session)

    goal = GoalModel(
        user_id=user.id,
        daily_goal="Read",
        weekly_goal="Write")
    created_goal = goal.create(session)

    fetched_goal = get_goal(created_goal.id, session)

    assert fetched_goal.daily_goal == "Read"
    assert fetched_goal.user_id == user.id

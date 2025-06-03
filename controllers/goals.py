from sqlalchemy.orm import Session

from models import UserModel
from models.goals import GoalModel, Goal
from db.database import get_db


# List all goals
def list_goals(session: Session, user_name: str):
    user = session.query(UserModel).filter(UserModel.name == user_name).first()
    if not user:
        return []
    return session.query(GoalModel).filter(GoalModel.user_id == user.id).all()

# Get one goal by id
def get_goal(goal_id: int, session: Session):
    goal = session.query(GoalModel).filter(GoalModel.id == goal_id).first()
    if goal:
        return Goal(
            id=goal.id,
            user_id=goal.user_id,
            daily_goal=goal.daily_goal,
            weekly_goal=goal.weekly_goal,
            created_at=goal.created_at,
        )
    return None


# Create a new goal
def create_goal(goal_data: Goal, session: Session):
    new_goal = GoalModel(
        user_id=goal_data.user_id,
        daily_goal=goal_data.daily_goal,
        weekly_goal=goal_data.weekly_goal,
    )
    result = new_goal.create(session)
    return result


# Update existing goal
def update_goal(goal_id: int, goal_data: Goal, session: Session):
    goal = session.query(GoalModel).filter(GoalModel.id == goal_id).first()
    if goal:
        goal.user_id = goal_data.user_id
        goal.daily_goal = goal_data.daily_goal
        goal.weekly_goal = goal_data.weekly_goal
        return goal.update(session)
    return None


# Delete a goal
def delete_goal(goal_id: int, session: Session):
    goal = session.query(GoalModel).filter(GoalModel.id == goal_id).first()
    if goal:
        return goal.delete(session)
    return None


def set_goal(db: Session, user_name: str, daily: str, weekly: str):
    user_obj = db.query(UserModel).filter(UserModel.name == user_name).first()
    if not user_obj:
        return False  # or raise an error if preferred

    goal = db.query(GoalModel).filter(GoalModel.user_id == user_obj.id).first()
    if goal:
        goal.daily_goal = daily
        goal.weekly_goal = weekly
    else:
        goal = GoalModel(user_id=user_obj.id, daily_goal=daily, weekly_goal=weekly)
        db.add(goal)

    db.commit()
    return True
    return None
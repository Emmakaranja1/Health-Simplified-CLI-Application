from sqlalchemy.orm import Session
from models.meal_plan import MealPlanModel, MealPlan
from db.database import get_db


# List all meal plans
def list_meal_plans(session: Session):
    plans = session.query(MealPlanModel).all()
    # Optionally convert to dataclass instances
    # return [MealPlan(id=p.id, user_id=p.user_id, week_number=p.week_number, description=p.description, created_at=p.created_at) for p in plans]
    return plans


# Get one meal plan by id
def get_meal_plan(plan_id: int, session: Session):
    plan = session.query(MealPlanModel).filter(MealPlanModel.id == plan_id).first()
    if plan:
        return MealPlan(
            id=plan.id,
            user_id=plan.user_id,
            week_number=plan.week_number,
            description=plan.description,
            created_at=plan.created_at,
        )
    return None


# Create a new meal plan
def create_meal_plan(plan_data: MealPlan, session: Session):
    new_plan = MealPlanModel(
        user_id=plan_data.user_id,
        week_number=plan_data.week_number,
        description=plan_data.description
    )
    result = new_plan.create(session)
    return result


# Update existing meal plan
def update_meal_plan(plan_id: int, plan_data: MealPlan, session: Session):
    plan = session.query(MealPlanModel).filter(MealPlanModel.id == plan_id).first()
    if plan:
        plan.user_id = plan_data.user_id
        plan.week_number = plan_data.week_number
        plan.description = plan_data.description
        return plan.update(session)
    return None


# Delete a meal plan
def delete_meal_plan(plan_id: int, session: Session):
    plan = session.query(MealPlanModel).filter(MealPlanModel.id == plan_id).first()
    if plan:
        return plan.delete(session)
    return None

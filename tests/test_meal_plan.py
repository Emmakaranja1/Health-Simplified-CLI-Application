from models.meal_plan import MealPlanModel
from services.meal_plan_service import create_meal_plan, get_meal_plan
from models.user import UserModel

def test_create_and_get_meal_plan(session):
    user = UserModel(name="Diana").create(session)

    plan = MealPlanModel(
        user_id=user.id,
        week_number=22,
        description="Low-carb")
    created_plan = plan.create(session)

    fetched_plan = get_meal_plan(created_plan.id, session)

    assert fetched_plan.week_number == 22
    assert fetched_plan.description == "Low-carb"

from models.food_entry import FoodEntryModel
from services.food_entry_service import create_food_entry, get_food_entry
from models.user import UserModel
from datetime import date

def test_create_and_get_food_entry(session):

    user = UserModel(name="James").create(session)


    entry = FoodEntryModel(
        user_id=user.id,
        food="Banana",
        calories=100,
        entry_date=date.today()
    )
    created_entry = entry.create(session)


    fetched_entry = get_food_entry(created_entry.id, session)


    assert fetched_entry.food == "Banana"
    assert fetched_entry.calories == 100
    assert fetched_entry.user_id == user.id

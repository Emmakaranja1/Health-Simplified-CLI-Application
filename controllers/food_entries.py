#Controllers = App logic like checking if user exists, calling model methods
from sqlalchemy.orm import Session

from models import UserModel
from models.food_entries import FoodEntryModel, FoodEntry
from db.database import get_db


# List all food entries
def list_food_entries(session: Session, user: str = None, date: str = None):
    query = session.query(FoodEntryModel)

    if user:
        user_record = session.query(UserModel).filter_by(name=user).first()
        if not user_record:
            print("❌ User not found.")
            return []
        query = query.filter(FoodEntryModel.user_id == user_record.id)

    if date:
        query = query.filter(FoodEntryModel.entry_date == date)

    entries = query.all()

    return [
        FoodEntry(
            id=e.id,
            user_id=e.user_id,
            food=e.food,
            calories=e.calories,
            entry_date=e.entry_date
        )
        for e in entries
    ]

# Get one food entry by id
def get_food_entry(entry_id: int, session: Session):
    entry = session.query(FoodEntryModel).filter(FoodEntryModel.id == entry_id).first()
    if entry:
        return FoodEntry(
            id=entry.id,
            user_id=entry.user_id,
            food=entry.food,
            calories=entry.calories,
            entry_date=entry.entry_date,
        )
    return None


# Create a new food entry
def create_food_entry(entry_data: FoodEntry, session: Session):
    new_entry = FoodEntryModel(
        user_id=entry_data.user_id,
        food=entry_data.food,
        calories=entry_data.calories,
        entry_date=entry_data.entry_date,
    )
    result = new_entry.create(session)
    return result


def update_food_entry(entry_id: int, entry_data: FoodEntry, session: Session):
    entry = session.query(FoodEntryModel).filter(FoodEntryModel.id == entry_id).first()
    if entry:
        entry.user_id = entry_data.user_id
        entry.food = entry_data.food
        entry.calories = entry_data.calories
        entry.entry_date = entry_data.entry_date
        session.commit()
        return True
    return False


# Delete a food entry
def delete_food_entry(entry_id: int, session: Session):
    entry = session.query(FoodEntryModel).filter(FoodEntryModel.id == entry_id).first()
    if entry:
        return entry.delete(session)
    return None

def add_food_entry(session: Session, user: str, food: str, calories: int, date: str):
    new_entry = FoodEntryModel(
        user_id=user,
        food=food,
        calories=calories,
        entry_date=date
    )
    session.add(new_entry)
    session.commit()
    session.refresh(new_entry)
    return FoodEntry(
        id=new_entry.id,
        user_id=new_entry.user_id,
        food=new_entry.food,
        calories=new_entry.calories,
        entry_date=new_entry.entry_date
    )
from sqlalchemy.orm import Session
from models.food_entries import FoodEntryModel, FoodEntry
from db.database import get_db


# List all food entries
def list_food_entries(session: Session):
    entries = session.query(FoodEntryModel).all()
    # Optionally convert to dataclass instances
    # return [FoodEntry(id=e.id, user_id=e.user_id, food=e.food, calories=e.calories, entry_date=e.entry_date) for e in entries]
    return entries


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


# Update existing food entry
def update_food_entry(entry_id: int, entry_data: FoodEntry, session: Session):
    entry = session.query(FoodEntryModel).filter(FoodEntryModel.id == entry_id).first()
    if entry:
        entry.user_id = entry_data.user_id
        entry.food = entry_data.food
        entry.calories = entry_data.calories
        entry.entry_date = entry_data.entry_date
        return entry.update(session)
    return None


# Delete a food entry
def delete_food_entry(entry_id: int, session: Session):
    entry = session.query(FoodEntryModel).filter(FoodEntryModel.id == entry_id).first()
    if entry:
        return entry.delete(session)
    return None

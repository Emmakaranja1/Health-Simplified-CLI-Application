from dataclasses import dataclass
from typing import Optional
from datetime import date
from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from db.database import Base


@dataclass
class FoodEntry:
    id: Optional[int]
    user_id: int
    food: str
    calories: int
    entry_date: date


class FoodEntryModel(Base):
    __tablename__: str = 'food_entries'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    food = Column(Text, nullable=False)
    calories = Column(Integer, nullable=False)
    entry_date = Column(Date, nullable=False)

   # def(self, user_id, food, calories, entry_date):
        #self.user_id = user_id
        #self.food = food
        #self.calories = calories
        #self.entry_date = entry_date

    def __repr__(self):
        return (f"<FoodEntry(id={self.id}, user_id={self.user_id}, "
                f"food='{self.food}', calories={self.calories}, "
                f"entry_date={self.entry_date})>")

    def create(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        print(f"Food entry '{self.food}' has been added successfully!")
        return self

    def update(self, session):
        session.commit()
        session.refresh(self)
        print(f"Food entry '{self.food}' has been updated successfully!")
        return self

    def delete(self, session):
        session.delete(self)
        session.commit()
        print(f"Food entry '{self.food}' has been deleted successfully!")
        return True
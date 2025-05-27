from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from db.database import Base


@dataclass
class MealPlan:
    id: Optional[int]
    user_id: int
    week_number: int
    description: Optional[str]
    created_at: Optional[datetime] = None


class MealPlanModel(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    week_number = Column(Integer, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id, week_number, description=None):
        self.user_id = user_id
        self.week_number = week_number
        self.description = description

    def __repr__(self):
        return (f"<MealPlan(id={self.id}, user_id={self.user_id}, "
                f"week_number={self.week_number}, description='{self.description}', "
                f"created_at={self.created_at})>")


    def create(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        print(f"Meal plan for week {self.week_number} has been added successfully!")
        return self

    def update(self, session):
        session.commit()
        session.refresh(self)
        print(f"Meal plan for week {self.week_number} has been updated successfully!")
        return self

    def delete(self, session):
        session.delete(self)
        session.commit()
        print(f"Meal plan for week {self.week_number} has been deleted successfully!")
        return True
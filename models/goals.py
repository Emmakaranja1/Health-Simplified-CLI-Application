from dataclasses import dataclass
from typing import Optional, Any
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text
from db.database import Base


@dataclass
class Goal:
    id: Optional[int]
    user_id: int
    daily_goal: Optional[str] = None
    weekly_goal: Optional[str] = None
    created_at: Optional[datetime] = None


class GoalModel(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    daily_goal = Column(Text, nullable=True)    # Changed to Text and nullable
    weekly_goal = Column(Text, nullable=True)   # Changed to Text and nullable
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id, daily_goal=None, weekly_goal=None):
        self.user_id = user_id
        self.daily_goal = daily_goal
        self.weekly_goal = weekly_goal

    def __repr__(self):
        return (f"<Goal(id={self.id}, user_id={self.user_id}, "
                f"daily_goal={self.daily_goal}, weekly_goal={self.weekly_goal}, "
                f"created_at={self.created_at})>")

    def create(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        print(f"Goal for user {self.user_id} has been added successfully!")
        return self

    def update(self, session):
        session.commit()
        session.refresh(self)
        print(f"Goal for user {self.user_id} has been updated successfully!")
        return self

    def delete(self, session):
        session.delete(self)
        session.commit()
        print(f"Goal for user {self.user_id} has been deleted successfully!")
        return True


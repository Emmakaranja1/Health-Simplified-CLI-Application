from dataclasses import dataclass
from typing import Optional
from sqlalchemy import Column, Integer, Text
from db.database import Base

# Data class used for DTO or plain data manipulation
@dataclass
class User:
    id: Optional[int]
    name: str

# SQLAlchemy ORM model
class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

    def create(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        print(f"User '{self.name}' has been added successfully!")
        return self

    def update(self, session):
        session.commit()
        session.refresh(self)
        print(f"User '{self.name}' has been updated successfully!")
        return self

    def delete(self, session):
        session.delete(self)
        session.commit()
        print(f"User '{self.name}' has been deleted successfully!")
        return True
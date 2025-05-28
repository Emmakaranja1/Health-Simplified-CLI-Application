from sqlalchemy.orm import Session
from models.user import UserModel, User
from db.database import get_db


# List all users
def list_users(session: Session = next(get_db())):
    users = session.query(UserModel).all()
    # Optionally convert to dataclass instances using list comprehension
    # return [User(id=user.id, name=user.name) for user in users]
    return users


# Get one user by id
def get_user(user_id: int, session: Session = next(get_db())):
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        return User(id=user.id, name=user.name)
    return None


# Create a new user
def create_user(user_data: User, session: Session = next(get_db())):
    new_user = UserModel(name=user_data.name)
    result = new_user.create(session)
    return result


# Update existing user
def update_user(user_id: int, user_data: User, session: Session = next(get_db())):
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        user.name = user_data.name
        return user.update(session)
    return None


# Delete a user
def delete_user(user_id: int, session: Session = next(get_db())):
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        return user.delete(session)
    return None

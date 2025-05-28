from models.user import UserModel
from services.user_service import create_user, get_user

def test_create_and_get_user(session):
    user_data = UserModel(name="Emma")
    created_user = user_data.create(session)
    fetched_user = get_user(created_user.id, session)

    assert fetched_user.name == "Emma"
    assert fetched_user.id == created_user.id

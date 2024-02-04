from app.config import SessionLocal
from app.model.user import User
from app.services.user_services import get_all_users
from app.services.user_services import get_user_by_id
from app.services.user_services import remove_user
from app.services.user_services import add_new_user
from app.services.user_services import get_user_by_document

def test_add_new_user():
    user = User()
    user.name = "teste"
    user.document = "00000000000"

    add_new_user(SessionLocal(), user)
    
    created_user = get_user_by_document(SessionLocal(), user.document)
    
    assert created_user
    
    
def test_remove_user():
    assert 1 ==1
def test_get_user_by_id():...
def test_get_all_users():...

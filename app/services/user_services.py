from model.user import User
from sqlalchemy.orm import sessionmaker



def add_new_user(db: sessionmaker, new_user_data: User) -> str:
    new_user = User()
    new_user.name = new_user_data['name']
    new_user.document = new_user_data['document']

    db.add(new_user)
    db.commit()
    db.close_all()
    return f"Usuário {new_user_data['name']} - Cadastrado."

def remove_user(db: sessionmaker, user_data: User) -> str:
    db.delete(user_data)
    db.commit()
    
    db.close_all()
    return f"Usuário {user_data.name} - Removido."

def get_user_by_id(db: sessionmaker, id: str) -> User:
    data = db.query(User).filter(User.id == id).first()
    db.close_all()
    return data

def get_all_users(db: sessionmaker) -> 'list[User]':
    data = db.query(User).all()
    db.close_all()

    return data

from model.user import User
from sqlalchemy.orm import sessionmaker


class UserService:
    def add_new_user(db: sessionmaker, new_user_data: User) -> str:
        new_user = User()
        new_user.name = new_user_data.name
        new_user.document = new_user_data.document
        new_user.password = new_user_data.password

        db.add(new_user)
        db.commit()

        return f"Usuário {new_user_data.name} - Cadastrado."

    def remove_user(db: sessionmaker, user_data: User) -> str:
        db.delete(user_data)
        db.commit()
    
    def get_user_by_id(db: sessionmaker, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()
    
    def get_all_users(db: sessionmaker) -> 'list[User]':
        return db.query(User).all()

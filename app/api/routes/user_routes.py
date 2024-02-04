from flask import jsonify, request
from config import SessionLocal

from schemas.user_schema import UserSchema
from model.user import User
from services.user_services import add_new_user
from services.user_services import remove_user
from services.user_services import get_user_by_id
from services.user_services import get_all_users


def create_user() -> str:
    data: User = request.get_json()
    user_schema = UserSchema()
    errors = user_schema.validate(data)
    
    if errors:
        return jsonify({'errors': errors}), 400
    
    user_data: dict = user_schema.load(data)
    result: str = add_new_user(SessionLocal(), user_data)
    return jsonify({"Response": result}), 200

def delete_user(id: str) -> str:
    user = get_user_by_id(SessionLocal(), id)
    delete = remove_user(SessionLocal(), user)

    return jsonify({"Response": delete}), 200

def get_all() -> 'list[dict]':
    result: 'list[User]'= get_all_users(SessionLocal())
    user_schema = UserSchema(many=True)
    user_data: 'list[dict]' = user_schema.dump(result)
    
    return jsonify({"Response": user_data}), 200 
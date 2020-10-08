from .. import db
from flask_login import current_user
from ..models import User, FavList


def create_user(data):
    new_user = User(name=data["name"],
                    email=data["email"],
                    phone=data["phone"],
                    password=data["password"])
    db.session.add(new_user)
    db.session.commit()
    return 'User saved'


def update_user(id, data):
    user = User.get(id)
    if not user:
        return 'Not user found'
    user.name = data["name"]
    user.email = data["email"]
    user.phone = data["phone"]
    password = data["password"]
    db.session.commit()
    return 'User updated'


def delete_user(id):
    user = User.get(id)
    if not user:
        return 'Not user found'
    db.session.delete(user)
    db.session.commit()
    return 'User deleted'


def get_user(id):
    user = User.query.get(id)
    if user:
        return user
    return 'User not found'
from .. import db
from flask_login import current_user, login_user
from ..models import Refuge
from .password_service import check_password, hash_password


def email_exists(email):
    refuge = db.session.query(Refuge).filter(Refuge.email == email).first()
    if refuge:
        return True
    else:
        return False


def get_refuges():
    refuges = Refuge.query.all()
    return refuges


def get_refuge(id):
    refuge = Refuge.query.get(id)
    if not refuge:
        msg = 'Refuge not found'
        return msg
    return refuge


def create_refuge(data):
    if not email_exists(data["email"]):
        hashed = hash_password(data["password"])
        new_refuge = Refuge(name=data["name"],
                            phone=data["phone"],
                            email=data["email"],
                            address=data["address"],
                            password=hashed)
        db.session.add(new_refuge)
        db.session.commit()
        msg = 'Refuge Created.'
        return msg
    else:
        return "The email  is already in use"


def update_refuge(id, data):
    updated_refuge = Refuge.query.get(id)
    if not updated_refuge:
        return 'No refuge found'
    updated_refuge.name = data["name"]
    updated_refuge.phone = data["phone"]
    updated_refuge.email = data["email"]
    updated_refuge.address = data["address"]
    db.session.commit()
    return 'Refuge updated'


def delete_refuge(id):
    refuge = Refuge.query.get(id)
    if refuge:
        db.session.delete(refuge)
        db.session.commit()
        return 'Refuge Deleted'
    return 'Refuge not found'


def login_refuge(email, password):
    if email and password:
        refuge = db.session.query(Refuge).filter_by(email=email).first()
        print(refuge.name)
        print(refuge.password)
        if refuge:
            if check_password(refuge.password, password):
                login_user(refuge)
                return "Logged in"
            else:
                return "Wrong Username or Password"
        else:
            return "Wrong Username or Password"
    else:
        return "Invalid Data"

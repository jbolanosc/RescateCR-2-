from .. import db
from flask_login import current_user
from ..models import Refuge


def get_refuges():
    refuges = Refuge.query.all()
    return refuges


def get_refuge(id):
    refuge = Refuge.get_by_id(id)
    if not refuge:
        msg = 'Refuge not found'
        return msg
    return refuge


def create_refuge(data):
    new_refuge = Refuge(name=data["name"],
                        phone=data["phone"],
                        email=data["email"],
                        address=data["address"])
    db.session.add(new_refuge)
    db.session.commit()
    msg = 'Refuge Created.'
    return msg


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

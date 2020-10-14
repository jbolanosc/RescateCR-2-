from .. import db, login_manager
from flask_login import UserMixin


class Refuge(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    phone = db.Column(db.String())
    email = db.Column(db.String)
    address = db.Column(db.String)
    password = db.Column(db.String)
    animals = db.relationship('Animal', backref="refuge.animals")
    employees = db.relationship('Employee', backref='refuge.employees')

    def __init__(self, name, phone, email, address, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'animals': self.animals,
            'employees': self.employees
        }

    @login_manager.user_loader
    def load_user(self, refuge_id):
        if refuge_id is not None:
            refuge = Refuge.query.get(refuge_id)
            return refuge
        return None
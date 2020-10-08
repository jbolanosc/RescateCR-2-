from .. import db


class Refuge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    phone = db.Column(db.String())
    email = db.Column(db.String)
    address = db.Column(db.String)
    animals = db.relationship('Animal', backref="refuge.animals")
    employees = db.relationship('Employee', backref='refuge.employees')

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

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
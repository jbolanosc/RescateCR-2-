from .. import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    phone = db.Column(db.String())
    email = db.Column(db.String())
    refuge = db.Column(db.Integer(), db.ForeignKey("refuge.id"))
    role = db.Column(db.Integer())
    password = db.Column(db.String())

    def __init__(self, name, phone, email, refuge, role, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.refuge = refuge
        self.role = role
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'refuge': self.refuge,
            'role': self.role,
            'password': self.password
        }
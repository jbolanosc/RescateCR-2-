from .. import db, login_manager
from flask_login import UserMixin


class Employee(UserMixin, db.Model):
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

    @login_manager.user_loader
    def load_employee(employee_id):
        if employee_id is not None:
            employee = Employee.query.get(employee_id)
            return employee
        return None
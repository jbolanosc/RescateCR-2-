from .. import db
from flask_login import current_user
from ..models import Employee, Refuge


def get_employee(id):
    employee = Employee.get(id)
    if employee:
        return employee
    return 'Employee not found.'


def update_employee(id, data):
    employee = Employee.get(id)
    if not employee:
        return 'Employee not found.'

    employee.name = data["name"]
    employee.phone = data["phone"]
    employee.email = data["email"]
    employee.refuge = data["refuge"]
    employee.role = data["role"]
    employee.password = data["password"]

    db.session.commit()
    return 'Employee updated.'


def delete_employee(id):
    employee = Employee.get(id)
    if not employee:
        return 'Employee not found.'
    db.session.delete(employee)
    db.session.commit()


def create_employee(data):
    new_employee = Employee(name=data["name"],
                            phone=data["phone"],
                            email=data["email"],
                            refuge=data["refuge"],
                            role=data["role"],
                            password=data["password"])
    db.session.add(new_employee)
    db.session.add()
    return 'Employee saved'

from .. import db
from flask_login import current_user, login_user
from ..models import Employee, Refuge
from .password_service import check_password, hash_password


def get_employee(id):
    employee = Employee.get(id)
    if employee:
        return employee
    return 'Employee not found.'


def login_employee(email, password):
    if email and password:
        employee = db.session.query(Employee).filter_by(email=email).fi
        if employee:
            if check_password(employee.password, password):
                login_user(employee)
            else:
                return 'Wrong Username or password'
        else:
            return 'Invalid Username or Password'
    else:
        return 'Invalid data'


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
                            password=hash_password(data["password"]))
    db.session.add(new_employee)
    db.session.add()
    return 'Employee saved'

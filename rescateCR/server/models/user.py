from .. import db, login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.String())
    password = db.Column(db.String())
    favList = db.relationship('FavList', backref='user.favList')
    animals = db.relationship('Animal', backref='user.animals')

    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'favList': self.favList,
            'animals': self.animals
        }

    @login_manager.user_loader
    def load_user(user_id):
        if user_id is not None:
            user = User.query.get(user_id)
            return user
        return None
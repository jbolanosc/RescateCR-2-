from .. import db


class User(db.Model):
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

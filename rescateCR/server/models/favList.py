from .. import db


class FavList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.Integer)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, animal, user):
        self.id = id
        self.animal = animal
        self.user = user

    def serialize(self):
        return {'id': self.id, 'animal': self.animal, 'user': self.user}

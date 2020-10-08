from .. import db


class Animal(db.Model):
    __tablename__ = 'Animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    photos = db.Column(db.String())
    refuge = db.Column(db.Integer, db.ForeignKey('refuge.id'))
    adopted = db.Column(db.Boolean)
    size = db.Column(db.String())
    animal_type = db.Column(db.String())
    breed = db.Column(db.String())
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, name, photos, refuge, adopted, size, animal_type, breed,
                 owner):
        self.name = name
        self.photos = photos
        self.refuge = refuge
        self.adopted = adopted
        self.size = size
        self.animal_type = animal_type
        self.breed = breed
        self.owner = owner

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'photos': self.photos,
            'refuge': self.refuge,
            'adopted': self.adopted,
            'size': self.size,
            'animal type': self.animal_type,
            'breed': self.breed,
            'owner': self.owner
        }
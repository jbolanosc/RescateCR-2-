from .. import db
from flask_login import current_user
from ..models import Animal


def save_animal(animal):
    new_animal = Animal(name=animal["name"],
                        photos="",
                        refuge=current_user.id,
                        adopted=bool(animal["adopted"]),
                        size=animal["size"],
                        animal_type=animal["animal_type"],
                        breed=animal["breed"],
                        owner=None)
    db.session.add(new_animal)
    db.session.commit()
    msg = f'Animal {animal["name"]} saved.'
    return msg


def get_animal(id):
    animal = Animal.query.get(id)
    if animal:
        return animal
    return 'Animal not found.'


def get_animals():
    animals = Animal.query.all()
    return animals


def delete_animal(id):
    animal = Animal.query.filter(Animal.id == id).delete()
    db.session.commit()
    msg = "Animal deleted"
    return msg


def update_animal(id, data):
    animal = Animal.get(id)
    if animal:
        animal.name = data["name"]
        animal.photos = data["photos"]
        animal.refuge = data["refuge"]
        animal.adopted = data["adopted"]
        animal.size = data["size"]
        animal.breed = data["breed"]
        animal.owner = data["owner"]

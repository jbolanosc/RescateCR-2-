from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound
from flask_login import login_required
from ..services.animal_service import get_animals, get_animal, save_animal, update_animal, delete_animal

animal_page = Blueprint('animal_page', __name__, template_folder="templates")


@animal_page.route('/')
def index():
    try:
        animals = get_animals()
        #return jsonify([e.serialize() for e in animals])
        return render_template('animal/Animals.html')
    except Exception as e:
        return (str(e))


@animal_page.route('/<int:id>')
def get(id):
    try:
        animal = get_animal(id)
        return render_template('animal/Animal.html')
    except Exception as e:
        return (str(e))


@animal_page.route('/create', methods=["GET", "POST"])
@login_required
def create():
    try:
        if request.method == "POST":
            animal = request.form
            msg = save_animal(animal)
            return jsonify(msg)

        return render_template('animal/Animalform.html')
    except Exception as e:
        return (str(e))


@animal_page.route('/<int:id>/update', methods=["GET", "POST"])
@login_required
def update(id):
    try:
        if request.method == "POST":
            animal = request.form
            msg = update_animal(id, animal)
            return jsonify(msg)
        return render_template('animal/Animalform.html')
    except Exception as e:
        return (str(e))


@animal_page.route('/<int:id>/delete', methods=["DELETE"])
@login_required
def delete(id):
    try:
        msg = delete_animal(id)
        return jsonify(msg)
    except Exception as e:
        return (str(e))

from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from ..services.refuge_service import get_refuge, get_refuges, create_refuge, update_refuge, delete_refuge

refuge_page = Blueprint('refuge_page', __name__, template_folder="templates")


@refuge_page.route('/', methods=["GET"])
def get():
    try:
        refuges = get_refuges()
        return render_template('refuge/refuges.html', refuges=refuges)
    except Exception as e:
        return (str(e))


@refuge_page.route('/create', methods=["GET", "POST"])
def create():
    try:
        if request.method == 'POST':
            refuge = request.form
            msg = create_refuge(refuge)
            return jsonify(msg)
        return render_template('refuge/refugeForm.html')
    except Exception as e:
        return (str(e))


@refuge_page.route('/<int:id>/update', methods=["GET", "POST"])
def update(id):
    try:
        if request.method == 'POST':
            refuge = request.form
            msg = update_refuge(id, refuge)
            return jsonify(refuge)
        return render_template('refuge/refugeForm.html')
    except Exception as e:
        return (str(e))


@refuge_page.route('/<int:id>', methods=["GET"])
def get_one(id):
    try:
        refuge = get_refuge(id)
        return render_template('refuge/refuge.html', refuge=refuge)
    except Exception as e:
        return (str(e))


@refuge_page.route('/<int:id>/delete', methods=["DELETE"])
def delete(id):
    try:
        msg = delete_refuge(id)
        return jsonify(msg)
    except Exception as e:
        return (str(e))
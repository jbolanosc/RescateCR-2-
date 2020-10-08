from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required
from ..services.user_service import create_user, update_user, delete_user, get_user

user_page = Blueprint('user_page', __name__, template_folder="templates")


@user_page.route('/<int:id>', methods=["GET"])
def get(id):
    try:
        user = get_user(id)
    except Exception as e:
        return (str(e))


@user_page.route('/<int:id>/update', methods=["GET", "POST"])
def update(id):
    try:
        data = request.form
        msg = update_user(id, data)
        return jsonify(data)
    except Exception as e:
        return (str(e))


@user_page.route('/<int:id>/delete', methods=["DELETE"])
def delete(id):
    try:
        msg = delete_user(id)
        return jsonify(msg)
    except Exception as e:
        return (str(e))

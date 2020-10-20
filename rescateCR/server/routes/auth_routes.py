from flask import Blueprint, render_template, request, redirect, jsonify, flash
from flask_login import login_required, logout_user, current_user, login_user
from ..services.refuge_service import login_refuge

auth_page = Blueprint('auth_page', __name__, template_folder="templates")


@auth_page.route('/login_refuge', methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            msg = login_refuge(email, password)
            flash(msg)
            return redirect(f'/refuges/{current_user.id}')
        elif current_user.is_authenticated:
            refuge = current_user.id
            return redirect(f'/refuges/{current_user.id}')

        return render_template('auth/login.html')
    except Exception as e:
        return (str(e))


@auth_page.route('/register', methods=["GET", "POST"])
def register_user():
    try:
        if current_user.is_authenticated:
            refuge = current_user.refuge
            return redirect(f'/refuge/{current_user.id}')
        else:
            if request.method == "GET":
                return render_template('auth/login.html')
            else:
                if request.form["type"] == "Refuge":
                    return render_template('refuge/refugeForm.html')
                return True
    except Exception as e:
        return (str(e))


@auth_page.route('/logout', methods=["GET"])
def logout():
    logout_user()
    flash("Logout successfully")
    return redirect('/')
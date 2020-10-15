from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, logout_user, current_user, login_user
from ..services.refuge_service import login_refuge

auth_page = Blueprint('auth_page', __name__, template_folder="templates")


@auth_page.route('/login_refuge', methods=["GET", "POST"])
def login():
    try:
        if current_user.is_authenticated:
            refuge = current_user.refuge
            return redirect(f'/refuge/{current_user.id}')
        elif request.method == "GET":
            return render_template('auth/login.html')
        else:
            email = request.form["email"]
            password = request.form["password"]
            msg = login_refuge(email, password)
            return redirect(f'/refuges/{current_user.id}')
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


@auth_page.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return render_template('pages/index.html')
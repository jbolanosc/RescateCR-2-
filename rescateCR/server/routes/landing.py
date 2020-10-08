from flask import Blueprint, render_template

landing_page = Blueprint('landing_page', __name__, template_folder="templates")


@landing_page.route('/', methods=["GET"])
def get():
    return render_template('pages/index.html')
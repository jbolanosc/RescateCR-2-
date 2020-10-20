import os
from flask import Flask, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager()

from .routes import auth_page, landing_page, user_page, animal_page, refuge_page

app.register_blueprint(landing_page)
app.register_blueprint(user_page, url_prefix="/user")
app.register_blueprint(refuge_page, url_prefix="/refuges")
app.register_blueprint(animal_page, url_prefix="/animals")
app.register_blueprint(auth_page, url_prefix="/auth")

login_manager.login_view = "auth_page.login"
login_manager.init_app(app)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

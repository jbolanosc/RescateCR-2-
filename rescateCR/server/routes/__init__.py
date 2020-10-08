from .animal_routes import animal_page
from .user_routes import user_page
from .refuge_routes import refuge_page
from .landing import landing_page


def register_blueprints(app):
    app.register_blueprint(landing_page)
    app.register_blueprint(user_page, url_prefix="/user")
    app.register_blueprint(refuge_page, url_prefix="/refuges")
    app.register_blueprint(animal_page, url_prefix="/animals")
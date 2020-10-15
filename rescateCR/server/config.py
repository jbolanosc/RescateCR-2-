import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'askdj_fjeo_12*fkf'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    UPLOAD_FOLDER = "/static/updloads"
    ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

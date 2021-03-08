import os

BASE_DIR = os.path.dirname(__name__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'infos.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'dev'
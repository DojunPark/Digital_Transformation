# pip install Flask-Migrate

# Pybo에 ORM 적용
import os

BASE_DIR = os.path.dirname(__file__)    # 루트 디렉토리

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # 데이터베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 이벤트 처리 옵션


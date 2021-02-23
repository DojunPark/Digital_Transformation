import os

BASE_DIR = os.path.dirname(__file__)  # 현재 파일이 있는 경로

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # pybo.db 파일로 생성
SQLALCHEMY_TRACK_MODIFICATIONS = False    # 이벤트 처리(?) False로 설정
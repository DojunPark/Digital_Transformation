import os

# 데이터베이스 환경설정
# aql-alchemy: 데이터베이스를 객체로 생성하여 편하게 사용할 수 있음
# 각 데이터베이스마다 접근하는 방법이 다름
BASE_DIR = os.path.dirname(__file__)  # 현재 파일이 있는 경로
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # pybo.db 파일로 생성
SQLALCHEMY_TRACK_MODIFICATIONS = False    # 이벤트 처리(?) False로 설정
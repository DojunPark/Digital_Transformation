from flask import Flask

# ORM 적용
import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


# 애플리케이션 팩토리 사용
def create_app():
    app = Flask(__name__)

    # app에 ORM 적용
    app.config.from_object(config)  # 환경변수 설정
    db.init_app(app)
    migrate.init_app(app, db)

    # 데이터베이스 모델 가져오기
    from . import models

    # app에 Blueprint 등록
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app


# flask db init     데이터베이스 초기화 (migrations 디렉토리 생성)
# flask db migrate  모델 생성 및 변경 (db 파일 생성 / 리비전 파일 생성)
# flask db upgrade  모델의 변경 내옹을 데이터베이스에 적용 (리비전 파일 실행, db 갱신)


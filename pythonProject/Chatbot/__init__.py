from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from Chatbot import config

app = Flask(__name__)
app.config.from_object(config)
app.debug = True

# 데이터베이스 설정
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
migrate = Migrate()
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
db.init_app(app)

if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
    migrate.init_app(app, db, render_as_batch=True)
else:
    migrate.init_app(app, db)

# 라우트 등록
from Chatbot.views import main_views, titanic_views, iris_views
app.register_blueprint(main_views.bp)
app.register_blueprint(titanic_views.bp)
app.register_blueprint(iris_views.bp)

# 필터 등록
from Chatbot.filter import shortword
app.jinja_env.filters['shortword'] = shortword
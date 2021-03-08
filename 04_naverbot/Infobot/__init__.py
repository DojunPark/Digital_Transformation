from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config

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
from Infobot.views import book_views, movie_views, shopping_views
app.register_blueprint(book_views.bp)
app.register_blueprint(movie_views.bp)
app.register_blueprint(shopping_views.bp)

# 필터 등록
from Infobot.filter import shortword, price_parser, barhide
app.jinja_env.filters['shortword'] = shortword
app.jinja_env.filters['price_parser'] = price_parser
app.jinja_env.filters['barhide'] = barhide

@app.route('/')
def hello():
    return render_template('main.html')


from flask import Flask, render_template
from .views import title_views, author_views, movie_views
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
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()
db.init_app(app)

if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
    migrate.init_app(app, db, render_as_batch=True)
else:
    migrate.init_app(app, db)


from Bookbot.views import shopping_views

app.register_blueprint(title_views.bp)
app.register_blueprint(author_views.bp)
app.register_blueprint(movie_views.bp)
app.register_blueprint(shopping_views.bp)

# 필터 등록
from .filter import shortword, barhide, price_comma
app.jinja_env.filters['shortword'] = shortword
app.jinja_env.filters['barhide'] = barhide
app.jinja_env.filters['price_comma'] = price_comma


@app.route('/')
def hello():
    return render_template('main.html')
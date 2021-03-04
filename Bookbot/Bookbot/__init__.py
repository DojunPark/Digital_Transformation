from flask import Flask, render_template
from .views import title_views, author_views, movie_views
import config

app = Flask(__name__)

app.config.from_object(config)
app.debug = True
app.register_blueprint(title_views.bp)
app.register_blueprint(author_views.bp)
app.register_blueprint(movie_views.bp)

# 필터 등록
from .filter import shortword, barhide
app.jinja_env.filters['shortword'] = shortword
app.jinja_env.filters['barhide'] = barhide


@app.route('/')
def hello():
    return render_template('main.html')
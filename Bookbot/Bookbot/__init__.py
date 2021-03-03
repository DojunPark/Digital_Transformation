from flask import Flask, render_template
from .views import title_views, author_views
import config

app = Flask(__name__)

app.config.from_object(config)
app.debug = True
app.register_blueprint(title_views.bp)
app.register_blueprint(author_views.bp)

# 필터 등록
from .filter import shortword
app.jinja_env.filters['shortword'] = shortword


@app.route('/')
def hello():
    return render_template('main.html')
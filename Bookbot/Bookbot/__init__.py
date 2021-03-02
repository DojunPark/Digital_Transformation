from flask import Flask, render_template
from .views import title_views, author_views
import config

app = Flask(__name__)

app.config.from_object(config)
app.debug = True
app.register_blueprint(title_views.bp)
app.register_blueprint(author_views.bp)

@app.route('/')
def hello():
    return render_template('main.html')
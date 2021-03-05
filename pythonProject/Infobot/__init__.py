from flask import Flask, render_template

app = Flask(__name__)



from Infobot.views import book_views, movie_views, shopping_views

app.register_blueprint(book_views.bp)
app.register_blueprint(movie_views.bp)
app.register_blueprint(shopping_views.bp)



@app.route('/')
def hello():
    return render_template('main.html')


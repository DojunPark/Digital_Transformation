from flask import Blueprint, render_template

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/title')
def movie_title():
    return render_template('movie/movie_title.html')

@bp.route('/rank')
def movie_rank():
    return render_template('movie/movie_rank.html')

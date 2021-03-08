from flask import Blueprint, render_template, request
from Infobot.forms import MovieTitleForm
from Infobot.naver_api import n_get_idpw, n_movie_title, n_movie_rank

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/title', methods=('POST', 'GET'))
def movie_title():
    form = MovieTitleForm()
    if request.method == 'POST' and form.validate_on_submit():
        nid, npw = n_get_idpw()
        data = n_movie_title(form.movie_title.data, nid, npw)
        return render_template('movie/movie_title.html', form=form, data=data)
    return render_template('movie/movie_title.html', form=form)

@bp.route('/rank', methods=('POST', 'GET'))
def movie_rank():
    form = n_movie_rank()
    if request.method == 'POST':
        data = n_movie_rank()
        return render_template('movie/movie_rank.html', form=form, data=data)
    return render_template('movie/movie_rank.html', form=form)

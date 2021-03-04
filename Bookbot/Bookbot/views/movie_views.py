from flask import Blueprint, render_template, request
from Bookbot.naverapi import get_idpw, naver_movie, naver_movie_rank
from Bookbot.forms import MovieInfoForm
from Bookbot.filter import barhide

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/info', methods=('POST', 'GET'))
def movie_info():
    form = MovieInfoForm()
    if request.method == 'POST' and form.validate_on_submit():
        nid, npw = get_idpw()
        json = naver_movie(form.title.data, nid, npw)
        return render_template('movie_info.html', form=form, json=json)

    return render_template('movie_info.html', form=form)


@bp.route('/rank', methods=('POST', 'GET'))
def movie_rank():
    if request.method == 'POST':
        titles = naver_movie_rank()
        return render_template('movie_rank.html', titles = titles)

    return render_template('movie_rank.html')
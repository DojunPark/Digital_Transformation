from flask import Blueprint, render_template, request
from Infobot.forms import BookTitleForm, BookAuthorForm
from Infobot.naver_api import n_get_idpw, n_book_title, n_book_author

bp = Blueprint('book', __name__, url_prefix='/book')

@bp.route('/title', methods = ('POST', 'GET'))
def book_title():
    form = BookTitleForm()
    if request.method == 'POST' and form.validate_on_submit():
        nid, npw = n_get_idpw()
        data = n_book_title(form.book_title.data, nid, npw)
        return render_template('book/book_title.html', form=form, data=data)

    return render_template('book/book_title.html', form=form)


@bp.route('/author', methods = ('POST', 'GET'))
def book_author():
    form = BookAuthorForm()
    if request.method == 'POST' and form.validate_on_submit():
        nid, npw = n_get_idpw()
        data = n_book_author(form.book_author.data, nid, npw)
        return render_template('book/book_author.html', form=form, data=data)

    return render_template('book/book_author.html', form=form)

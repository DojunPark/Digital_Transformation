from flask import Blueprint, render_template, request
from Infobot.forms import BookTitleForm
from Infobot.naver_api import n_get_idpw, n_book_author

bp = Blueprint('book', __name__, url_prefix='/book')

@bp.route('/title')
def book_title():
    form = BookTitleForm()
    if request.mothod == 'POST' and form.validate_on_submit():
        nid, npw = n_get_idpw()
        data = n_book_author(form.book_title, nid, npw)
        return render_template('book/book_title.html', form=form, data=data)

    return render_template('book/book_title.html', form=form)


@bp.route('/author')
def book_author():
    return render_template('book/book_author.html')

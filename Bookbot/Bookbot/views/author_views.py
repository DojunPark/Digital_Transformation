from flask import Blueprint, render_template, request
from ..forms import AuthorForm
from Bookbot.naverapi import get_idpw, search_title

bp = Blueprint('author', __name__, url_prefix='/author')

@bp.route('/', methods=('POST', 'GET'))
def author_search():
    form = AuthorForm()
    # print(request.method)
    if request.method == 'POST' and form.validate_on_submit():
        nid, npw = get_idpw()
        df = search_title(form.author.data, nid, npw)
        return render_template('author.html', form=form, df=df)

    return render_template('author.html', form=form)
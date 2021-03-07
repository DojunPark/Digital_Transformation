from flask import Blueprint, render_template, request
from Bookbot.forms import TitleForm
from Bookbot.naverapi import get_idpw, search_title

bp = Blueprint('title', __name__, url_prefix='/book')

@bp.route('/', methods=('POST', 'GET'))
def title_search():
    form = TitleForm()
    print(request.method)
    if request.method == 'POST' and form.validate_on_submit():
        # print(form.title.data)
        nid, npw = get_idpw()
        df = search_title(form.title.data, nid, npw)
        return render_template('title.html', form=form, df=df)

    return render_template('title.html', form=form)
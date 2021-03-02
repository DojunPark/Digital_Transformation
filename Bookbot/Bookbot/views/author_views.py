from flask import Blueprint, render_template
from ..forms import SearchForm

bp = Blueprint('author', __name__, url_prefix='/author')

@bp.route('/')
def author_search():
    form = SearchForm()
    return render_template('author.html', form=form)
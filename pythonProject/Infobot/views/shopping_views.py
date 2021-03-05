from flask import Blueprint, render_template

bp = Blueprint('shopping', __name__, url_prefix='/shopping')

@bp.route('/title')
def shopping_title():
    return render_template('shopping/shopping_title.html')

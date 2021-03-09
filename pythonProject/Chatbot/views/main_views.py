from flask import Blueprint, render_template, request


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=('POST', 'GET'))
def index():
    if request.method == 'POST':
        return render_template('main.html')
    return render_template('main.html')
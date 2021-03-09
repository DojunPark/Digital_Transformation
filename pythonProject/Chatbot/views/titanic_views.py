from flask import Blueprint, render_template, request


bp = Blueprint('titanic', __name__, url_prefix='/titanic')

@bp.route('/', methods=('POST', 'GET'))
def predict():
    if request.method == 'POST' and form.validate_on_submit():
        return render_template('titanic.html')
    return render_template('titanic.html')
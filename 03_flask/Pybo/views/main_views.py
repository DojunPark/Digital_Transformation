# uri를 분석하고 uri에 따라 실행되는 함수를 정의하는 곳

from flask import Blueprint, render_template, url_for
from Pybo import db
from Pybo.models import Question, Answer
from datetime import datetime
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')   # url를 구분짓는 구분자 역할을 함

# @bp.route('/')
# def hello_pybo():
#     return 'hello, pybo! 안녕 파이보!'

@bp.route('/')
def index():
    return redirect(url_for('question.qlist'))   # question 블루프린트에서 qlist 함수로 주소를 넘김

@bp.route('/test')
def test():
    age_tmp = 10
    ls_tmp = list(range(10))
    return render_template('question/test.html', age=age_tmp, ls_data=ls_tmp)


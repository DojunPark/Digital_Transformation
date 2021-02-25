from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from Pybo import db
from Pybo.models import Question, Answer
from datetime import datetime

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
    for i in range(100):
        q = Question(subject='테스트입니다. {0}'.format(i), content='내용무', create_date=datetime.now())
        db.session.add(q)
    db.session.commit()
    return 'Success'


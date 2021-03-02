# 블루프린트로 라우트 함수 관리

from flask import Blueprint, render_template
from Pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    # 질문 목록 출력
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list) # question_list를 html 페이지로 전달

@bp.route('/hello')
def hello():
    return 'Hello, Pybo!'


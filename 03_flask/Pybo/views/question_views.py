from flask import Blueprint, render_template
from Pybo import db
from Pybo.models import Question, Answer
from datetime import datetime

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list')
def qlist():
    question_list = Question.query.order_by(Question.create_date.desc())
    print(question_list)
    # return 'Success'
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/add_question')
def add_question():
    q = Question(subject='궁금합니다~~', content='무엇이 궁금한지 알려주세요', create_date=datetime.now())
    db.session.add(q)
    db.session.commit()
    return 'Success'

@bp.route('/question/detail/<int:question_id>/')   # <자료형:변수명>
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    print(question.content)
    return render_template('question/question_detail.html', question=question)
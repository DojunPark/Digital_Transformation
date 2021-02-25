from flask import Blueprint, render_template, request, url_for
from Pybo import db
from Pybo.models import Question, Answer
from datetime import datetime
from werkzeug.utils import redirect
from ..forms import AnswerForm

bp = Blueprint('answer', __name__, url_prefix='/answer')  # 각각의 views마다 블루프린트를 따로 설정함

@bp.route('/create/<int:question_id>', methods = ('POST', ))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(question = question, content = content, create_date=datetime.now())
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_detail.html', question=question, form=form)





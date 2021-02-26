from flask import Blueprint, render_template, url_for, request, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from Pybo import db
from Pybo.models import Question, Answer, User
from Pybo.forms import UserCreateForm, UserLoginForm
from datetime import datetime
from werkzeug.utils import redirect

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.before_app_request
def load_logged_ina_user():
    user_id = session.get('user_id')
    
    # 로그인 정보 없음
    if user_id is None:
        g.user = None
    # 로그인 정보 있음
    else:
        g.user = User.query.get(user_id)

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data, password=generate_password_hash(form.password1.data), email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')

    return render_template('/auth/signup.html', form=form)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password, form.password.data):
            error = '비밀번호가 올바르지 않습니다.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))

        flash(error)


    return render_template('/auth/login.html', form=form)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


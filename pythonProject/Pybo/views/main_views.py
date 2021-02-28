# 블루프린트로 라우트 함수 관리

from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def pybo1():
    return 'Pybo index'

@bp.route('/hello')
def hello():
    return 'Hello, Pybo!'
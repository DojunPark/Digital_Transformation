from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')   # url를 구분짓는 구분자 역할을 함

@bp.route('/')
def hello_pybo():
    return 'hello, pybo! 안녕 파이보!'

@bp.route('/hello')
def hello_pybo1():
    return 'hello page 입니다.'




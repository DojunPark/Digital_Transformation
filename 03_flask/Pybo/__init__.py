from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config   # 환경설정

# 데이터베이스
db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)   # 데이터베이스 설정
app.debug = True    # 코드가 수정되면 서버 재실행

# ORM 데이터베이스 초기화
db.init_app(app)   # flask를 sqlalchemy에 넣음
migrate.init_app(app, db)  # flask와 db를 migrate에 넣음

from .views import main_views, question_views, answer_views   # uri 구분 실행 코드 실행
app.register_blueprint(main_views.bp)   # 블루프린트를 앱에 등록
app.register_blueprint(question_views.bp)   # 블루프린트를 앱에 등록
app.register_blueprint(answer_views.bp)


#
# #--------------------------------------------------------
# from . import models
# from Pybo.models import Question, Answer
# from datetime import datetime
#
# # @은 데코레이터
# # @app.route는 app앞에 route를 미리 사용하는 것 -> uri를 분석함
# # 데코레이터 아래는 항상 함수가 사용되고, 조건이 만족되면 아래 함수를 바로 사용하게 됨
# @app.route('/')
# def hello():
#     return 'hello Pybo!'
#
# @app.route('/examples')
# def examples():
#     # q = Question(subject='이것은 무엇인가요?', content='알려주세요 궁금합니다', create_date=datetime.now())  # 질문 입력
#     # q.subejct = '[질문] 무엇일까요?'  # subject 변경
#     # db.session.add(q)
#
#     # q = Question.query.all()    # 모든 데이터 가져오기
#     # print(q)
#     # print('id: ', q[0].id)
#     # print('subject: ', q[0].subject)
#     # print('date: ', q[0].create_date)
#
#     # q = Question.query.get(1)  # pk가 1번인 데이터를 가져옴
#     # print('id: ', q.id)
#     # print('subject: ', q.subject)
#     # print('date: ', q.create_date)
#
#     # q = Question.query.filter(Question.subject.like('%무엇%')).all()   # 제목에 "무엇"이 들어간 자료를 가져옴
#     # print('id: ', q[0])
#
#     # q = Question.query.get(1)   # 데이터의 subject를 수정
#     # q.subject = '질문내용1'
#     # db.session.commit()
#
#     # q = Question.query.get(1)   # 데이터 삭제
#     # db.session.delete(q)
#     # db.session.commit()
#
#     # q = Question.query.get(2)    # 답변 및 참조 가져오는 방법
#     # a = Answer(question=q, content='답변 생성입니다.', create_date=datetime.now())
#     # db.session.add(a)
#     # db.session.commit()
#
#     a = Answer.query.get(1)    # 답변에 해당하는 질문 가져오기
#     q = a.question
#     print(q.id)
#     print(q.subject)
#     print(q.create_date)
#
#     q_all = q.answer_set   # 모든 답변 가져오기
#     print(q_all)
#
#     return 'Success'    # http 프로토콜을 열어 결과값을 클라이언트에게 전달
#
# # 연습문제1: 질문을 입력하는 명령
# @app.route('/insert_question')
# def insert_question5():
#     for i in range(1, 6):
#         q = Question(subject='질문for문'+str(i), content='궁금합니다for문'+str(i), create_date=datetime.now())
#         db.session.add(q)
#
#     db.session.commit()
#     return '커밋 완료'
#
# # 연습문제2: 모든 질문을 조회
# @app.route('/find_question_all')
# def find_questions():
#     q = Question.query.all()    # 모든 데이터 가져오기
#     for i in range(len(q)):
#         print('id: ', q[i].id)
#         print('subject: ', q[i].subject)
#     print('완료')
#     return '모든 질문 조회 완료'
#
# # 연습문제3: for문 질문에 답변 입력
# @app.route('/insert_answer')
# def insert_answer():
#     q = Question.query.filter(Question.subject.like('%for문%')).all()  # 제목에 "무엇"이 들어간 자료를 가져옴
#     for i in range(len(q)):
#         a = Answer(question=q[i], content=str(i+1)+'번째 답변 추가', create_date=datetime.now())
#         db.session.add(a)
#
#     db.session.commit()
#     return '질문 답변 완료'
#
# # 연습문제4: 처음 3개 질문 삭제
# @app.route('/delete_questions')
# def delete_questions3():
#     q = Question.query.all()
#     for i in range(3):
#         db.session.delete(q[i])
#
#     db.session.commit()
#     return '질문 삭제 완료'
#
#
#
#

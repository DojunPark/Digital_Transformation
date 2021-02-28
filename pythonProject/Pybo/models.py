# 데이터베이스의 모델을 관리

from Pybo import db   # __init__에서 생성한 SQLAlchemy 객체

# Question 모델 - db의 Model 클래스를 상속받아 생성
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# Answer 모델
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Question 모델의 primary key / 질문 삭제시 함께 삭제
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # 답변 모델에서 질문 모델 참조 / 역참조 설정, 질문 삭제시 함께 삭제
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
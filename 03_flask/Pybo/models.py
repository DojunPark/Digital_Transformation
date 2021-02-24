from Pybo import db

# 클래스 형태로 데이터베이스 질문 테이블 생성
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary_key는 중복되지 않는 값임
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ForeignKey(외래값)는 다른 데이터테이블의 primary_key(고유값)를 사용하는 것
    # ondelete='CASCADE'는 answer에서 삭제되었을때 question에서도 삭제하는 것
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# 데이터베이스의 유저 테이블 클래스 생성
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(12), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)



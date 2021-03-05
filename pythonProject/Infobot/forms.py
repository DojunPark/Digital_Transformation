from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class BookTitleForm(FlaskForm):
    book_title = StringField('도서명을 입력하세요', validators=[DataRequired()])





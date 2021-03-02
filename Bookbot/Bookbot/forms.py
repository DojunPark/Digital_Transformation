from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    title = StringField('도서명을 입력하세요', validators=[DataRequired()])
    author = StringField('저자명을 입력하세요', validators=[DataRequired()])





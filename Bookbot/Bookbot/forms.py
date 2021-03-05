from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TitleForm(FlaskForm):
    title = StringField('도서명을 입력하세요', validators=[DataRequired()])

class AuthorForm(FlaskForm):
    author = StringField('저자명을 입력하세요', validators=[DataRequired()])

class MovieInfoForm(FlaskForm):
    title = StringField('영화명을 입력하세요', validators=[DataRequired()])

class ShoppingForm(FlaskForm):
    title = StringField('상품명을 입력하세요', validators=[DataRequired()])

class BuyForm(FlaskForm):
    address = StringField('주소', validators=[DataRequired()])








from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class BookTitleForm(FlaskForm):
    book_title = StringField('도서명을 입력하세요', validators=[DataRequired()])

class BookAuthorForm(FlaskForm):
    book_author = StringField('작가명을 입력하세요', validators=[DataRequired()])

class MovieTitleForm(FlaskForm):
    movie_title = StringField('영화명을 입력하세요', validators=[DataRequired()])

class ShoppingItemForm(FlaskForm):
    shopping_item = StringField('상품명을 입력하세요', validators=[DataRequired()])

class ShoppingPurchaseForm(FlaskForm):
    delivery_address = StringField('주소를 입력하세요', validators=[DataRequired()])







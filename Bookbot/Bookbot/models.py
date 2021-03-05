from Bookbot import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Text(), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
from flask import Blueprint, render_template, request
from Bookbot.forms import ShoppingForm, BuyForm
from Bookbot.naverapi import get_idpw, shopping
from Bookbot import db
from Bookbot.models import Order
from datetime import datetime

bp = Blueprint('shopping', __name__, url_prefix='/shopping')

@bp.route('/', methods=('POST', 'GET'))
def shopping_info():
    form = ShoppingForm()
    if request.method == 'POST' and form.validate_on_submit():
        nid, npw = get_idpw()
        json = shopping(form.title.data, nid, npw)
        return render_template('shopping_info.html', form=form, json=json)

    return render_template('shopping_info.html', form=form)

@bp.route('/buy', methods=('POST', 'GET'))
def buy_product():
    form = BuyForm()
    stitle = request.form['title']
    slprice = request.form['lprice']
    simage = request.form['image']

    if request.method == 'POST' and form.validate_on_submit():
        order = Order(title= stitle, price= slprice, address= form.address.data, create_date=datetime.now())
        db.session.add(order)
        db.session.commit()
        return render_template('    completed.html')

    return render_template('shopping_buy.html', form=form, stitle=stitle, slprice=slprice, simage=simage)
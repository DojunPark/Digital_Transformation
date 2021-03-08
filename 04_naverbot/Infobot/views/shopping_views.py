from flask import Blueprint, render_template, request
from Infobot.forms import ShoppingItemForm, ShoppingPurchaseForm
from Infobot.naver_api import n_get_idpw, n_shopping_item
from Infobot import db
from Infobot.models import Order
from datetime import datetime

bp = Blueprint('shopping', __name__, url_prefix='/shopping')

@bp.route('/item', methods=('POST', 'GET'))
def shopping_item():
    form = ShoppingItemForm()
    if request.method == 'POST' and form.validate_on_submit():
        nid, npw = n_get_idpw()
        data = n_shopping_item(form.shopping_item.data, nid, npw)
        return render_template('shopping/shopping_item.html', form=form, data=data)
    return render_template('shopping/shopping_item.html', form=form)

@bp.route('/purchase', methods=('POST', 'GET'))
def shopping_purchase():
    form = ShoppingPurchaseForm()
    image = request.form['image']
    title = request.form['title']
    lprice = request.form['lprice']

    if request.method == 'POST' and form.validate_on_submit():
        order = Order(title=title, price=lprice, address=form.delivery_address.data, create_date=datetime.now())
        db.session.add(order)
        db.session.commit()
        return render_template('/shopping/shopping_ordered.html', image=image, title=title, lprice=lprice, address=form.delivery_address.data)

    return render_template('/shopping/shopping_purchase.html', form=form, image=image, title=title, lprice=lprice)

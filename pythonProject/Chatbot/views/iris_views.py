from flask import Blueprint, render_template, request
import joblib


bp = Blueprint('iris', __name__, url_prefix='/iris')

@bp.route('/', methods=('POST', 'GET'))
def predict():
    if request.method == 'GET':
        return render_template('iris.html')
    if request.method == 'POST':
        clf = joblib.load('Chatbot/models/iris_svm.pkl')

        sepal_len = float(request.form['sepal_len'])
        sepal_wid = float(request.form['sepal_wid'])
        petal_len = float(request.form['petal_len'])
        petal_wid = float(request.form['petal_wid'])

        data = ((sepal_len, sepal_wid, petal_len, petal_wid),)
        data = clf.predict(data)[0]

        c_list = ['setosa', 'versicolor', 'virginica']
        prediction = c_list[data]

        return render_template('iris.html', prediction=prediction)
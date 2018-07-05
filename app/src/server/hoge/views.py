from flask import Blueprint, render_template

app = Blueprint(
    'hoge',
    __name__,
    url_prefix='/hoge'
)


@app.route('/index')
def index():
    return render_template('hoge/index.html')

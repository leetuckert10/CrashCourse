# First program using Flask!

from flask import Flask, render_template, url_for, redirect, request
from typing import List, Tuple
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        return request.form['password']
    return render_template('index-1.html')


if __name__ == '__main__':
    app.run(debug=True)

# First program using Flask!

from flask import Flask, render_template, url_for, redirect
from typing import List, Tuple
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

# Configure MySql
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route('/')
def index() -> str:
    cursor = mysql.connection.cursor()
#   cursor.execute("INSERT INTO users VALUES(%s)", ['Mike'])
#   mysql.connection.commit()
    result: int = cursor.execute("SELECT * FROM users")
    if result > 0:
        users: Tuple = cursor.fetchall()
        print(users)
        return users[0][0]
    return render_template('index.html')


@app.route('/about')
def about() -> str:
    return render_template('about.html')


@app.route('/css')
def css():
    return render_template('css.html')


@app.errorhandler(404)
def page_not_fount(e):
    return f"{e}: Fucking page not found you idiot!"


if __name__ == '__main__':
    app.run(debug=True)

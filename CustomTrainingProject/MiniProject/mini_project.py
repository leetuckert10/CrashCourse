# mini_project.py

from flask import Flask, render_template, request, session, flash
from flask_bootstrap import Bootstrap
from typing import List, Tuple
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import yaml
import os

app = Flask(__name__)
Bootstrap(app)

# Configure MySql
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = os.urandom(24)
mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def index() -> str:
    if request.method == "POST":
        try:
            form = request.form
            name = form["name"]
            age = form["age"]
            password = generate_password_hash(form["password"])
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO employee(name, age, password) VALUES("
                           "%s, %s, %s)", (name, age, password))
            mysql.connection.commit()
            flash("Successfully inserted data", 'success')
        except:
            flash("Failed to insert data!", 'danger')
    return render_template('index.html')


@app.route('/employees', methods=['GET'])
def employees():
    cursor = mysql.connection.cursor()
    result = cursor.execute("SELECT * FROM employee")
    if result > 0:
        employee_list = cursor.fetchall()
        session['username'] = employee_list[0]['name']
#       print(f"{check_password_hash(employee_list[0]['password'], 'letmein')}")
        return render_template('employees.html', employees=employee_list)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, session, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app=Flask(__name__)
app.secret_key="123"
mysql = MySQLConnector(app,'friends')

@app.route('/')
def index():
    friends=mysql.query_db("SELECT * FROM users")
    print friends
    return render_template('index.html', friends=friends)

@app.route('/create', methods=['POST'])
def create():
    query="INSERT INTO users (first_name,last_name,age,created_at,updated_at) VALUES (:first_name,:last_name,:age,now(),now())"
    data={
        'first_name': request.form['fullname'].split()[0],
        'last_name': request.form['fullname'].split()[1],
        'age': request.form['age']
    }

    mysql.query_db(query,data)
    return redirect('/')
app.run(debug=True)

from flask import Flask, render_template, redirect, request
from flask import url_for
#import sqlite3
import sqlitecloud
from Simple import Simplify

simple = Simplify()

"""
test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
test_cursor = test_conn.cursor()

test_cursor.execute(simple.remove_table('testing'))
test_cursor.execute(simple.create_table('testing', 'Firstname TEXT', 'Lastname TEXT', 'Email TEXT', 'Age INTEGER', 'Role TEXT', 'Activity TEXT', 'Ethnicity_Race TEXT', 'Comments TEXT'))

test_conn.commit()
test_conn.close()
"""

app = Flask(__name__)

@app.route("/")
def start():
	return redirect(url_for('home'))

@app.route("/home")
def home():
	return render_template('testing.html')

@app.route("/survey", methods = ['POST', 'GET'],)
def survey():
	if request.method == 'GET':
		return render_template('test_survey.html')
	elif request.method == 'POST':
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()

		f_name = request.form['firstname']
		l_name = request.form['lastname']
		email = request.form['email']
		age = request.form['age']
		role = request.form['role']
		recommend = request.form['recommend']
		race = request.form['race']
		comments = request.form['comment']
		
		test_cursor.execute(simple.insert('testing', f_name, l_name, email, age, role, recommend, race, comments))

		test_conn.commit()
		
		test_conn.close()
		
		return redirect(url_for('home'))

@app.route('/Power_Map')
def power_map(): 
    pass

@app.route('/login')
def login():
	pass	

if __name__ == "__main__":
	app.run(debug=True)

from flask import Flask, render_template, redirect, request
from flask import url_for
#import sqlite3
import sqlitecloud
from Simple import Simplify

simple = Simplify()

app = Flask(__name__)

#The app initializes with the end '/' so we want to redirect to '/home' for reliability
#Redirects to the Home page
@app.route("/")
def start():
	return redirect(url_for('home'))

#Displays home page
@app.route("/home")
def home():
	return render_template('testing.html')

#Survey page
@app.route("/survey", methods = ['POST', 'GET'],)
def survey():
	#Loads the survey page
	if request.method == 'GET':
		return render_template('test_survey.html')
	elif request.method == 'POST':
		#Establishes a connection object with the database
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()
		#Retrieves the information from the survey using request.form[x]
		#where x is the 'name' of the variable in the html file
		#Storing retrieved data in variables with corresponding names
		f_name = request.form['firstname']
		l_name = request.form['lastname']
		email = request.form['email']
		age = request.form['age']
		role = request.form['role']
		recommend = request.form['recommend']
		race = request.form['race']
		comments = request.form['comment']
		
		test_cursor.execute(simple.insert('testing', f_name, l_name, email, age, role, recommend, race, comments))
		#'Posts' the executed command
		test_conn.commit()
		#Closes the connection object, to ensure "safety" I think
		test_conn.close()
		#Self explanitory
		return redirect(url_for('home'))

@app.route("/survey_demo", methods = ['POST', 'GET'])
def survey_demo():
	#Loads the survey page
	if request.method == 'GET':
		return render_template('demographics.html')
	elif request.method == 'POST':
		#Establishes a connection object with the database
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()
		#Retrieves the information from the survey using request.form[x]
		#where x is the 'name' of the variable in the html file
		#Storing retrieved data in variables with corresponding names
		f_name = request.form['firstname']
		email = request.form['email']
		zipcode = request.form['zipcode']
		role = request.form['role']
		recommend = request.form['recommend']
		race = request.form['race']
		comments = request.form['comment']
		
		test_cursor.execute(simple.insert('testing', f_name, email, zipcode, role, recommend, race, comments))
		#'Posts' the executed command
		test_conn.commit()
		#Closes the connection object, to ensure "safety" I think
		test_conn.close()
		#Self explanitory
		return redirect(url_for('home'))

@app.route("/survey_general", methods = ['POST', 'GET'])
def survey_general():
	#Loads the survey page
	if request.method == 'GET':
		return render_template('general_information.html')
	elif request.method == 'POST':
		#Establishes a connection object with the database
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()
		#Retrieves the information from the survey using request.form[x]
		#where x is the 'name' of the variable in the html file
		#Storing retrieved data in variables with corresponding names
		f_name = request.form['firstname']
		l_name = request.form['lastname']
		dob = request.form['DOB']
		role = request.form['role']
		recommend = request.form['recommend']
		gender = request.form['gender']
		Pronouns = request.form['Pronouns']
		PhoneNum = request.form['Phone_Number']
		ufsa_CJL = request.form['UFSA-CJL']
		ufsa_LC = request.form['UFSA-LC']
		la_LC = request.form['LA-LC']
		Rudsdale_FV = request.form['Rudsdale-FV']
		la_GSI = request.form['LA-GSI']
		la_GS = request.form['LA-AC']
		cali_SPSP = request.form['CALI-SP(SP)']
		cali_SPSF = request.form['CALI-SP(SF)']
		cali_DSC = request.form['CALI-DSC']
		cali_PCGC = request.form['CALI-PCGC']
		
		test_cursor.execute(simple.insert('General_info', f_name, l_name, dob, role, recommend, gender, Pronouns, PhoneNum, ufsa_CJL, ufsa_LC, la_LC, Rudsdale_FV, la_GSI, la_GS, cali_SPSP, cali_SPSF, cali_DSC, cali_PCGC))
		#'Posts' the executed command
		test_conn.commit()
		#Closes the connection object, to ensure "safety" I think
		test_conn.close()
		#Self explanitory
		return redirect(url_for('home'))
	
@app.route("/self-assessment", methods = ['POST', 'GET'])
def self_assess():
	#Loads the survey page
	if request.method == 'GET':
		return render_template('self_assessments.html')
	elif request.method == 'POST':
		#Establishes a connection object with the database
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()
		#Retrieves the information from the survey using request.form[x]
		#where x is the 'name' of the variable in the html file
		#Storing retrieved data in variables with corresponding names
		f_name = request.form['firstname']
		l_name = request.form['lastname']
		email = request.form['email']
		age = request.form['age']
		role = request.form['role']
		recommend = request.form['recommend']
		race = request.form['race']
		comments = request.form['comment']
		
		test_cursor.execute(simple.insert('testing', f_name, l_name, email, age, role, recommend, race, comments))
		#'Posts' the executed command
		test_conn.commit()
		#Closes the connection object, to ensure "safety" I think
		test_conn.close()
		#Self explanitory
		return redirect(url_for('home'))
	
@app.route('/power_map', methods = ['POST', 'GET'],)
def power_map(): 
	if request.method == 'GET':
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		#test_conn = sqlite3.connect('FLC_database.db')
		test_cursor = test_conn.cursor()

		data = test_cursor.execute(simple.multiples("plottable", "AGE"))
		
		age_data=[]
		age_data_quantity=[]		
		for row in data:
			age_data.append(row[0])
			age_data_quantity.append(row[-1])

		test_conn.commit()

		test_conn.close()

		return render_template('surveyplot.html',age_data=age_data, age_data_quantity=age_data_quantity)

@app.route('/login')
def login():
	if request.method == 'GET':
		return render_template('test_login.html')
	elif request.method == 'POST':
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()

		user = request.form['email']
		password = request.form['password']
		
		#These search functions return a list of the valid query results ex:email/username and password
		data_email = test_cursor.execute(simple.searchall_or_con('login', 'EMAIL = ', user, 'EMAIL', 'PASSWORD'))
		data_user = test_cursor.execute(simple.searchall_or_con('login', 'USERNAME = ', user, 'USERNAME', 'PASSWORD'))

		email = data_email[0]
		email_pass = data_email[-1]

		user_name = data_user[0]
		user_pass = data_user[-1]

		if user_name == user or email == user:
			if user_pass == password or email_pass == password:
				#return login successful
				pass
			else:
				#return incorrect password
				pass
		else:
			#return invalid username/email
			pass

		test_conn.commit()
		
		test_conn.close()
		
		return redirect(url_for('login'))

@app.route('/register')		
def register():
	if request.method == 'GET':
		return render_template('register.html')
	elif request.method == 'POST':
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()

		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		
		data_email = test_cursor.execute(simple.searchall_or_con('login', 'EMAIL = ', email, 'EMAIL', 'USERNAME'))

		user_email = data_email[0]
		user_name = data_email[-1]

		if user_email == email:
			#return email already in use
			pass
		elif user_name == username:
			#return username already in use
			pass
		else:
			test_cursor.execute(simple.insert('login', username, email, password))

		test_conn.commit()
		
		test_conn.close()
		
		return redirect(url_for('register'))
	
if __name__ == "__main__":
	app.run(debug=True)

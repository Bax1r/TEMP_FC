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
		return render_template('community_insight.html')
	elif request.method == 'POST':
		#Establishes a connection object with the database
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()
		#Retrieves the information from the survey using request.form[x]
		#where x is the 'name' of the variable in the html file
		#Storing retrieved data in variables with corresponding names
		# 'ej' == 'environmental justice'
		community_ej = request.form['community_environmental_justice']
		seen_ej = request.form['seen_environmental_justice']
		# 'qi' == 'quality issues'
		air_qi = request.form['air_quality_issues']
		quality_of_air = request.form['quality_of_air']
		water_qi = request.form['water_quality_issues']
		improve_water_quality = request.form['improving_drinking_water']
		green_spaces = request.form['visible_green_spaces']
		invest_green = request.form['green_spaces_investments']
		use_green_spaces = request.form['utilizing_green_spaces']
		more_community_spaces = request.form['want_to_see_more_community_spaces']
		increase_school_funding = request.form['increased_funding_local_schools']
		affordable_utilities = request.form['affordable_utilities_important']
		better_infrastructure = request.form['better_infrastructures_oakland']
		better_transport = request.form['better_public_transportation']
		participation_interest = request.form['interested_in_participating']
		
		test_cursor.execute(simple.insert('testing', community_ej, seen_ej, air_qi, quality_of_air, water_qi, improve_water_quality,
									green_spaces, invest_green, use_green_spaces, more_community_spaces, increase_school_funding, affordable_utilities,
									better_infrastructure, better_transport, participation_interest))
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
		race = request.form.getlist('race')
		email = request.form['email']
		zipcode = request.form['zipcode']
		affilation = request.form['affilated']
		school = request.form['school']
		grade = request.form['grade']
		organization = request.form['community_member']
		org_name = request.form['organization_name']
		heard = request.form['heard_us']
		newsletter = request.form['sign_up']
		comment = request.form['comment']
		
		test_cursor.execute(simple.insert('testing', race, email, zipcode, affilation, school, grade, organization, org_name, heard, newsletter, comment))
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
		ufsa_CJL = request.form.get('UFSA-CJL', 'No')
		ufsa_LC = request.form.get('UFSA-LC', 'No')
		la_LC = request.form.get('LA-LC', 'No')
		Rudsdale_FV = request.form.get('Rudsdale-FV', 'No')
		la_GSI = request.form.get('LA-GSI', 'No')
		la_GS = request.form.get('LA-AC', 'No')
		cali_SPSP = request.form.get('CALI-SP(SP)', 'No')
		cali_SPSF = request.form.get('CALI-SP(SF)', 'No')
		cali_DSC = request.form.get('CALI-DSC', 'No')
		cali_PCGC = request.form.get('CALI-PCGC', 'No')
		
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
	return redirect(url_for('home'))

	if request.method == 'GET':
		test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		#test_conn = sqlite3.connect('FLC_database.db')
		test_cursor = test_conn.cursor()

		def getColumn(table, data, cursor):
			# Arguments: table (A table of the database), data (a column), cursor (new cursor for every use of this function)
			# Returns: List of possible entries, amount of each entry found
			cursor.execute(simple.multiples(table,data))
			column = cursor.fetchall()
		
			column_data=[]
			column_data_quantity=[]		
			for row in column:
				column_data.append(row[0])
				column_data_quantity.append(row[-1])

			return column_data, column_data_quantity

		##############################################################################################################
		# General info: Recommend
		##############################################################################################################
		cursor_recommend = test_conn.cursor()
		recommend_data, recommend_data_quantity = getColumn("General_info", "RECOMMEND", cursor_recommend)

		##############################################################################################################
		# General info: Roles
		##############################################################################################################
		cursor_role = test_conn.cursor()
		role_data, role_data_quantity = getColumn("General_info", "ROLE", cursor_role)

		##############################################################################################################
		# General info: Gender
		##############################################################################################################
		cursor_gender = test_conn.cursor()
		gender_data, gender_data_quantity = getColumn("General_info", "GENDER", cursor_gender)

		##############################################################################################################
		# General info: Pronouns
		##############################################################################################################
		cursor_pronouns = test_conn.cursor()
		pronouns_data, pronouns_data_quantity = getColumn("General_info", "PRONOUNS", cursor_pronouns)

		##############################################################################################################
		#General info: Programs
		##############################################################################################################
		cursor_UFSA_CJL = test_conn.cursor()
		UFSA_CJL_labels, UFSA_CJL_data_quantity = getColumn("General_info", "UFSA_CJL", cursor_UFSA_CJL)
		cursor_UFSA_LC = test_conn.cursor()
		UFSA_LC_labels, UFSA_LC_data_quantity = getColumn("General_info", "UFSA_LC", cursor_UFSA_LC)
		cursor_LA_LC = test_conn.cursor()
		LA_LC_labels, LA_LC_data_quantity = getColumn("General_info", "LA_LC", cursor_LA_LC)
		cursor_RUDSDALE_FV = test_conn.cursor()
		RUDSDALE_FV_labels, RUDSDALE_FV_data_quantity = getColumn("General_info", "RUDSDALE_FV", cursor_RUDSDALE_FV)
		cursor_LA_GSI = test_conn.cursor()
		LA_GSI_labels, LA_GSI_data_quantity = getColumn("General_info", "LA_GSI", cursor_LA_GSI)
		cursor_LA_AC = test_conn.cursor()
		LA_AC_labels, LA_AC_data_quantity = getColumn("General_info", "LA_AC", cursor_LA_AC)
		cursor_CALI_SPSP = test_conn.cursor()
		CALI_SPSP_labels, CALI_SPSP_data_quantity = getColumn("General_info", "CALI_SPSP", cursor_CALI_SPSP)
		cursor_SPSF = test_conn.cursor()
		CALI_SPSF_labels, CALI_SPSF_data_quantity = getColumn("General_info", "CALI_SPSF", cursor_SPSF)
		cursor_CALI_DSC = test_conn.cursor()
		CALI_DSC_labels, CALI_DSC_data_quantity = getColumn("General_info", "CALI_DSC", cursor_CALI_DSC)
		cursor_CALI_PCGC = test_conn.cursor()
		CALI_PCGC_labels, CALI_PCGC_data_quantity = getColumn("General_info", "CALI_PCGC", cursor_CALI_PCGC)

		# The data we want from Programs
		programs = [[], []]
		simple.yesCheck(programs, UFSA_CJL_labels, UFSA_CJL_data_quantity, "UFSA_CJL")
		simple.yesCheck(programs, UFSA_LC_labels, UFSA_LC_data_quantity, "UFSA_LC")
		simple.yesCheck(programs, LA_LC_labels, LA_LC_data_quantity, "LA_LC")
		simple.yesCheck(programs, RUDSDALE_FV_labels, RUDSDALE_FV_data_quantity, "RUDSDALE_FV")
		simple.yesCheck(programs, LA_GSI_labels, LA_GSI_data_quantity, "LA_GSI")
		simple.yesCheck(programs, LA_AC_labels, LA_AC_data_quantity, "LA_AC")
		simple.yesCheck(programs, CALI_SPSP_labels, CALI_SPSP_data_quantity, "CALI_SPSP")
		simple.yesCheck(programs, CALI_SPSF_labels, CALI_SPSF_data_quantity, "CALI_SPSF")
		simple.yesCheck(programs, CALI_DSC_labels, CALI_DSC_data_quantity, "CALI_DSC_SPSF")
		simple.yesCheck(programs, CALI_PCGC_labels, CALI_PCGC_data_quantity, "CALI_PCGC_SPSF")

		##############################################################################################################
		
		test_conn.commit()
		test_conn.close()

		return render_template(
			'surveyplot.html',

			recommend_data=recommend_data, recommend_data_quantity=recommend_data_quantity,
			role_data=role_data, role_data_quantity=role_data_quantity,
			gender_data=gender_data, gender_data_quantity=gender_data_quantity,
			pronouns_data=pronouns_data, pronouns_data_quantity=pronouns_data_quantity,
			programs_data=programs[0], programs_data_quantity=programs[1]
			)

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

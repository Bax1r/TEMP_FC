from flask import Flask, render_template, redirect, request
from flask import url_for
from datetime import date
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
	return render_template('home.html')

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
		community_ej = request.form.get('community_environmental_justice', 'No')
		seen_ej = request.form.get('seen_environmental_justice', 'No')
		# 'qi' == 'quality issues'
		air_qi = request.form.get('air_quality_issues', 'No')
		quality_of_air = request.form.get('quality_of_air', 'No')
		water_qi = request.form.get('water_quality_issues', 'No')
		improve_water_quality = request.form.get('improving_drinking_water', 'No')
		green_spaces = request.form.get('visible_green_spaces', 'No')
		invest_green = request.form.get('green_spaces_investments', 'No')
		use_green_spaces = request.form.get('utilizing_green_spaces', 'No')
		more_community_spaces = request.form.get('want_to_see_more_community_spaces', 'No')
		increase_school_funding = request.form.get('increased_funding_local_schools', 'No')
		affordable_utilities = request.form.get('affordable_utilities_important', 'No')
		better_infrastructure = request.form.get('better_infrastructures_oakland', 'No')
		better_transport = request.form.get('better_public_transportation', 'No')
		participation_interest = request.form.get('interested_in_participating', 'No')
		# Date of submission
		today = date.today()
		currentDate = today.strftime("%m/%d/%y")
		#Insert data into table
		test_cursor.execute(simple.insert('Community_Insight', community_ej, seen_ej, air_qi, quality_of_air, water_qi, improve_water_quality,
									green_spaces, invest_green, use_green_spaces, more_community_spaces, increase_school_funding, affordable_utilities,
									better_infrastructure, better_transport, participation_interest, currentDate))
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
		test_conn = sqlitecloud.connect(simple.test_connection())
		test_cursor = test_conn.cursor()
		#Retrieves the information from the survey using request.form[x]
		#where x is the 'name' of the variable in the html file
		#Storing retrieved data in variables with corresponding names
		white = request.form.get('white', 'No')
		american = request.form.get('american-native', 'No')
		asian = request.form.get('asian', 'No')
		black = request.form.get('black', 'No')
		hispanic = request.form.get('hispanic', 'No')
		latine = request.form.get('latine', 'No')
		middle_eastern = request.form.get('middle-eastern', 'No')
		pacific_islander = request.form.get('pacific-islander', 'No')
		none = request.form.get('none', 'No')
		other = request.form.get('other', 'No')
		email = request.form['email']
		zipcode = request.form['zipcode']
		affiliation_list = request.form.getlist('affiliated')
		#Convert list to str
		affiliation = ' '.join(affiliation_list)
		school = request.form['school']
		grade = request.form['grade']
		organization = request.form.get('community_member', 'no')
		org_name = request.form['organization_name']
		heard = request.form['heard_us']
		newsletter = request.form.get('sign_up', 'no')
		comment = request.form['comment']

		# Date of submission
		today = date.today()
		currentDate = today.strftime("%m/%d/%y")
		
		data_identifier = test_cursor.execute("SELECT Race_Identifier FROM Demographics ORDER BY Race_Identifier DESC LIMIT 1")

		for item in data_identifier:
			identifier = item[-1]

		identifier += 1

		test_cursor.execute(simple.insert('Demographics', email, zipcode, school, grade, organization, org_name, heard, newsletter, comment, affiliation, currentDate, identifier))
		test_cursor.execute(simple.insert('race_data', white, american, asian, black, hispanic, latine, middle_eastern, pacific_islander, none, other, currentDate, identifier))
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
		test_conn = sqlitecloud.connect(simple.test_connection())
		#test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
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
		email = request.form['Phone_Number']
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

		# Date of submission
		today = date.today()
		currentDate = today.strftime("%m/%d/%y")
		
		data_identifier = test_cursor.execute("SELECT Participation_Identifier FROM General_Information ORDER BY Participation_Identifier DESC LIMIT 1")

		for item in data_identifier:
			identifier = item[-1]

		identifier += 1

		test_cursor.execute(simple.insert('General_Information', f_name, l_name, dob, role, recommend, gender, Pronouns, email, currentDate, identifier))
		test_cursor.execute(simple.insert('participation_data', ufsa_CJL, ufsa_LC, la_LC, Rudsdale_FV, la_GSI, la_GS, cali_SPSP, cali_SPSF, cali_DSC, cali_PCGC, identifier))
		#'Posts' the executed command
		test_conn.commit()
		#Closes the connection object, to ensure "safety" I think
		test_conn.close()
		#Self explanitory
		return redirect(url_for('home'))

@app.route('/power_maps', methods = ['POST', 'GET'],)
def power_maps(): 
	return render_template("power_map_preview.html")

# Plotting for general information and participation survey
@app.route("/power_map_general", methods = ['POST', 'GET'],)
def power_map_general(): 
	if request.method == 'GET':
		#test_conn = sqlite3.connect("FLC_database.db")
		test_conn = sqlitecloud.connect(simple.test_connection())

		##############################################################################################################
		# General info: Age
		##############################################################################################################
		#cursor_age = test_conn.cursor()
		#cursor_date = test_conn.cursor()
		#age_data, age_data_quantity = getYears("General_info", cursor_age, cursor_date)

		##############################################################################################################
		# General info: Recommend
		##############################################################################################################
		cursor_recommend = test_conn.cursor()
		recommend_data, recommend_data_quantity = simple.getColumn("General_Information", "Recommend", cursor_recommend)

		##############################################################################################################
		# General info: Roles
		##############################################################################################################
		cursor_role = test_conn.cursor()
		role_data, role_data_quantity = simple.getColumn("General_Information", "Role", cursor_role)

		##############################################################################################################
		# General info: Gender
		##############################################################################################################
		cursor_gender = test_conn.cursor()
		gender_data, gender_data_quantity = simple.getColumn("General_Information", "Gender", cursor_gender)

		##############################################################################################################
		# General info: Pronouns
		##############################################################################################################
		cursor_pronouns = test_conn.cursor()
		pronouns_data, pronouns_data_quantity = simple.getColumn("General_Information", "Pronouns", cursor_pronouns)

		##############################################################################################################
		#General info: Programs
		##############################################################################################################
		# The data we want from Programs
		programs = [[], []]

		cursor_UFSA_CJL = test_conn.cursor()
		UFSA_CJL_labels, UFSA_CJL_data_quantity = simple.getColumnYes("participation_data", "UFSA_CJL", cursor_UFSA_CJL, programs)
		cursor_UFSA_LC = test_conn.cursor()
		UFSA_LC_labels, UFSA_LC_data_quantity = simple.getColumnYes("participation_data", "UFSA_LC", cursor_UFSA_LC, programs)
		cursor_LA_LC = test_conn.cursor()
		LA_LC_labels, LA_LC_data_quantity = simple.getColumnYes("participation_data", "LA_LC", cursor_LA_LC, programs)
		cursor_RUDSDALE_FV = test_conn.cursor()
		RUDSDALE_FV_labels, RUDSDALE_FV_data_quantity = simple.getColumnYes("participation_data", "RUDSDALE_FV", cursor_RUDSDALE_FV, programs)
		cursor_LA_GSI = test_conn.cursor()
		LA_GSI_labels, LA_GSI_data_quantity = simple.getColumnYes("participation_data", "LA_GSI", cursor_LA_GSI, programs)
		cursor_LA_AC = test_conn.cursor()
		LA_AC_labels, LA_AC_data_quantity = simple.getColumnYes("participation_data", "LA_AC", cursor_LA_AC, programs)
		cursor_CALI_SPSP = test_conn.cursor()
		CALI_SPSP_labels, CALI_SPSP_data_quantity = simple.getColumnYes("participation_data", "CALI_SPSP", cursor_CALI_SPSP, programs)
		cursor_SPSF = test_conn.cursor()
		CALI_SPSF_labels, CALI_SPSF_data_quantity = simple.getColumnYes("participation_data", "CALI_SPSF", cursor_SPSF, programs)
		cursor_CALI_DSC = test_conn.cursor()
		CALI_DSC_labels, CALI_DSC_data_quantity = simple.getColumnYes("participation_data", "CALI_DSC", cursor_CALI_DSC, programs)
		cursor_CALI_PCGC = test_conn.cursor()
		CALI_PCGC_labels, CALI_PCGC_data_quantity = simple.getColumnYes("participation_data", "CALI_PCGC", cursor_CALI_PCGC, programs)


		programs_data = programs[0]
		programs_data_quantity = programs[-1]

		##############################################################################################################

		plot_data = [
			recommend_data, 
			recommend_data_quantity, 
			role_data,
			role_data_quantity,
			gender_data,
			gender_data_quantity,
			pronouns_data,
			pronouns_data_quantity,
			programs_data,
			programs_data_quantity
			]
		
		test_conn.commit()
		test_conn.close()

		return render_template('surveyplotgeneral.html', plot_data=plot_data)

@app.route("/power_map_demo")
def power_map_demo():
	if request.method == 'GET':
		#test_conn = sqlite3.connect("FLC_database.db")
		test_conn = sqlitecloud.connect(simple.test_connection())

		##############################################################################################################
		#General info: Programs
		##############################################################################################################
		# The data we want from Programs
		races = [[], []]

		cursor_white = test_conn.cursor()
		white_labels, white_data_quantity = simple.getColumnYes("race_data", "White", cursor_white, races)
		cursor_native = test_conn.cursor()
		native_labels, native_data_quantity = simple.getColumnYes("race_data", "American_Native", cursor_native, races)
		cursor_asian = test_conn.cursor()
		asian_labels, asian_data_quantity = simple.getColumnYes("race_data", "Asian", cursor_asian, races)
		cursor_black = test_conn.cursor()
		black_labels, black_data_quantity = simple.getColumnYes("race_data", "Black", cursor_black, races)
		cursor_hispanic = test_conn.cursor()
		hispanic_labels, hispanic_data_quantity = simple.getColumnYes("race_data", "Hispanic", cursor_hispanic, races)
		cursor_latine = test_conn.cursor()
		latine_labels, latine_data_quantity = simple.getColumnYes("race_data", "Latine", cursor_latine, races)
		cursor_middle = test_conn.cursor()
		middle_labels, middle_data_quantity = simple.getColumnYes("race_data", "Middle_Eastern", cursor_middle, races)
		cursor_pacific = test_conn.cursor()
		pacific_labels, pacific_data_quantity = simple.getColumnYes("race_data", "Pacific_Islander", cursor_pacific, races)
		cursor_none = test_conn.cursor()
		none_labels, none_data_quantity = simple.getColumnYes("race_data", "None", cursor_none, races)



		races_data = races[0]
		races_data_quantity = races[1]

		##############################################################################################################
		
		##############################################################################################################
		# Demographics: School
		##############################################################################################################
		cursor_school = test_conn.cursor()
		school_data, school_data_quantity = simple.getColumn("demographics", "SCHOOL", cursor_school)

		##############################################################################################################
		# Demographics: Grade
		##############################################################################################################
		cursor_grade = test_conn.cursor()
		grade_data, grade_data_quantity = simple.getColumn("demographics", "GRADE", cursor_grade)

		##############################################################################################################
		# Demographics: Organization Member
		##############################################################################################################
		cursor_community = test_conn.cursor()
		community_data, community_data_quantity = simple.getColumn("demographics", "COMMUNITY_MEMBER", cursor_community)

		##############################################################################################################
		# Demographics: Organization
		##############################################################################################################
		cursor_org = test_conn.cursor()
		org_data, org_data_quantity = simple.getColumn("demographics", "ORGANIZATION_NAME", cursor_org)

		##############################################################################################################
		# Demographics: Newsletter
		##############################################################################################################
		cursor_news = test_conn.cursor()
		news_data, news_data_quantity = simple.getColumn("demographics", "NEWSLETTER_SIGN_UP", cursor_news)

		
		plot_data = [
			races_data,
			races_data_quantity,
			school_data, 
			school_data_quantity, 
			grade_data,
			grade_data_quantity,
			community_data,
			community_data_quantity,
			org_data,
			org_data_quantity,
			news_data,
			news_data_quantity
			]

		test_conn.commit()
		test_conn.close()
		
		return render_template('surveyplotdemo.html', plot_data=plot_data)

# Plotting for survey #3
@app.route("/power_map_insight")
def power_map_insight():
	return render_template('surveyplotinsight.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'GET':
		return render_template('admin_login.html')
	elif request.method == 'POST':
		test_conn = sqlitecloud.connect(simple.test_connection())
		#test_conn = sqlitecloud.connect("sqlitecloud://ccd05tfthz.g1.sqlite.cloud:8860/Testing?apikey=Mji9QZnn0DLv8by9woBTc105GxkTltAVbcixpOF71Cg")
		test_cursor = test_conn.cursor()

		user = request.form['login']
		password = request.form['password']
		
		#These search functions return a list of the valid query results ex:email/username and password
		admin_data = test_cursor.execute(simple.search_all('admin_login', f'EMAIL="{user}"'))
		#admin_data = test_cursor.execute(f'''SELECT * FROM admin_login WHERE EMAIL={user}''')

		for item in admin_data:
			data_email = item[0]
			data_pass = item[-1]

		test_conn.commit()
		
		test_conn.close()

		if data_email == user:
			if data_pass == password:
				return redirect(url_for("power_maps"))
		else:
			return redirect(url_for('login'))
	
if __name__ == "__main__":
	app.run(debug=True)

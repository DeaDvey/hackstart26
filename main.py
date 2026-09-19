from flask import Flask
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def page1():
	return render_template('form1.html')

@app.route('/page2', methods=['POST'])
def page2(email=None):
	email = request.form['email']
	domain = email.split("@")[-1]
	if domain != "soton.ac.uk" and domain != "soutampton.ac.uk" and domain != "ecs.soton.ac.uk":
		return render_template('error.html', error='Domain is not a Southampton official™ domain')
	else:
		return render_template('form2.html', email=email)

@app.route('/page3', methods=['POST'])
def page3(email1=None, email2=None):
	email1 = request.form['email1']
	email2 = request.form['email2']
	if email1 != email2:
		return render_template('error.html', error="Your emails do not match.")
	else:
		return render_template('form3.html', email=email1)

@app.route('/page4', methods=['POST'])
def page4(email_original=None, email_backwards=None):
	# These should be the same and should both be recieved in reversed format
	email_original = request.form['email_original']
	email_backwards = request.form['email_backwards']
	actual_email = email_original[::-1]
	if email_original != email_backwards:
		return render_template('error.html', error="Your reversed emails do not match.")
	else:
		return render_template('form4.html', email=actual_email)

@app.route('/page5', methods=['POST'])
def page5(email_original=None, second_email=None):
	email_original = request.form['email_original']
	second_email = request.form['second_email']
	second_domain = second_email.split("@")[-1]
	if email_original == second_email:
		return render_template('error.html', error='You should have a different personal email to your uni email!')
	elif second_domain == "gmail.com":
		return render_template('error.html', error='Don\'t use Gmail, you data subject!')
	elif second_domain == "outlook.com" or second_domain == "hotmail.com":
		return render_template('error.html', error='Don\'t use Outlook, you corporate brown-nose!')
	elif second_domain == "proton.me":
		return render_template('error.html', error='Oh so you like privacy?  We have a zero tolerance policy against child predators.')
	elif second_domain == "aol.com":
		return render_template('error.html', error='What is this? The 1990\'s?')
	else:
		return render_template('form5.html', email=email_original, second_email=second_email)

@app.route('/page6', methods=['POST'])
def page6(email1=None, email2=None):
	email1 = request.form['email1']
	email2 = request.form['email2']
	second_email = request.form['second_email']
	if email1 != email2:
		return render_template('error.html', error="Your emails do not match.")
	else:
		return render_template('form6.html', uni_email=email1, second_email=second_email)

@app.route('/page7', methods=['POST'])
def page7(email1=None, email2=None):
	univowel = request.form['univowel']
	perscons = request.form['perscons']
	uni_email = request.form['uni_email']
	second_email = request.form['second_email']
	correct_univowel = ''
	for char in uni_email:
		if char.lower() in 'aeiou':
			correct_univowel += char.lower()
	
	correct_perscons = ''
	for char in second_email:
		if char.lower() in 'bcdfghjklmnpqrstvwxyz':
			correct_perscons += char.lower()

	if univowel != correct_univowel:
		return render_template('error.html', error="You did not input the vowels from your uni email correctly.")
	if perscons != correct_perscons:
		return render_template('error.html', error="You did not input the consonants from your personal email correctly.")
	else:
		return render_template('form7.html')

@app.route('/page8', methods=['POST', 'GET'])
def page8():
	return render_template('form8.html')

@app.route('/page9', methods=['POST','GET'])
def page9():
	return render_template('form9.html')

@app.route('/page10', methods=['POST','GET'])
def page10():
	return render_template('form10.html')

@app.route('/page11', methods=['POST','GET'])
def page11():
	return render_template('form11.html')

@app.route('/quizend', methods=['POST','GET'])
def timeout():
	return render_template('session_timeout.html')

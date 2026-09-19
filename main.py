from flask import Flask
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def dynamic():
	return render_template('dynamic.html')

@app.route('/page2', methods=['POST'])
def page2(email=None):
	email = request.form['email']
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

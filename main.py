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
def page3(email=None):
	email = request.form['email']
	return render_template('form3.html', email=email)

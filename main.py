from flask import Flask
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.route('/dynamic/')
@app.route('/dynamic/<name>')
def dynamic(name=None):
	return render_template('dynamic.html', person=name)

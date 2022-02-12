from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

boostrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

@app.route('/')
def index():
	# fruits = ["apple", "grapes", "berries", "oranges"]
	# return render_template('index.html', fruits=fruits)
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)


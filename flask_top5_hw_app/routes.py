# Import the app variable from the init
from flask_top5_hw_app import app

# Import specific packages from flask
from flask import render_template

# Default Home Route - in order to use a route, u need a decorator = line 8
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/top5_content')
def testRoute():
    names = ['Drake','Rod Wave','Summer Walker','Maleek Berry']
    return render_template('top5_content.html', list_names = names)
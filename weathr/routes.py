from flask import render_template
from weathr import app

@app.route('/')
@app.route('/index')
def index():
    cities = [
        {"name": "London", "temperature": "32 degrees"},
        {"name": "Paris", "temperature": "28 degrees"},
        {"name": "Berlin", "temperature": "25 degrees"}
    ]
    # cities = {"London": "32 degrees", "Paris": "28 degrees", "Berlin": "25 degrees"}

    return render_template('main.html', cities=cities)
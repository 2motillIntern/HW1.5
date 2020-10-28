#Import the app variable from init
from homework_app import app

#Import specific packages from flask
from flask import render_template

#Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

#Favorite Five Route
@app.route('/Favorite5')
def Favorite5():
    names = ['Aretha Franklin', 'Phyllis Hyman', 'Luther Vandross', 'Snoh Alegra', 'Marvin Gaye']
    return render_template('Favorite5.html',list_name = names)
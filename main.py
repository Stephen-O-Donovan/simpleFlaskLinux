# all the imports
import os
from config import *
from forms import *
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, json

app = Flask(__name__) # create the application instance :)
app.config.from_object(Config) # load config

app.config.from_envvar('MAIN_SETTINGS', silent=True)


# For connecting to the database
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# Initialise MySQL 
mysql = MySQL(cursorclass=DictCursor)
mysql.init_app(app)

# decorators that will run this function when the web browser requests these URLs
@app.route('/')
@app.route('/index') # root and index will both go to index page
def index(): # function that will build the index HTML file


    # information retrieved from the database
    try:
        cursor = create_connection().cursor()
        cursor.execute('SELECT * FROM users')
        users_db = cursor.fetchall()
        cursor.execute('SELECT * FROM tasks')
        tasks_db = cursor.fetchall()
    finally:
        print("done")

    #Can use dictionaries to pass variables to the HTML
    user = {'username' : 'Stephen'}
    tasks = [
        {
            'name':'Create tutorial',
            'due_date':"27/06/2019"
        },
        {
            'name':'Debug website',
            'due_date':"27/06/2019"
        },
    ]
    

    #The function to load the webpage, optionally passing along variables as arguments
    return render_template('index.html', title='Home', user=user, tasks=tasks, users_db=users_db, tasks_db=tasks_db)
    
# define the login page, sets to accept both GET and POST submissions
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    remember_me_checked = ''

    # Handle the submision
    if form.validate_on_submit():
        # Validate login credentials
        if form.remember_me.data:
            remember_me_checked = "to be remembered"
        else:
            remember_me_checked = "not to be remembered"

        # Flashes a message
        flash('{} has logged in, chosen {}'.format(form.username.data, remember_me_checked))

        # Go to different page instead of loading this one
        return redirect(url_for('index'))
    return render_template('/login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():

    # Use the request function to get data from a form passed in
    user =  request.form['username']
    password = request.form['password']

    
    return json.dumps({'status':'OK','user':user,'pass':password})


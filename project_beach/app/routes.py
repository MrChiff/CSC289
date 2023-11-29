# Importing flask
import os
from flask import Flask, render_template, url_for, flash, redirect, request, session
from app.forms import Registration, Login, ChangePassword
from app.models import User
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import sqlite3
from PIL import Image
from werkzeug.exceptions import abort



# This will save the picture the user uploads with a random hex number
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    # This will resize the picture to make it 125 X 125 in size
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn




# Routes are what we create to move to other webpages.

#####################
# Home / Root Route #
#####################

# This is a default webpage route for our root or welcome page.
# The render_template returns our home.html webpage.
#
# have the greeting change after login using conditional if statement and passing
# test as a variable.
@app.route("/")
def home():
    session['set_complete'] = ""
    return render_template('home.html')


###############
# Login Route #
###############
# This is creating the route for the registratin page to link the registration form
@app.route("/login", methods = ['GET', 'POST'])
def login():
    # This will check to see if current user is logged in and redirect them back to the welcome page if Login link is clicked
    #if current_user.is_authenticated:
    #    return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        #studentid = User.query.filter_by(id=id.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #next_page = request.args.get('next')
            return render_template ('welcome.html', title = 'Welcome') 
        else:
            flash("Either username or password was typed in incorrectly. Please try agian.")
    return render_template('login.html', title = 'Login', form = form)


#################
# Welcome Route #
#################
# This is to log the user out of the current session so another user can log in. 
@app.route("/welcome")
@login_required
def welcome():
    return render_template('welcome.html', title='Welcome')
 

######################
# Registration Route #
######################
# This is creating the route for the registratin page to link the registration form
@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    form = Registration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, firstname=form.first_name.data, lastname=form.last_name.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'The account has been added successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title = 'Registration', form = form)


#########################
# Change Password Route #
#########################
# This is to allow the user to change their password.
@app.route("/change_password", methods = ['GET', 'POST'])
def change_password():
    # This will check to see if current user is logged in and redirect them back to the welcome page if Login link is clicked
    #if current_user.is_authenticated:
    #    return redirect(url_for('home'))
    form = ChangePassword()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print("pw afer hash: ", hashed_password)
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            temp_pw = hashed_password
            # reference sqlalchemy docs on ORM and https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#insert-update-delete
            user.password = hashed_password # will update DB on flush
            if user in db.session.dirty:
                print("object", user, "will be updated on commit")
            #debug end
            db.session.commit()
            flash("Your password has been successfully updated", 'success')
            return redirect(url_for('change_password'))
        else:
            flash("The Username does not exist. Please try agian.")
    return render_template('change_password.html', title = 'Change Password', form = form)












#################################################################################
###  EVERYTHING BELOW HERE WILL BE PART OF THE NAVIGATION BAR AS WELL.        ###
###  DON'T FORGET TO CHANGE THE WELCOME SCREEN AND ADD THE NAVIGATION BAR.    ###
#################################################################################




################
# Logout Route #
################
# This is to log the user out of the current session so another user can log in. 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))






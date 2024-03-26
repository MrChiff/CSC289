# Importing flask
import os
from flask import Flask, render_template, url_for, flash, redirect, request, session, send_from_directory, abort
from app.forms import Registration, Login, ChangePassword, UpdateAccount, Review, EditAccount, Manufacturers, UpdateManufacturers, GameConsole
from app.models import User, Reviews, Manufacturer, Consoles
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import sqlite3
from PIL import Image
from werkzeug.exceptions import abort


################################################
# Save user profile pic with Random hex number #
################################################
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
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        #studentid = User.query.filter_by(id=id.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
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



################
# Logout Route #
################
# This is to log the user out of the current session so another user can log in. 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


######################
# Account Info Route #
######################
# This is to access the account information page after the user is logged in
@app.route("/accountinfo", methods = ['GET', 'POST'])
@login_required
def accountinfo():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.firstname = form.first_name.data
        current_user.lastname = form.last_name.data
        db.session.commit()
        flash("Your account has been successfully updated", 'success')
    elif request.method == 'GET':
        # This will prepopulate the fields to change
        form.username.data = current_user.username
        form.first_name.data = current_user.firstname
        form.last_name.data = current_user.lastname
    image_file = url_for('static', filename = 'images/' + current_user.image_file)
    return render_template('accountinfo.html', title = 'Account Info', image_file = image_file, form = form)



###############
# About Route #
###############

@app.route("/about")
def about():
    return render_template('about.html', title = "About Video Game Library & Sales")


###############
# Admin Route #
###############

@app.route("/admin")
@login_required
def admin():
    admin = current_user.admin_user
    if admin == 'Admin':
        return render_template('admin.html', title = "Admin Area")
    else:
        flash("Sorry you must be an admin to access this page")
        return redirect(url_for('welcome'))



####################################
# Show Reviews on Admin Side Route #
####################################
@app.route("/view_admin")
@login_required
def view_admin():
    posts = Reviews.query.all()
    return render_template('view_admin.html', title = "Reviews", posts=posts)


###################################
# Show Reviews on User Side Route #
###################################
@app.route("/view_user")
def view_user():
    posts = Reviews.query.all()
    return render_template('view_user.html', title = "Reviews", posts=posts)



#############################
# Create a new Review Route #
#############################
@app.route("/review/new", methods = ['GET', 'POST'])
@login_required
def new_review():
    form = Review()
    if form.validate_on_submit():
        post = Reviews(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!!!', 'success')
        return redirect(url_for('view_admin'))
    return render_template('create_review.html', title='Submit Review', form = form, legend = 'New Review')



####################################################
# View the extended Review on Logged in side Route #
####################################################
@app.route("/review/<int:review_id>")
@login_required
def view_admin_detail(review_id):
    post = Reviews.query.get_or_404(review_id)
    return render_template('view_update.html', title=post.title, post=post)


######################################################
# View the extended Review on Unlogged in side Route #
######################################################
@app.route("/user_review/<int:review_id>")
def view_user_detail(review_id):
    post = Reviews.query.get_or_404(review_id)
    return render_template('view_update_user.html', title=post.title, post=post)



#########################
# Update a Review Route #
#########################
@app.route("/review/<int:review_id>/update", methods = ['GET', 'POST'])
@login_required
def view_update(review_id):
    post = Reviews.query.get_or_404(review_id)
    if post.author != current_user:
        abort(403)
    form = Review()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated", 'success')
        return redirect(url_for("view_admin", post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_review.html', title='Submit Review', form = form, legend='Update Review')


#########################
# Delete a Review Route #
#########################
@app.route("/review/delete/<int:review_id>")
@login_required
def delete_review(review_id):
    post = Reviews.query.get_or_404(review_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted", 'success')
    return redirect(url_for('view_admin'))

        


####################################
# Show usernames of accounts route #
####################################
# This is to access the account information page after the user is logged in
@app.route("/view_accounts")
@login_required
def view_accounts():
    accounts = User.query.all()
    return render_template('edit.html', title = 'Edit/Delete User',  accounts= accounts)



########################################################
# View the full account information for username Route #
########################################################
@app.route("/view_accounts/<int:user_id>")
@login_required
def edit_delete_user(user_id):
    form = EditAccount()
    accounts = User.query.get_or_404(user_id)
    form.username.data = accounts.username
    form.first_name.data = accounts.firstname
    form.last_name.data = accounts.lastname
    form.admin_user.data = accounts.admin_user
    return render_template('edit_account.html', title = accounts.username, form=form)
    



###############################
# Delete a User Account Route #
###############################
@app.route("/view_accounts/delete/<int:user_id>")
@login_required
def delete_account(user_id):        
    users_to_delete = User.query.get_or_404(user_id)
    if users_to_delete == current_user:
        abort(403)
    try:
        db.session.delete(users_to_delete)
        db.session.commit()
        flash("The user account has been deleted", 'success')
        return redirect(url_for('view_accounts'))
    except:
        flash("something went wrong deleting the user")
        return render_template('edit.html')



###############################
# Update a user account Route #
###############################
@app.route("/view_accounts/<int:user_id>/update", methods = ['GET', 'POST'])
@login_required
def account_update(user_id):
    users = User.query.get_or_404(user_id)
    form = EditAccount()
    if form.validate_on_submit():
        users.username = form.username.data
        users.firstname = form.first_name.data
        users.lastname = form.last_name.data
        users.admin_user = form.admin_user.data
        db.session.commit()
        flash("Your account has been successfully updated", 'success')
    elif request.method == 'GET':
        # This will prepopulate the fields to change
        form.username.data = users.username
        form.first_name.data = users.firstname
        form.last_name.data = users.lastname
        form.admin_user.data = users.admin_user
    return render_template('edit_account.html', title = 'Account Info', form = form)



################################
# View all Manufacturers Route #
################################
# This is to log the user out of the current session so another user can log in. 
@app.route("/view_manufacturer")
@login_required
def view_manufacturer():
    accounts=Manufacturer.query.all()
    return render_template('manufacturer.html', title='Manufacturer', accounts=accounts)


#############################
# Create Manufacturer Route #
#############################
# This is to log the user out of the current session so another user can log in. 
@app.route("/create_manufacturer", methods = ['GET', 'POST'])
@login_required
def create_manufacturer():
    form = Manufacturers()
    if form.validate_on_submit():
        post = Manufacturer(manufacturer=form.manufacturer.data)
        db.session.add(post)
        db.session.commit()
        flash("The manufacturer has been added successfully.")
        return redirect(url_for('view_manufacturer'))
    return render_template('create_manufacturer.html', title='Manufacturer', form=form)



###############################
# Delete a Manufacturer Route #
###############################
@app.route("/manufacturer/delete/<int:user_id>")
@login_required
def delete_manufacturer(user_id):        
    post = Manufacturer.query.get_or_404(user_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted", 'success')
    return redirect(url_for('view_manufacturer'))



#######################################
# Update a manufacturer account Route #
#######################################
@app.route("/manufacturer/<int:user_id>/update", methods = ['GET', 'POST'])
@login_required
def manufacturer_update(user_id):
    users = Manufacturer.query.get_or_404(user_id)
    form = UpdateManufacturers()
    if form.validate_on_submit():
        users.manufacturer = form.manufacturer.data
        db.session.commit()
        flash("The manufacturer has been successfully updated", 'success')
    elif request.method == 'GET':
        # This will prepopulate the fields to change
        form.manufacturer.data = users.manufacturer
    return render_template('edit_manufacturer.html', title = 'Manufacturer Info', form = form)


    
###############################
# Game Consoles Systems Route #
###############################
# This is to log the user out of the current session so another user can log in. 
@app.route("/consoles")
@login_required
def consoles():
    accounts = Consoles.query.all()
    return render_template('consoles.html', title='Game consoles', accounts = accounts)
    


#########################
# Create Consoles Route #
#########################
# This is to log the user out of the current session so another user can log in. 
@app.route("/create_consoles", methods = ['GET', 'POST'])
@login_required
def create_consoles():
    form = GameConsole()
    if form.validate_on_submit():
        post = Consoles(console=form.console.data, manufacturer = form.manufacturer.data)
        db.session.add(post)
        db.session.commit()
        flash("The console has been added successfully.")
        return redirect(url_for('consoles'))
    return render_template('create_consoles.html', title='Consoles', form=form)
















    
    










































































############################
# Video Game Systems Route #
############################
# This is to log the user out of the current session so another user can log in. 
@app.route("/video_games")
@login_required
def video_games():
    return render_template('game_systems.html', title='Game Systems')


########################
# Create Library Route #
########################
# This is to log the user out of the current session so another user can log in. 
@app.route("/create")
@login_required
def create():
    return render_template('create_library.html', title='Create Library')    


########################
# Update Library Route #
########################
# This is to log the user out of the current session so another user can log in. 
@app.route("/update")
@login_required
def update():
    return render_template('update_library.html', title='Update Library')


######################
# Sell Library Route #
######################
# This is to log the user out of the current session so another user can log in. 
@app.route("/sell")
@login_required
def sell():
    return render_template('sell_library.html', title='Sell Library')



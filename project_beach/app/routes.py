# Importing flask
import os
from flask import Flask, render_template, url_for, flash, redirect, request, session, send_from_directory, abort
from app.forms import Registration, Login, ChangePassword, UpdateAccount, Review, EditAccount, Manufacturers, \
    UpdateManufacturers, GameConsole, UpdateConsole, Game_Names, UpdateGames, console_query, manufacturer_query, \
        games_query, CreateLibrary, VideoGameSearch, UpdateLibrary
# import app.forms
from app.models import User, Reviews, Manufacturer, Consoles, Games, Library
from app import app, db, bcrypt
from app.db_query import playstation, switch, pc, nes, gameboy
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import sqlite3
from PIL import Image
from werkzeug.exceptions import abort
from search_class import RAWG_Search as RS
from search_class import NEXARDA_Search as NS




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

################
# Search Route #
################
# This is to log the user out of the current session so another user can log in. 
@app.route("/search", methods = ['GET', 'POST'])
@login_required
def search():
    user = User.query.filter_by(username=str(current_user)).first().id
    form = VideoGameSearch()
    if form.validate_on_submit():
        # Getting search results from RAWG and NEXARDA
        search_results = RS().game_search("games", form.vg_search.data)
        
        # Committing unique results to database
        temp = []
        results_names = []
        # prices = []
        output = {}
        accounts=Games.query.all()

        # converts the accounts from objects to strings
        for account in accounts:
            temp.append(str(account))

        for game in search_results:
            results_names.append(game)
            rawg_id = search_results[game][0]
            # platforms is a list
            platforms = search_results[game][1]
            price = search_results[game][2]
            # prices.append(price)
            description = search_results[game][3]
            playtime = search_results[game][4]
            # not_in_list = game not in temp
            # flash(not_in_list) 
            if game not in temp:
                for platform in platforms:
                    con = Consoles.query.filter_by(console=platform).first()
                    if con is None:
                        new_console = Consoles(console=platform, manufacturer_id = 0)
                        db.session.add(new_console)
                        db.session.commit()
                        con = Consoles.query.filter_by(console=platform).first()
                    input = Games(videogame=game, creator_id = 0, console_id = con.id)
                    db.session.add(input)
                    db.session.commit() 
            output[game] = [platforms, price, description]

        return render_template('search.html', title='Search', form=form, results_names=output, user = user)
    
    return render_template('search.html', title='Search', form=form, results_names="", user = user)
 
#######################################
# Add Search Results To Library Route #
#######################################
# This is to log the user out of the current session so another user can log in. 
@app.route("/add_search_to_library/<int:user_id>/<name>/<console>/", methods = ['GET', 'POST'])
@login_required
def add_search_to_library(user_id, name, console):
    console_id = Consoles.query.filter_by(console=console).first().id
    videogame_id = Games.query.filter_by(videogame = name, console_id = console_id).first().id
    add_to_library = Library(videogame_id=videogame_id, console_id=console_id, quantity = 1, user_id=user_id)
    db.session.add(add_to_library)
    db.session.commit()
    return redirect(url_for('welcome'))



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


#######################################
# Pulling Manufacturer Info from RAWG #
#######################################
@app.route("/manufacturer/pull", methods = ['GET', 'POST'])
@login_required
def manufacturer_pull():
    temp = []
    accounts=Manufacturer.query.all()
    for account in accounts:
        temp.append(str(account))
    mfg_list = RS().update_mfg()
    for mfg in mfg_list: 
        if mfg not in temp:
            input = Manufacturer(manufacturer=mfg)
            db.session.add(input)
            db.session.commit()

    accounts=Manufacturer.query.all()
    flash("The manufacturers have been successfully updated from RAWG.", 'success')
    return render_template('manufacturer.html', title='Manufacturer', accounts=accounts)

    
###############################
# Game Consoles Systems Route #
###############################
# This is to view all of the consoles in the database. 
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



###############################
# Delete a Consoles Route #
###############################
@app.route("/consoles/delete/<int:user_id>")
@login_required
def delete_console(user_id):        
    post = Consoles.query.get_or_404(user_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your Console has been deleted", 'success')
    return redirect(url_for('consoles'))



#########################
# Update Consoles Route #
#########################
@app.route("/console/<int:user_id>/update", methods = ['GET', 'POST'])
@login_required
def console_update(user_id):
    users = Consoles.query.get_or_404(user_id)
    form = UpdateConsole()
    if form.validate_on_submit():
        users.console = form.console.data
        users.manufacturer = form.manufacturer.data
        db.session.commit()
        flash("The manufacturer has been successfully updated", 'success')
    elif request.method == 'GET':
        # This will prepopulate the fields to change
        form.console.data = users.console
    return render_template('edit_consoles.html', title = 'Manufacturer Info', form = form)



###################################
# Pulling Consoles Info from RAWG #
###################################
@app.route("/console/pull", methods = ['GET', 'POST'])
@login_required
def console_pull():
    temp = []
    accounts = Consoles.query.all()
    # converts the accounts from objects to strings
    for account in accounts:
        temp.append(str(account))
    # Retrieves a list of all consoles from RAWG
    console_list = RS().update_console()
    # for the console in the list of consoles:
    for con in console_list:
        # if the console doesn't already exist
        if con not in temp:
            # add console to database
            input = Consoles(console=con, manufacturer_id = 0)
            db.session.add(input)
            db.session.commit()
    # retrieve update list of consoles from database
    accounts=Consoles.query.all()
    flash("The consoles have been successfully updated from RAWG.", 'success')
    return render_template('consoles.html', title='Consoles', accounts=accounts)


############################
# Video Game Systems Route #
############################
# This is to log the user out of the current session so another user can log in. 
@app.route("/video_games")
@login_required
def video_games():
    accounts = Games.query.all()
    return render_template('video_games.html', title='Video Games', accounts = accounts)



############################
# Create Video Games Route #
############################
# This is to log the user out of the current session so another user can log in. 
@app.route("/create_game", methods = ['GET', 'POST'])
@login_required
def create_game():
    form = Game_Names()
    if form.validate_on_submit():
        #post = Games(videogame=form.videogame.data, console_id=form.console.data)
        # Query database to find console_id from the name of the console
        #console_idnum = 0
        #if str(form.console.data)  == "Nintendo Entertianment System":
        #    console_idnum = 6
        # Console is a Result object
        manufacturer_name = str(form.manufacturer.data)
        manufacturer = db.session.execute(db.select(Manufacturer).filter_by(manufacturer=manufacturer_name)).scalar_one()
        manufacturer_idnum = manufacturer.id
        console_name = str(form.console.data)
        console = db.session.execute(db.select(Consoles).filter_by(console=console_name)).scalar_one()
        console_idnum = console.id
        post = Games(videogame=form.videogame.data, creator_id=manufacturer_idnum ,console_id=console_idnum )
        db.session.add(post)
        db.session.commit()
        flash("The video game has been added successfully.")
        return redirect(url_for('video_games'))
    return render_template('create_games.html', title='Create Games', form=form)


###############################
# Delete a Video GAme Route #
###############################
@app.route("/games/delete/<int:game_id>")
@login_required
def delete_game(game_id):  
    post = Games.query.get_or_404(game_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your Game has been deleted", 'success')
    return redirect(url_for('video_games'))
    
    

#########################
# Update Games Route #
#########################
@app.route("/games/<int:game_id>/update", methods = ['GET', 'POST'])
@login_required
def games_update(game_id):
    game = Games.query.get_or_404(game_id)
    form = UpdateGames()
    if form.validate_on_submit():
        game.videogame = form.videogame.data
        console_name = str(form.console.data)
        console = db.session.execute(db.select(Consoles).filter_by(console=console_name)).scalar_one()
        console_idnum = console.id
        game.console_id = console_idnum
        manufacturer_name = str(form.manufacturer.data)
        manufacturer = db.session.execute(db.select(Manufacturer).filter_by(manufacturer=manufacturer_name)).scalar_one()
        manufacturer_idnum = manufacturer.id
        game.creator_id = manufacturer_idnum
        db.session.commit()
        flash("The videogame has been successfully updated", 'success')
    elif request.method == 'GET':
        # This will prepopulate the fields to change
        form.videogame.data = game.videogame
    return render_template('edit_games.html', title = 'Game Info', form = form)


###################################
# Pulling Top Games Info from RAWG #
###################################
@app.route("/games/pull", methods = ['GET', 'POST'])
@login_required
def pull_top_games():
    temp = []
    accounts=Games.query.all()
    # converts the accounts from objects to strings
    for account in accounts:
        temp.append(str(account))
    top_games = RS().top_games()
    for game in top_games:
        rawg_id = top_games[game][0]
        # platforms is a list
        platforms = top_games[game][1]
        price = top_games[game][2]
        description = top_games[game][3]
        playtime = top_games[game][4]
        not_in_list = game not in temp
        if game not in temp:
            for platform in platforms:
                con = Consoles.query.filter_by(console=platform).first()
                if con is None:
                    new_console = Consoles(console=platform, manufacturer_id = 0)
                    db.session.add(new_console)
                    db.session.commit()
                    con = Consoles.query.filter_by(console=platform).first()
                input = Games(videogame=game, creator_id = 0, console_id = con.id, price = price)
                db.session.add(input)
                db.session.commit()

    accounts=Games.query.all()
    flash("The top games from RAWG (according to metacritic score) have been added to the video game database.", 'success')
    return render_template('video_games.html', title='Vidoe Games', accounts=accounts)


##################################
# Updating Game Prices (NEXARDA) #
##################################
@app.route("/games/price_update", methods = ['GET', 'POST'])
@login_required
def update_game_prices():
    temp = []
    accounts=Games.query.all()
    # converts the accounts from objects to strings
    for account in accounts:
        temp.append(str(account))
        print("account.videogame type:  ", type(account.videogame))

        # uses NEXARDA to determine the price
        # returns dictionary => game[video_game_name] = [price, description]
        game = NS().search('games', account.videogame)
        print("type(game):  ", type(game))
        

        # if a price is available for that specific game:
        if game and account.videogame in game:
            # print("game[account.vidoegame]:  ", game[account.videogame])
            # if account.videogame in game:
                # compare new price to old price and update if necessary
            if game[account.videogame][0] != account.price:
                account.price = game[account.videogame][0]
                db.session.commit()

    flash("The prices have been updated!.", 'success')
    return render_template('video_games.html', title='Vidoe Games', accounts=accounts)




######################
# View Library Route #
######################
# @app.route("/view_library")
# @login_required
# def view_library():
#     user = User.query.filter_by(username=str(current_user)).first().id
#     accounts = Library.query.filter_by(user_id = user)
#     for account in accounts:
#         account.game_name = Games.query.filter_by(id = account.videogame_id).first().videogame
#         account.console = Consoles.query.filter_by(id = account.console_id).first().console
#         # return render_template('library.html', title='Library', headings = '', accounts = accounts)
#     # accounts = Library.query.all()
#     # print(accounts)
#     #print(current_user)
#     return render_template('library.html', title='Library', headings='', accounts = accounts)

######################
# View Library Route #
######################
@app.route("/view_library")
@login_required
def view_library():
    output = {}
    headings = {'ID', 'Videogame', 'Console', 'Quantity', 'User'}
    user = User.query.filter_by(username=str(current_user)).first().id
    accounts = Library.query.filter_by(user_id = user)
    # print(accounts)
    for account in accounts:
        game_name = Games.query.filter_by(id = account.videogame_id).first()
        console = Consoles.query.filter_by(id = account.console_id).first().console
        output[account.id] = [game_name.videogame, console, account.quantity, game_name.price]
    return render_template('library_user.html', title='Library',headings = headings, output = output)
    


#############################
# Delete library item Route #
#############################
@app.route("/library/delete/<int:user_id>")
@login_required
def delete_library(user_id):        
    post = Library.query.get_or_404(user_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your Library item been deleted", 'success')
    return redirect(url_for('view_library'))




########################
# Create Library Route #
########################
# This is to log the user out of the current session so another user can log in. 
@app.route("/create_library", methods = ['GET', 'POST'])
@login_required
def create_library():
    form=CreateLibrary()
    if form.validate_on_submit():
        videogame_name = str(form.videogame.data)
        # videogame = db.session.execute(db.select(Games).filter_by(videogame=videogame_name)).scalar_one()
        # videogame_idnum = videogame.id
        videogame_idnum = Games.query.filter_by(videogame = videogame_name).first().id
        console_name = str(form.console.data)
        # console = db.session.execute(db.select(Consoles).filter_by(console=console_name)).scalar_one()
        # console_idnum = console.id
        console_idnum = Consoles.query.filter_by(console = console_name).first().id
        quantity = int(form.quantity.data)
        user = User.query.filter_by(username=str(current_user)).first().id
        post = Library(videogame_id = videogame_idnum, console_id = console_idnum, quantity = quantity, user_id = user)
        db.session.add(post)
        db.session.commit()
        flash("The library has been updated successfully")
        return redirect(url_for('view_library'))
    return render_template('create_library.html', title='Library', form=form)  






########################
# Update Library Route #
########################
# This is to log the user out of the current session so another user can log in. 
@app.route("/update/<int:user_id>",  methods = ['GET', 'POST'])
@login_required
def update_library(user_id):
    library = Library.query.get_or_404(user_id)
    form = UpdateLibrary()
    if form.validate_on_submit():
        videogame_name = str(form.videogame.data)
        videogame = db.session.execute(db.select(Games).filter_by(videogame=videogame_name)).scalar_one()
        videogame_idnum = videogame.id
        library.videogame_id = videogame_idnum
        console_name = str(form.console.data)
        console = db.session.execute(db.select(Consoles).filter_by(console=console_name)).scalar_one()
        console_idnum = console.id
        library.console_id = console_idnum
        quantity = int(form.quantity.data)
        library.quantity = quantity
        db.session.commit()
        flash("The Library has been successfully updated", 'success')
    elif request.method == 'GET':
        print("something went wrong")
    return render_template('update_library.html', title='Update Library', form = form)


######################
# Sell Library Route #
######################
# This is to log the user out of the current session so another user can log in. 
@app.route("/sell")
@login_required
def sell_library():
    

    return render_template('sell_library.html', title='Sell Library')



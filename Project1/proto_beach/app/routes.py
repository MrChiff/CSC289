# Importing flask
import os
from flask import Flask, render_template, url_for, flash, redirect, request, session
from app.forms import Registration, Login, UpdateAccount, Memory_Bank, ChangePassword
from app.models import User, Student_Statistics, Memory
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import sqlite3
from PIL import Image
from app import Answer_Checker
from app.Question_Class import Question
from werkzeug.exceptions import abort

def get_mem_bank_conn():
    """This function initializes the memory_bank.db database."""
    conn = sqlite3.connect('instance/mathmaticus.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_flash_cards_conn():
    """This function initializes the flash_cards.db database."""
    conn = sqlite3.connect('instance/mathmaticus.db')
    conn.row_factory = sqlite3.Row
    return conn

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

def get_eqnset(user_id):
    """This function retrieves all of the equations from the memory bank for a given user"""
    conn = get_mem_bank_conn()
    eqnset = conn.execute('SELECT * FROM memory_bank WHERE user_id = ?',(user_id,)).fetchall()
    conn.close()
    if eqnset is None:
        abort(404)
    return eqnset

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
#@app.route("/home")

 
#############################
# Account Information Route #
############################# 
    
# The render_template returns our accountinfo.html webpage.
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
        return redirect(url_for('accountinfo'))
    elif request.method == 'GET':
        #This will prepopulate the fields to change
        form.username.data = current_user.username
        form.first_name.data = current_user.firstname
        form.last_name.data = current_user.lastname
    image_file = url_for('static', filename = 'images/' + current_user.image_file)
    return render_template('accountinfo.html', title = 'Account Info', image_file = image_file, form = form)


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


###############
# About Route #
###############
# This is to log the user out of the current session so another user can log in. 
@app.route("/about")
def about():
    return render_template('about.html', title="Luna's Journey")


################
# Logout Route #
################
# This is to log the user out of the current session so another user can log in. 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


#######################
# Game Checker Route  #
#######################
# This will send the user to the Answer Checker game 
@app.route("/game/checker")
@login_required
def checker():
    return render_template('checker.html', title='Answer Checker')




#########################
# Change Password Route #
#########################
# This is to allow the user to change their password.
@app.route("/user_info/change_password", methods = ['GET', 'POST'])
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





###################
# check_ans Route #
###################
# This is the route to gather the info from the user then to determine if the equation they wrote is right or wrong.
@app.route("/game/check_ans", methods = ['GET','POST'])
@login_required
def check_ans():
    if request.method == 'POST':
        num1 = request.form['num1']
        math_op = request.form['math_op']
        num2 = request.form['num2']
        ans = request.form['ans']
        note = ""
        if not num1:
            flash('1st number is required!')
        elif not math_op:
            flash('The operator is required!')
        elif not num2:
            flash('2nd number is required!')
        elif not ans:
            flash('The answer is required!')
        elif not int(num1) and num1 != 0:
            flash('1st number is NOT an integer!')
        elif math_op != "+" and math_op != "-" and math_op != "*" and math_op != "/":
            flash('Please enter an appropriate operator!')
        elif not int(num2) and num2 != 0:
            flash('The 2nd number is NOT an integer!')
        # Mod to allow for negative ans
        elif not int(ans) and ans != 0:
            flash('The answer is NOT an integer!')
        else:
            Ans_Chk = Answer_Checker.Answer_Checker() # modle.class() init
            true_or_false = Ans_Chk.right_or_wrong_var(num1,math_op,num2,int(ans))
            if true_or_false:
                eqn = num1 + " " + math_op + " " + num2 + " = " + ans 
                note = "You guessed the correct answer."
            else:
                eqn = ""
                note = "I'm sorry that is not the correct answer for this equation."
            return render_template('checker.html', feedback = true_or_false, eqn = eqn, note = note)

    return render_template('checker.html', feedback="", eqn="", note = note)



####################
# Flash Card Route #
####################
# This will send the user to the Flash Card game 
@app.route("/game/flash_cards", methods = ['GET','POST'])
@login_required
def flash_cards():
    # print("set complete?  ", session['set_complete'])
    conn = get_flash_cards_conn()
    categories = conn.execute('SELECT DISTINCT category FROM flash_cards').fetchall()
    # temp = conn.execute('ALTER TABLE flash_cards RENAME COLUMN operator TO math_op')
    conn.close()
    
    for i in range(len(categories)):
        categories[i] = categories[i]['category']
        
    categories.insert(0, "Memory Bank Set")

    if request.method == 'POST':
        
        session['cat_name'] = request.form['flash_card_set']
        
        session['i'] = 0
        session['true_or_false'] = ""
        session['eql_sign'] = ""
        session['ans'] = ""
        return redirect(url_for('flash_card_set'))

    return render_template('flash_cards.html', categories=categories, set_complete=session['set_complete'])


########################
# Flash Card Set Route #
########################
@app.route('/flash_card_set', methods = ['GET','POST'])
@login_required
def flash_card_set():

    if session['cat_name'] == 'Memory Bank Set':
        eqn_set = get_eqnset(current_user.id)
    else:
        conn = get_flash_cards_conn()
        eqn_set = conn.execute('SELECT * FROM flash_cards WHERE category = ?',(session['cat_name'],)).fetchall()
        conn.close()
        print("blah")
    
    # print("number of eqns in set: ", len(eqn_set))
    # print('i: ', session['i'])
    if session['i'] > len(eqn_set)-1:
        session['set_complete'] = "You have completed " + session['cat_name'] + "!"
        return redirect(url_for('flash_cards'))
    else:
        eqn = eqn_set[session['i']]
        # print('eqn: ', Question(eqn).__dict__)
        # print('eqn: ', eqn)
        # print('eqn: '+ str(eqn['num1']) + str(eqn['math_op']) + str(eqn['num2']) + str(eqn['ans']))

    if session['i'] == 0:
        session['old_eqn'] = {'num1': "", 'math_op': "", 'num2': ""}
        
    if request.method == 'POST':
        session['ans'] = request.form['ans']

        ans = Answer_Checker.Answer_Checker() # modle.class() init
        session['true_or_false'] = ans.right_or_wrong_var(eqn['num1'], eqn['math_op'], eqn['num2'], int(session['ans']))

        if session['true_or_false']:
            session['eql_sign'] = "="
            session['i']+=1
        else:
            session['eql_sign'] = "&ne;"

        session['old_eqn'] = Question(eqn).__dict__
        return redirect(url_for('flash_card_set'))
        
    return render_template('flash_card_set.html', chosen_cat=session['cat_name'], eqn=eqn_set[session['i']], ans="?", T_F=session['true_or_false'], 
                           eql_sign="=", old_eqn=session['old_eqn'], old_ans=session['ans'], old_eql_sign=session['eql_sign'])



#####################
# Memory Bank Route #
#####################
# This will send the user to the Memory Bank Game 
@app.route("/memory_bank/input")
@login_required
def memory_bank():
    return render_template('mem_bank.html', title='Memory Bank')


############################
# Memory Bank answer route #
############################
# This is the route that will store the equations into the database
@app.route("/mem_bank_ans", methods = ['GET','POST'])
@login_required
def mem_bank_ans():
    studentid = current_user.id
    if request.method == 'POST':
        num1 = request.form['num1']
        math_op = request.form['math_op']
        num2 = request.form['num2']
        ans = request.form['ans']
        note = ""

        if not num1:
            flash('1st number is required!')
        elif not math_op:
            flash('The operator is required!')
        elif not num2:
            flash('2nd number is required!')
        elif not ans:
            flash('The answer is required!')
        elif not int(num1) and num1 != 0:
            flash('1st number is NOT an integer!')
        elif math_op != "+" and math_op != "-" and math_op != "*" and math_op != "/":
            flash('Please enter an appropriate operator!')
        elif not int(num2) and num2 != 0:
            flash('The 2nd number is NOT an integer!')
        # Mod to allow for negative ans
        elif not int(ans) and ans != 0:
            flash('The answer is NOT an integer!')
        else:
            # Work on adding the userid, question and answer to database here!!!!!
            Ans_Chk = Answer_Checker.Answer_Checker() # modle.class() init
            true_or_false = Ans_Chk.right_or_wrong_var(num1,math_op,num2,int(ans))
            if true_or_false:
                conn = get_mem_bank_conn()
                #ALTER
                conn.execute("INSERT INTO memory_bank (user_id, num1, math_op, num2, ans) VALUES (?, ?, ?, ?, ?)",
                             (studentid, int(num1), math_op, int(num2), int(ans)))
                conn.commit()
                conn.close()
                eqn = num1 + " " + math_op + " " + num2 + " = " + ans 
                note = "Your answer has been added to the memory bank successfully."
            else:
                eqn = ""
                note = "I'm sorry, Your answer was not added successfully."
            return render_template('mem_bank.html', feedback = true_or_false, eqn = eqn, note = note)

    return render_template('mem_bank.html', feedback="", eqn="", note = note)

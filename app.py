#Import everything needed for program
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Below is what is typed in when trying to create the database in the terminal window
#from app import app
#from app import db
# To run flask server
# python -m flask run



# Create the Flask instance
app = Flask(__name__)

# Add a database table. This will reference the table of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataman.db'

# Create a secret key to validate the form has not been tampered with
app.config['SECRET_KEY'] = "secretkey"

# Initialize the database
db = SQLAlchemy(app)
app.app_context().push()


    
    

#########
#CLASSES#
#########

# Create Model for adding users to database
class students(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Create a string
    #def __repr__(self):
    #    return'<username %r>' % self.username

# Create a Form Class
class create_account(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    first_name = StringField("Enter your first name", validators=[DataRequired()])
    last_name = StringField("Enter your last name", validators=[DataRequired()])
    password = StringField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")





# Create a route decorator
# This decorator is for the default login page
@app.route("/")
def index():
    if request.method == "GET":
        return render_template("login.html")


# This decorator is for the user main page
# The <name> will be the name of the person logged in at the moment
@app.route("/top_scores")
def top_scores():
    if request.method == "GET":
        return render_template("top_scores.html")
    

# This decorator is for the create user account page
# Want to set the variables the form asks to none since there is nothing yet provided by the user.
# Going to pull up the form from the class we created earlier.
@app.route("/add_acct", methods=['GET','POST'])
def create_acct():
    username = None
    first_name = None
    last_name = None
    password = None
    form = create_account()
    
    # Validate Form
    if form.validate_on_submit():
        # This will query the database to see if this username already exists
        user = students.query.filter_by(username=form.username.data).first()
        if user is None:
            user= students(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data    
            # This will clear the form out for the next submission
            form.username.data = ''
            form.first_name.data = ''
            form.last_name.data = ''
            form.password.data = ''
            # This will put a flash banner across the screen if the form was submitted successfully.
            flash("Account Created Successfully")
        else:
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data    
            # This will clear the form out for the next submission
            form.username.data = ''
            form.first_name.data = ''
            form.last_name.data = ''
            form.password.data = ''
            # This will put a flash banner across the screen if the form was submitted successfully.
            flash("This username already exists")
        
    # This will show the users in the database by the date added    
    #our_users = students.query.order_by(students.date_added)    
    return render_template("add_acct.html", form = form, username = username, first_name = first_name, last_name = last_name, password = password)




# This decorator is for the invalid URL pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html"), 404
    

# This decorator is for the internal server error pages
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500_error.html"), 500
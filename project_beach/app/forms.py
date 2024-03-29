from flask_wtf import FlaskForm
from flask import flash
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User, Reviews, Manufacturer, Consoles, Games
from wtforms_sqlalchemy.fields import QuerySelectField

##############
# Login Form #
##############

# This is creating the form for student registration
class Login(FlaskForm):
    # Username will be used as the label for the html.
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



#####################
# User Profile Form #
#####################

# This is creating the form for student registration
class UpdateAccount(FlaskForm):
    # Username will be used as the label for the html.
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    first_name = StringField('FirstName', validators=[DataRequired()])
    last_name = StringField('LastName', validators=[DataRequired()])
    picture = FileField("Update Profile Picture. Only JPG and PNG file extensions allowed.", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update Account')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('This username already exists. Please select another one.')

  

########################
# Change Password Form #
########################
class ChangePassword(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Change Password')



#####################
# Registration Form #
#####################

# This is creating the form for user registration
class Registration(FlaskForm):
    # Username will be used as the label for the html.
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    first_name = StringField('FirstName', validators=[DataRequired()])
    last_name = StringField('LastName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register Account')
    
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('This username already exists. Please select another one.')




################
# Reviews Form #
################
# This is creating the form for user reviews
class Review(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit Review')


#####################
# User Profile Form #
#####################

# This is creating the form for student registration
class EditAccount(FlaskForm):
    # Username will be used as the label for the html.
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    first_name = StringField('FirstName', validators=[DataRequired()])
    last_name = StringField('LastName', validators=[DataRequired()])
    picture = FileField("Update Profile Picture. Only JPG and PNG file extensions allowed.", validators=[FileAllowed(['jpg','png'])])
    admin_user = StringField('Admin/User', validators=[DataRequired()])
    submit = SubmitField('Update Account')
    
    
############################
# Create Manufacturer Form #
############################

# This is creating the form for user registration
class Manufacturers(FlaskForm):
    # Username will be used as the label for the html.
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    submit = SubmitField('Create Manufacturer')
    
    def validate_manufacturer(self, manufacturer):
        company_name = Manufacturer.query.filter_by(manufacturer = manufacturer.data).first()
        if company_name:
            flash("This manufacturer already exists. Please try again")
            raise ValidationError('This manufacturer already exists. Please select another one.')


############################
# Update Manufacturer Form #
############################

# This is creating the form for user registration
class UpdateManufacturers(FlaskForm):
    # Username will be used as the label for the html.
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    submit = SubmitField('Update Manufacturer')
    
    def validate_manufacturer(self, manufacturer):
        company_name = Manufacturer.query.filter_by(manufacturer = manufacturer.data).first()
        if company_name:
            flash("This manufacturer already exists. Please try again")
            raise ValidationError('This manufacturer already exists. Please select another one.')



################################################
# Query the Manufacturer Table for QuerySelect #
################################################
# This will query the manufacturer table to populate the QuerySelect
def manufacturer_query():
    return Manufacturer.query


#################################################
# Query the Game Consoles Table for QuerySelect #
#################################################
# This will query the manufacturer table to populate the QuerySelect
def console_query():
    return Consoles.query



############################
# Create Game Console Form #
############################

# This is creating the form for user registration
class GameConsole(FlaskForm):
    # Username will be used as the label for the html.
    console = StringField('Game Console', validators=[DataRequired()])
    manufacturer = QuerySelectField(query_factory = manufacturer_query, allow_blank=True)
    submit = SubmitField('Create Game Console')
    
    def validate_console(self, console):
        system = Consoles.query.filter_by(console = console.data).first()
        if system:
            flash("This console already exists. Please try again")
            raise ValidationError('This console already exists. Please select another one.')


############################
# Update Consoles Form #
############################

# This is creating the form for user registration
class UpdateConsole(FlaskForm):
    # Username will be used as the label for the html.
    console = StringField('Manufacturer', validators=[DataRequired()])
    manufacturer = QuerySelectField(query_factory = manufacturer_query, allow_blank=True)
    submit = SubmitField('Update Manufacturer')
    #######################################################
    # Need to figure out how to prevent a duplicate from  #
    # Being created when updating but still allow the     #
    # Console name if you need to change the manufacturer #
    #######################################################
    
    
    
##########################
# Create Video Game Form #
##########################

# This is creating the form for user registration
class Game_Names(FlaskForm):
    # Username will be used as the label for the html.
    videogame = StringField('Video Game', validators=[DataRequired()])
    console = QuerySelectField(query_factory = console_query, allow_blank=False)
    submit = SubmitField('Create Video Games')
    
    #######################################################
    # Figure out a way to say if this game already exists #
    # in both video game name and console then to say it  #
    # already exists.                                     #
    #######################################################
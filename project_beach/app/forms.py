from flask_wtf import FlaskForm
from flask import flash
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User


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
    picture = FileField("Update Profile Picture", validators=[FileAllowed(['jpg','png'])])
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

# This is creating the form for student registration
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



    
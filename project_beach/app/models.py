from app import db, login_manager
from flask_login import UserMixin
from flask import session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func


# Creating a user loader for the login manager to work
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



##############
# User model #
##############

# Here we are going to create the model for the students table in the database.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    firstname = db.Column(db.String(20), nullable = False)
    lastname = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    admin_user = db.Column(db.String(20), nullable = False, default = 'User')
    
    
    def __repr__(self):
        return f"{self.username}"



######################
# Manufacturer model #
######################

# Here we are going to create the model for the students table in the database.
class Manufacturer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    manufacturer = db.Column(db.String(20), unique = True, nullable = False)

from datetime import datetime
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
    reviews = db.relationship('Reviews', backref='author', lazy = True)

    # This is how the object will be printed
    def __repr__(self):
        return f"{self.username}"


######################
# User Reviews model #
######################
class Reviews(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    # This is how the object will be printed
    def __repr__(self):
        return f"('{self.title}', '{self.date_posted}')"
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
    user_id = db.relationship('Library', backref='user', lazy=True)
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


######################
# Manufacturer model #
######################

# Here we are going to create the model for the students table in the database.
class Manufacturer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    manufacturer = db.Column(db.String(100), unique = True, nullable = False)
    # Manufacturer can have many consoles
    # The backref is basically creating a virtual column I'm naming systems and it references the foreign key name before the dot.
    console_id = db.relationship('Consoles', backref='manufacturer', lazy=True)
    # This is how the object will be printed
    def __repr__(self):
        return f"{self.manufacturer}"
    

#######################
# Game Consoles model #
#######################
class Consoles(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    console = db.Column(db.String(100), nullable = False)
    # Each Console can have only one manufacturer
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable = False)
    # manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    # This is the back reference for the one to many
    system_id = db.relationship('Games', backref='consoles', lazy=True)
    library_id = db.relationship('Library', backref='consoles', lazy=True)
    # This is how the object will be printed
    def __repr__(self):
        return f"{self.console}"


#####################
# Video Games model #
#####################
class Games(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    videogame = db.Column(db.String(100), nullable = False)
    creator_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable = True)
    # Each Console can have more than one game
    console_id = db.Column(db.Integer, db.ForeignKey('consoles.id'), nullable = False)
    videogame_id = db.relationship('Library', backref='games', lazy=True)
    price = db.Column(db.Float, nullable = True)
    # This is how the object will be printed
    def __repr__(self):
        return f"{self.videogame}"



#####################
# Library model #
#####################
class Library(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    videogame_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable = False)
    # This is console id
    console_id = db.Column(db.Integer, db.ForeignKey('consoles.id'), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) 
    # This is how the object will be printed
    def __repr__(self):
        return f"{self.videogame_id, self.console_id, self.quantity, self.user_id}"
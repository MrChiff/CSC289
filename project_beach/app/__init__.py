# Importing flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import webview



# Setting this to an instance of a flask class (__name__) means just the name of the module
app = Flask(__name__)
window = webview.create_window('mathmaticus', app)

# setting the secret key to prevent cross site scripting.
# This will be hidden before site goes live.
app.config['SECRET_KEY'] = 'secretkey'

# This creates the database instance
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mathmaticus.db"
db = SQLAlchemy(app)

# Setting up the hashing for passwords
bcrypt = Bcrypt(app)

# Setting up the login manager to use in the program.
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



# must put this import here or else you will get a circular import
from app import routes
# Importing flask
import os
from flask import Flask, render_template, url_for, flash, redirect, request, session, send_from_directory, abort
from app.forms import Registration, Login, ChangePassword, UpdateAccount, Review, EditAccount, Manufacturers, UpdateManufacturers, GameConsole, UpdateConsole, Game_Names, UpdateGames, console_query, manufacturer_query
from app.models import User, Reviews, Manufacturer, Consoles, Games
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import sqlite3
from PIL import Image
from werkzeug.exceptions import abort


##################################
# Playstation One Database Query #
##################################
#def playstation_one():
#    game_name = Consoles.query.filter_by(console='Playstation One').first()
#    game_id = game_name.id
#    console_names = Games.query.filter_by(console_id = game_id).all()
#    for console_name in console_names:
#        print(console_name)
#        return console_name
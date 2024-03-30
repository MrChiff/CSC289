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


#####################################
# Display all Playstation One Games #
#####################################

@app.route("/playstation_one")
def playstation_one():
    game_name = Consoles.query.filter_by(console='Playstation One').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Playstation Games', console_names = console_names)


#####################################
# Display all Nintendo Switch Games #
#####################################

@app.route("/switch")
def switch():
    game_name = Consoles.query.filter_by(console='Switch').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Switch Games', console_names = console_names)


###################################################
# Display all Nintendo Entertainment System Games #
###################################################

@app.route("/nes")
def nes():
    game_name = Consoles.query.filter_by(console='NES').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'NES Games', console_names = console_names)


#####################################
# Display all Xbox One System Games #
#####################################

@app.route("/xbox_one")
def xbox_one():
    game_name = Consoles.query.filter_by(console='X Box One').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'X Box One Games', console_names = console_names)

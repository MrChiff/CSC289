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


##########################################
# Display Description and Price for Game #
##########################################

@app.route("/price_descript")
def price_descript():
    return render_template('price_descript.html', title = "Price/Description")


#########################################
#########################################
## NINTENDO GAME LOOKUP BY CONSOLENAME ##
#########################################
#########################################


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
# Display all Nintendo Switch Games #
#####################################

@app.route("/switch")
def switch():
    game_name = Consoles.query.filter_by(console='Switch').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Switch Games', console_names = console_names)






###################################
###################################
## Display all Sony System Games ##
###################################
###################################


#################################
# Display all Playstation Games #
#################################

@app.route("/playstation")
def playstation():
    game_name = Consoles.query.filter_by(console='Playstation').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Playstation Games', console_names = console_names)


###################################
# Display all Playstation 4 Games #
###################################

@app.route("/playstation_4")
def playstation_4():
    game_name = Consoles.query.filter_by(console='Playstation 4').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Playstation 4 Games', console_names = console_names)


###################################
# Display all Playstation 5 Games #
###################################

@app.route("/playstation_5")
def playstation_5():
    game_name = Consoles.query.filter_by(console='Playstation 5').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Playstation 5 Games', console_names = console_names)






########################################
########################################
## Display all Microsoft System Games ##
########################################
########################################


##########################################
# Display all Xbox Seriex X System Games #
##########################################

@app.route("/xbox_x")
def xbox_x():
    game_name = Consoles.query.filter_by(console='Xbox Series X').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Xbox Series X Games', console_names = console_names)



####################################
####################################
## Display all Atari System Games ##
####################################
####################################


###########################
# Display all Atari Games #
###########################

@app.route("/atari")
def atari():
    game_name = Consoles.query.filter_by(console='atari').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Atari Games', console_names = console_names)
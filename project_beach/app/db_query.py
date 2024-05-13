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


def games_for_console(console_name):
    console_id = Consoles.query.filter_by(console=console_name).first().id
    # game_id = game_name.id
    games = Games.query.filter_by(console_id = console_id).all()

    return games

##########################################
# Display Description and Price for Game #
##########################################

@app.route("/price_descript")
def price_descript():
    return render_template('price_descript.html', title = "Price/Description")


@app.route("/pc")
def pc():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console("pc")
    return render_template('videogame_view.html', title = 'PC Games', games = games, console = "PC", user = user)


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
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console("NES")
    return render_template('videogame_view.html', title = 'NES Games', games = games, console = "NES", user = user)



#####################################
# Display all Nintendo Switch Games #
#####################################

@app.route("/switch")
def switch():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Nintendo Switch')
    return render_template('videogame_view.html', title = 'Nintendo Switch Games', games = games, console = 'Nintendo Switch', user = user)

#####################################
# Display all Nintendo Game Boy Games #
#####################################

@app.route("/gameboy")
def gameboy():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Game Boy')
    return render_template('videogame_view.html', title = 'Game Boy', games = games, console = 'Game Boy', user = user)



#####################################
# Display all Nintendo Game Boy Advanced Games #
#####################################

@app.route("/gameboy_adv")
def gameboy_adv():
    game_name = Consoles.query.filter_by(console='Game Boy Advanced').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Game Boy Advanced Games', console_names = console_names)


#####################################
# Display all Nintendo Game Boy Advanced Games #
#####################################

@app.route("/gameboy_color")
def gameboy_color():
    game_name = Consoles.query.filter_by(console='Game Boy Color').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Game Boy Color Games', console_names = console_names)

@app.route("/gamecube")
def gamecube():
    game_name = Consoles.query.filter_by(console='GameCube').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()

    return render_template('videogame_view.html', title = 'GameCube Games', console_names = console_names)


@app.route("/nintendo3ds")
def nintendo3ds():
    game_name = Consoles.query.filter_by(console='Nintendo 3DS').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Nintendo 3DS Games', console_names = console_names)

@app.route("/nintendo64")
def nintendo64():
    game_name = Consoles.query.filter_by(console='Nintendo 64').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Nintendo 64 Games', console_names = console_names)

@app.route("/nintendods")
def nintendods():
    game_name = Consoles.query.filter_by(console='Nintendo DS').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Nintendo DS Games', console_names = console_names)

@app.route("/nintendodsi")
def nintendodsi():
    game_name = Consoles.query.filter_by(console='Nintendo DSi').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Nintendo DSi Games', console_names = console_names)

@app.route("/snes")
def snes():
    game_name = Consoles.query.filter_by(console='SNES').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'SNES Games', console_names = console_names)

@app.route("/wii")
def wii():
    game_name = Consoles.query.filter_by(console='Wii').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Wii Games', console_names = console_names)

@app.route("/wiiu")
def wiiu():
    game_name = Consoles.query.filter_by(console='Wii U').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Wii U Games', console_names = console_names)




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
# Display all Playstation 2 Games #
###################################

@app.route("/playstation2")
def playstation2():
    game_name = Consoles.query.filter_by(console='Playstation 2').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Playstation 2 Games', console_names = console_names)


#################################
# Display all Playstation 3 Games #
#################################

@app.route("/playstation3")
def playstation3():
    game_name = Consoles.query.filter_by(console='Playstation 3').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Playstation 3 Games', console_names = console_names)



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


@app.route("/psvita")
def psvita():
    game_name = Consoles.query.filter_by(console='PS Vita').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'PS Vita Games', console_names = console_names)

@app.route("/psp")
def psp():
    game_name = Consoles.query.filter_by(console='PSP').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'PSP Games', console_names = console_names)




########################################
########################################
## Display all Microsoft System Games ##
########################################
########################################

@app.route("/xbox")
def xbox():
    game_name = Consoles.query.filter_by(console='Xbox').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Xbox Games', console_names = console_names)

@app.route("/xbox360")
def xbox360():
    game_name = Consoles.query.filter_by(console='Xbox 360').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Xbox 360 Games', console_names = console_names)

@app.route("/xbox1")
def xbox1():
    game_name = Consoles.query.filter_by(console='Xbox One').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Xbox One Games', console_names = console_names)


##########################################
# Display all Xbox Seriex X/S System Games #
##########################################

@app.route("/xbox_sx")
def xbox_sx():
    game_name = Consoles.query.filter_by(console='Xbox Series S/X').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Xbox Series S/X Games', console_names = console_names)



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
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console("atari")
    return render_template('videogame_view.html', title = 'Atari Games', games = games, console = "atari", user = user)




####################################
####################################
## Display all SEGA System Games ##
####################################
####################################

@app.route("/dreamcast")
def dreamcast():
    game_name = Consoles.query.filter_by(console='Dreamcast').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Dreamcast Games', console_names = console_names)

@app.route("/gamegear")
def gamegear():
    game_name = Consoles.query.filter_by(console='Game Gear').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Game Gear Games', console_names = console_names)

@app.route("/genesis")
def genesis():
    game_name = Consoles.query.filter_by(console='Genesis').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'Genesis Games', console_names = console_names)


@app.route("/sega_cd")
def sega_cd():
    game_name = Consoles.query.filter_by(console='SEGA CD').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'SEGA CD Games', console_names = console_names)

@app.route("/sega_saturn")
def sega_saturn():
    game_name = Consoles.query.filter_by(console='SEGA Saturn').first()
    game_id = game_name.id
    console_names = Games.query.filter_by(console_id = game_id).all()
    return render_template('videogame_view.html', title = 'SEGA Saturn Games', console_names = console_names)
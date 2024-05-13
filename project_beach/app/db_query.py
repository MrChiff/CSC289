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
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Game Boy Advanced')
    return render_template('videogame_view.html', title = 'Game Boy Advanced', games = games, console = 'Game Boy Advanced', user = user)


#####################################
# Display all Nintendo Game Boy Advanced Games #
#####################################

@app.route("/gameboy_color")
def gameboy_color():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Game Boy Color')
    return render_template('videogame_view.html', title = 'Game Boy Color', games = games, console = 'Game Boy Color', user = user)

@app.route("/gamecube")
def gamecube():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('GameCube')
    return render_template('videogame_view.html', title = 'GameCube', games = games, console = 'GameCube', user = user)


@app.route("/nintendo3ds")
def nintendo3ds():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Nintendo 3DS')
    return render_template('videogame_view.html', title = 'Nintendo 3DS', games = games, console = 'Nintendo 3DS', user = user)

@app.route("/nintendo64")
def nintendo64():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Nintendo 64')
    return render_template('videogame_view.html', title = 'Nintendo 64', games = games, console = 'Nintendo 64', user = user)

@app.route("/nintendods")
def nintendods():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Nintendo DS')
    return render_template('videogame_view.html', title = 'Nintendo DS', games = games, console = 'Nintendo DS', user = user)

@app.route("/nintendodsi")
def nintendodsi():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Nintendo DSi')
    return render_template('videogame_view.html', title = 'Nintendo DSi', games = games, console = 'Nintendo DSi', user = user)

@app.route("/snes")
def snes():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('SNES')
    return render_template('videogame_view.html', title = 'SNES', games = games, console = 'SNES', user = user)

@app.route("/wii")
def wii():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Wii')
    return render_template('videogame_view.html', title = 'Wii', games = games, console = 'Wii', user = user)

@app.route("/wiiu")
def wiiu():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Wii U')
    return render_template('videogame_view.html', title = 'Wii U', games = games, console = 'Wii U', user = user)




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
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Playstation')
    return render_template('videogame_view.html', title = 'Playstation', games = games, console = 'Playstation', user = user)


###################################
# Display all Playstation 2 Games #
###################################

@app.route("/playstation2")
def playstation2():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Playstation 2')
    return render_template('videogame_view.html', title = 'Playstation 2', games = games, console = 'Playstation 2', user = user)


#################################
# Display all Playstation 3 Games #
#################################

@app.route("/playstation3")
def playstation3():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Playstation 3')
    return render_template('videogame_view.html', title = 'Playstation 3', games = games, console = 'Playstation 3', user = user)



###################################
# Display all Playstation 4 Games #
###################################

@app.route("/playstation_4")
def playstation_4():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Playstation 4')
    return render_template('videogame_view.html', title = 'Playstation 4', games = games, console = 'Playstation 4', user = user)


###################################
# Display all Playstation 5 Games #
###################################

@app.route("/playstation_5")
def playstation_5():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Playstation 5')
    return render_template('videogame_view.html', title = 'Playstation 5', games = games, console = 'Playstation 5', user = user)


@app.route("/psvita")
def psvita():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('PS Vita')
    return render_template('videogame_view.html', title = 'PS Vita', games = games, console = 'PS Vita', user = user)

@app.route("/psp")
def psp():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('PSP')
    return render_template('videogame_view.html', title = 'PSP', games = games, console = 'PSP', user = user)



########################################
########################################
## Display all Microsoft System Games ##
########################################
########################################

@app.route("/xbox")
def xbox():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Xbox')
    return render_template('videogame_view.html', title = 'Xbox', games = games, console = 'Xbox', user = user)

@app.route("/xbox360")
def xbox360():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Xbox 360')
    return render_template('videogame_view.html', title = 'Xbox 360', games = games, console = 'Xbox 360', user = user)

@app.route("/xbox1")
def xbox1():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Xbox One')
    return render_template('videogame_view.html', title = 'Xbox One', games = games, console = 'Xbox One', user = user)


##########################################
# Display all Xbox Seriex X/S System Games #
##########################################

@app.route("/xbox_sx")
def xbox_sx():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Xbox Series S/X')
    return render_template('videogame_view.html', title = 'Xbox Series S/X', games = games, console = 'Xbox Series S/X', user = user)



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
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Dreamcast')
    return render_template('videogame_view.html', title = 'Dreamcast', games = games, console = 'Dreamcast', user = user)

@app.route("/gamegear")
def gamegear():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Game Gear')
    return render_template('videogame_view.html', title = 'Game Gear', games = games, console = 'Game Gear', user = user)

@app.route("/genesis")
def genesis():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('Genesis')
    return render_template('videogame_view.html', title = 'Genesis', games = games, console = 'Genesis', user = user)

@app.route("/sega_cd")
def sega_cd():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('SEGA CD')
    return render_template('videogame_view.html', title = 'SEGA CD', games = games, console = 'SEGA CD', user = user)

@app.route("/sega_saturn")
def sega_saturn():
    user = User.query.filter_by(username=str(current_user)).first().id
    games = games_for_console('SEGA Saturn')
    return render_template('videogame_view.html', title = 'SEGA Saturn', games = games, console = 'SEGA Saturn', user = user)
# price fetcher for CSC289 VGLS
# to run:  python -m uvicorn filename(no .py):app --reload
#       for this file:  python -m uvicorn price_fetcher:app --reload

import requests
# from bs4 import BeautifulSoup as BS
# from fastapi import FastAPI



# testing searching ebay for mario 64 (N64)
# item = "mario 64"
# # url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=mario+64&_sacat=0"

# print("Testing Fast API with ebay for Mario 64 (N64)")
# # print("url:  ", url)

# app = FastAPI()
# @app.get("/")
# def root():
#     # returns a dictionary
#     return {"Price Fetcher":"Mario 64"}



# # This is what Mr. Norris sent me.
# # using https://api.rawg.io/api/games
# import requests

# # personal API Key for RAWG Video Games Database through Rapid API
# api_key = "08786c523fmsh0e3de68b92b2181p17ea20jsnf7fde4490fa3"

# # Define the API endpoint and parameters
# base_url = "https://api.rawg.io/api/games"
# # game_name = "Call of Duty: Modern Warfare"
# game_name = "Mario"

# # Set up the query parameters
# params = {
#     "search": game_name,
#     "key": api_key
# }

# # Make the API request
# response = requests.get(base_url, params=params)

# # Parse the response JSON
# data = response.json()
# print(data)

# # Extract the first game result (assuming it's the correct game)
# if "results" in data and len(data["results"]) > 0:
#     game = data["results"][0]
#     game_name = game["name"]
#     game_price = game.get("price", "N/A")
#     print(f"The average price of {game_name} is {game_price}")
# else:
#     print(f"No results found for {game_name}")


# # From Rapid API (RAWG Video Game Database)
# url = "https://rawg-video-games-database.p.rapidapi.com/games"

# headers = {
# 	# "X-RapidAPI-Key": "08786c523fmsh0e3de68b92b2181p17ea20jsnf7fde4490fa3",
#     "key": api_key,
# 	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())


# RAWG.io API
# jsonify, loads, dumps
# restapi parse json; curl


# API page example (not useful/too much info)
# GET https://api.rawg.io/api/platforms?key=YOUR_API_KEY
# GET https://api.rawg.io/api/games?key=YOUR_API_KEY&dates=2019-09-01,2019-09-30&platforms=18,1,7

print("RAWG API Requests")
rawg_api_key = "?key=8583455b78234c0b940762d0141319c4"
base_url = "https://api.rawg.io/api/"
games_search = "games/search"
game_name="Mario 64"

# response =  requests.get(base_url + "games")

response = requests.get(base_url + games_search + game_name + rawg_api_key)
print(response.json())
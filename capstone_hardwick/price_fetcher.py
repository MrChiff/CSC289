# price fetcher for CSC289 VGLS
# criterion crawler
# data detective
# super searcher
# 
# to run:  python -m uvicorn filename(no .py):app --reload
#       
# https://rawgthedocs.orels.sh/api/#api-clients

import requests
import json


# testing searching ebay for mario 64 (N64)

# API page example (not useful/too much info)
# GET https://api.rawg.io/api/platforms?key=YOUR_API_KEY
# GET https://api.rawg.io/api/games?key=YOUR_API_KEY&dates=2019-09-01,2019-09-30&platforms=18,1,7

print("RAWG API Requests")
rawg_api_key = "key=8583455b78234c0b940762d0141319c4"
base_url = "https://api.rawg.io/api/"
games = "games?"
search = "&search="
game_name="Super Mario 64"
searchable_name = "+".join(game_name.split())

url_name = base_url + games + rawg_api_key + search + game_name
print(url_name)

# response =  requests.get(base_url + "games")

# response = requests.get(base_url + games_search + game_name + rawg_api_key)
response = requests.get(url_name)
response_json = response.json()
# print("response_json:  ", response_json)
# print(response.json())
# print("\n")
print("response_json type:  ", type(response_json))
print("Name:  ", response_json["results"][0]["name"])
print("Duration:  ", response_json["results"][0]["playtime"])
print("Console:  ", response_json["results"][0]["platforms"][0]["platform"]["name"])
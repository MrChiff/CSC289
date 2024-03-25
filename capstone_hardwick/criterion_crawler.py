# criterion crawler for CSC289 VGLS
# 
# Convert this into a class that will save all of the details to the database.
# Need to create decision structure for the cases:
#   - just a game
#   - just a console
#   - just an accessory
#   - a combination of all of these
# Do I look up a multiplatform game for each console individually or look them all up at once 
# and save all types to the database?
#
# Need a file that extracts the items from the database for this class to look up and save 
# to the database. (will be used at start to populate the database with the details)
#
# Will I need a separate class for each of the categories (games, consoles, accessories).
# 
# Need to figure out how to use a class without all passing all the values to the class 
# (default values?)
#
# look into rawgpy
#
# to run uvicorn:  python -m uvicorn filename(no .py):app --reload
# output reqs:  pip freeze > reqs.txt
#      or       python -m pipreqs.pipreqs ./ --encoding=utf-8
# (./ is for current directory)
#
# Add these tasks to kanban
#      
# https://rawgthedocs.orels.sh/api/#api-clients
#
# use firefox to display json
# pretty print => json.dumps(json_data, indent=4) => rawg
# determine what columns want for games
# use cases for rawg.io
# asyncio lib function
# look into rawg on github: pip install rawg
# explain where data comes from (final pres)
# look at forms.py and routes.py (post=Console(....)), Console=name of db
#   forms.py => Create Manufacturer Form, Update Manufacturer Form
#   routes.py => View all Manufacturers Route, Create Manufacturer Route, 
#                Delete a Manufacturer Route, Update a manufacturer account Route

import requests
import json
import re
import sys


# API page example (not useful/too much info)
# GET https://api.rawg.io/api/platforms?key=YOUR_API_KEY
# GET https://api.rawg.io/api/games?key=YOUR_API_KEY&dates=2019-09-01,2019-09-30&platforms=18,1,7

print("#####################\n" + \
      "# RAWG API Requests #\n" + \
      "#####################\n")
rawg_api_key = "key=8583455b78234c0b940762d0141319c4"
base_url = "https://api.rawg.io/api/"
games = "games?"
search = "&search="
game_name="Super Mario 64"
searchable_name = "+".join(game_name.split())

url_name = base_url + games + rawg_api_key + search + searchable_name
print(url_name)

# response =  requests.get(base_url + "games")

# response = requests.get(base_url + games_search + game_name + rawg_api_key)
response = requests.get(url_name)
response_json = response.json()
print(response_json)
print("Name:  ", response_json["results"][0]["name"])
print("Duration:  ", response_json["results"][0]["playtime"])
print("Console:  ", response_json["results"][0]["platforms"][0]["platform"]["name"])


# print("PriceMatching.com Work Around")
# # a $49/mo subscription is required to use the Price Matching API. However, they do have a csv file with the data
# # which I am going to try and download to use for our purposes.  The CSV file is updated daily.
# # To Do:  Figure out how to download an updated CSV either everyday or every time the program is started.
# csv_url = "https://www.pricecharting.com/api-documentation#download"

# Other possible APIs
# CheapShark API => digital pc games only.  (apidocs.cheapshark.com)
# IGDB => may be better than RAWG but uses Oauth2 through twitch for validation (api-docs.igdb.com)
#      => searchable fields: age rating
# look at models


# NEXARDA => github.com/NEXARDA/NEXARDA
print("\n\n\n")

print("###########\n" + \
      "# NEXARDA #\n" + \
      "###########\n")

status_url = "https://www.nexarda.com/api/v3/status"
search_url = "https://www.nexarda.com/api/v3/search?type="
query = "q="

searchable_name = "Crysis+2"

website_status = requests.get(status_url)
website_json = json.loads(website_status.content.decode('utf-8'))
print(website_json["online"])
if website_json["online"] == True:
    print("Nexarda is online")
else:
    print("Nexarda is unreachable. Exiting Program.")
    sys.exit()

search = requests.get(search_url + "games" + "&" + query + searchable_name)
search_json = json.loads(search.content.decode('utf-8'))
names = []
low_price = []
year = []
game_dict = {}
print("\nGame:  ", searchable_name)
print("Search URL:  ", search.url)
# print("Search:  ", search.content)
print("Success?  ", search_json["success"])
print("Reason:  ", search_json["message"])

results_total = search_json["results"]["total"]
print("# of Results:  ", results_total)

for i in range(results_total):
    names.append(search_json["results"]["items"][i]["title"][:-7])
    year.append(search_json["results"]["items"][i]["title"][-5:-1])
    low_price.append((re.findall(r"[$,\d]+[.,\d]+[.,\d]+[.,\d]", search_json["results"]["items"][i]["text"]))[0])
    game_dict[names[i]] = [year[i], low_price[i]]
    print("\nitem:  ", i)
    print("Result " + str(i+1) + ":  " + names[i])
    print("Price:  ", search_json["results"]["items"][i]["text"])
    print("Lowest Price:  ", low_price[i])
print(game_dict)




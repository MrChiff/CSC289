# price fetcher for CSC289 VGLS
# to run:  python -m uvicorn filename(no .py):app --reload
#       for this file:  python -m uvicorn price_fetcher:app --reload

# import requests
from bs4 import BeautifulSoup as BS
from fastapi import FastAPI



# testing searching ebay for mario 64 (N64)
item = "mario 64"
# url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=mario+64&_sacat=0"

print("Testing Fast API with ebay for Mario 64 (N64)")
# print("url:  ", url)

app = FastAPI()
@app.get("/")
def root():
    # returns a dictionary
    return {"Price Fetcher":"Mario 64"}

# This is what Mr. Norris sent me.
# using https://api.rawg.io/api/games
import requests

# Define the API endpoint and parameters
base_url = "https://api.rawg.io/api/games"
game_name = "Call of Duty: Modern Warfare"

 

# Set up the query parameters
params = {
    "search": game_name,
    "key": "YOUR_API_KEY"  # Replace with your actual API key
}

# Make the API request
response = requests.get(base_url, params=params)

# Parse the response JSON
data = response.json()

# Extract the first game result (assuming it's the correct game)
if "results" in data and len(data["results"]) > 0:
    game = data["results"][0]
    game_name = game["name"]
    game_price = game.get("price", "N/A")
    print(f"The average price of {game_name} is {game_price}")
else:
    print(f"No results found for {game_name}")
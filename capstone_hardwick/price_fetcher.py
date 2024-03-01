# price fetcher for CSC289 VGLS
# to run:  python -m uvicorn filename(no .py):app --reload
#       for this file:  python -m uvicorn price_fetcher:app --reload

import requests
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
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


import search_class

# API page example (not useful/too much info)
# GET https://api.rawg.io/api/platforms?key=YOUR_API_KEY
# GET https://api.rawg.io/api/games?key=YOUR_API_KEY&dates=2019-09-01,2019-09-30&platforms=18,1,7
def main():
    print("#####################\n" + \
        "# RAWG API Requests #\n" + \
        "#####################\n")
   
    game_name="call of duty"
    category = "games" 
    # rawg_search_results(game_name) 
    results_dict = search_class.RAWG_Search().game_search(category, game_name)


    print("\n####################\n" + \
          "# Top Games (RAWG) #\n" + \
          "####################\n")
    search_class.RAWG_Search().top_games()

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
    # print("\n\n\n")

    print("\n###########\n" + \
          "# NEXARDA #\n" + \
          "###########\n")

    
    game_dict = search_class.NEXARDA_Search().search(category, game_name)
    # print(game_dict)



# Call the main function.
if __name__ == "__main__":    
    main()

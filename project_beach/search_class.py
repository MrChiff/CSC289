import requests
import json
# import re
import sys
import math

DEBUG = False
#==================#
class RAWG_Search():
#==================#    
    '''
    This class uses the RAWG API to search for platforms and video games
    '''

    def __init__(self):
        self.api_key = "key=8583455b78234c0b940762d0141319c4"
        self.base_url = "https://api.rawg.io/api/"
        self.results_total = 20

    #====================================#
    def game_search(self, category, name):
    #====================================#

        self.category = category + "?"
        self.searchable_name = "+".join(name.split())
        self.search_results_dict = {}

        self.search_url = self.base_url + self.category + self.api_key + "&search=" + self.searchable_name
        if DEBUG:
            print(self.search_url)

        response = requests.get(self.search_url)
        response_json = response.json()

        if DEBUG:
            print(f'{"item":<5}{"ID":<8}{"Name":<54}{"Platform":<72}{"lowest price":<5}')

        for i in range(self.results_total):
            name = response_json["results"][i]["name"]
            playtime = response_json["results"][i]["playtime"]
            rawg_id = response_json["results"][i]["id"]
            if playtime == 0:
                playtime = "unknown"
            platform = []
            for p in range(len(response_json["results"][i]["platforms"])):
                platform.append(response_json["results"][i]["platforms"][p]["platform"]["name"])

            # use NEXARDA for getting the description and price
            price_desc_dict = NEXARDA_Search().search("games", name)

            # if the the dictionary exists and the name is in the dictionary:
            if price_desc_dict and name in price_desc_dict: 
                price, desc = price_desc_dict[name]
                self.search_results_dict[name] = [rawg_id, platform, price, desc, playtime]
            else: 
                self.search_results_dict[name] = [rawg_id, platform, 0.00, 'unknown', playtime]
            

            if DEBUG:
                print(f'{i:<5}{rawg_id:<8}{name:<54}{" ".join(platform):<72}{price:<5}')
        
        return self.search_results_dict
    
    #==================#
    def top_games(self):
    #==================#
        
        '''
        This function gathers the top games by RAWG and exports them as a dictionary.
        '''
        self.top_results_dict = {}

        self.top_games_url = self.base_url + "games?" + self.api_key + "&-ordering=metacritic" 
        if DEBUG:
            print(self.top_games_url)
        response = requests.get(self.top_games_url)
        response_json = response.json()
        if DEBUG:
            print(response_json)

        if DEBUG:
            print(f'{"item":<5}{"Name":<54}{"Platform":<72}{"Playtime":<5}')

        for i in range(self.results_total):
            name = response_json["results"][i]["name"]
            rawg_id = response_json["results"][i]["id"]
            playtime = response_json["results"][i]["playtime"]
            if playtime == 0:
                playtime = "unknown"
            platform = []
            for p in range(len(response_json["results"][i]["platforms"])):
                platform.append(response_json["results"][i]["platforms"][p]["platform"]["name"])
            
            # use NEXARDA for getting the description and price
            price_desc_dict = NEXARDA_Search().search("games", name)
                
            # if the the dictionary exists and the name is in the dictionary:
            if price_desc_dict and name in price_desc_dict: 
                print("price, description:  ", price_desc_dict[name])
                price, desc = price_desc_dict[name]
                self.top_results_dict[name] = [rawg_id, platform, price, desc, playtime]
            else: 
                self.top_results_dict[name] = [rawg_id, platform, 0.00, 'unknown', playtime]

            if DEBUG:
                print(f'{i:<5}{name:<54}{" ".join(platform):<72}{playtime:<5}')
        
        return self.top_results_dict
    
    #=======================#
    def update_console(self):
    #=======================#
        '''
        This function retrieves all of the consoles from the RAWG database (51).
        '''

        # RAWG has 51 consoles => try to implement the next url to get all of the consoles.
        # create a function in which this function submits the url and console list and the
        # new function returns an updated list?

        self.update_consoles_list = []

        self.update_consoles_url = self.base_url + "platforms?" + self.api_key
        response = requests.get(self.update_consoles_url)
        response_json = response.json()

        # This is the total number of results for the first page of results.
        results_total = response_json["count"]
        page_results = len(response_json["results"])
        max_pages = math.ceil(results_total/page_results)
        
        for p in range(max_pages):

            for i in range(page_results):
                self.update_consoles_list.append(response_json["results"][i]["name"])

            if p > 1:
                # to get the next page add "&page=#" where # is the page number
                # Updating values for new page.
                response = requests.get(response_json["next"])
                response_json = response.json()
                page_results = len(response_json["results"])


        return self.update_consoles_list
    
    #===================#
    def update_mfg(self):
    #===================#
        
        self.update_mfg_dict = {}
        # 40 results is the max per page.
        self.update_mfg_url = self.base_url + "publishers?" + self.api_key + "&page_size=40"
        if DEBUG:
            print(self.update_mfg_url)
        response = requests.get(self.update_mfg_url)
        response_json = response.json()
        
        for i in range(len(response_json["results"])):
            name = response_json["results"][i]["name"]
            games = []
            
            for a in range(len(response_json["results"][i]["games"])):
                games.append(response_json["results"][i]["games"][a]["name"])

            self.update_mfg_dict[name] = games

        return self.update_mfg_dict

    
#===================#    
class NEXARDA_Search:
#===================#
    
    # NEXARDA => github.com/NEXARDA/NEXARDA
    def __init__(self):
        self.status_url = "https://www.nexarda.com/api/v3/status"
        self.search_url = "https://www.nexarda.com/api/v3/search?type="
        self.query = "q="
        self.results_total = 20
    
    #===============================#
    def search(self, category, name):
    #===============================#
        # DEBUG = True
        self.category = category
        self.search_results_dict = {} 

        # checking to see if the website is reachable
        website_status = requests.get(self.status_url)
        website_json = json.loads(website_status.content.decode('utf-8'))
        
        if DEBUG:
            print(website_json["online"])

        if website_json["online"] == True:
            if DEBUG:
                print("Nexarda is online")
        else:
            if DEBUG:
                print("Nexarda is unreachable. Exiting Program.")
            sys.exit()

        # Creating URL and sending request
        self.searchable_name = "+".join(name.split())
        search = requests.get(self.search_url + self.category + "&" + self.query + self.searchable_name)
        if DEBUG:
            print(self.search_url + self.category + "&" + self.query + self.searchable_name)
        search_json = json.loads(search.content.decode('utf-8'))
        if search_json["success"] == False:
            return None
     
        temp_total = search_json["results"]["total"]

        if self.results_total > temp_total:
            self.results_total = temp_total

        if DEBUG:
            print(f'{"item":<5}{"Name":<54}{"Lowest Price":<10}')

        for i in range(self.results_total):
            name = search_json["results"]["items"][i]["title"][:-7]
            lowest_price = search_json["results"]["items"][i]["game_info"]["lowest_price"]
            if lowest_price is None:
                lowest_price = 0.00
            elif lowest_price < 0.0:
                lowest_price = 0.00
            
            description = search_json["results"]["items"][i]["game_info"]["short_desc"]
            
            self.search_results_dict[name] = [lowest_price, description]
            
            if DEBUG:
                print(f'{i:<5}{name:<54}{lowest_price:<10}')
        
        return self.search_results_dict

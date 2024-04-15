import requests
import json
import re
import sys
import math

DEBUG = True
#================#
class RAWG_Search():
#================#    
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
        # print(self.category)
        self.searchable_name = "+".join(name.split())
        self.search_results_dict = {}

        self.search_url = self.base_url + self.category + self.api_key + "&search=" + self.searchable_name
        print(self.search_url)

        response = requests.get(self.search_url)
        response_json = response.json()
        # print(response_json)

        if DEBUG:
            print(f'{"item":<5}{"Name":<54}{"Platform":<72}{"Playtime":<5}')

        for i in range(self.results_total):
            name = response_json["results"][i]["name"]
            playtime = response_json["results"][i]["playtime"]
            if playtime == 0:
                playtime = "unknown"
            platform = []
            for p in range(len(response_json["results"][i]["platforms"])):
                platform.append(response_json["results"][i]["platforms"][p]["platform"]["name"])
            
            self.search_results_dict[name] = [platform, playtime]

            if DEBUG:
                print(f'{i:<5}{name:<54}{" ".join(platform):<72}{playtime:<5}')
        
        return self.search_results_dict
    
    #==================#
    def top_games(self):
    #==================#
        
        '''
        This function gathers the top games by RAWG and exports them as a dictionary.
        '''
        self.top_results_dict = {}

        self.top_games_url = self.base_url + "games?" + self.api_key + "&-ordering=metacritic" 
        response = requests.get(self.top_games_url)
        response_json = response.json()
        # print(response_json)

        if DEBUG:
            print(f'{"item":<5}{"Name":<54}{"Platform":<72}{"Playtime":<5}')

        for i in range(self.results_total):
            name = response_json["results"][i]["name"]
            playtime = response_json["results"][i]["playtime"]
            if playtime == 0:
                playtime = "unknown"
            platform = []
            for p in range(len(response_json["results"][i]["platforms"])):
                platform.append(response_json["results"][i]["platforms"][p]["platform"]["name"])
            self.top_results_dict[name] = [platform, playtime]

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

        # if DEBUG:
        #     print(response_json)
        
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
        response = requests.get(self.update_mfg_url)
        response_json = response.json()
        
        for i in range(len(response_json["results"])):
            name = response_json["results"][i]["name"]
            games = []
            
            for a in range(len(response_json["results"][i]["games"])):
                games.append(response_json["results"][i]["games"][a]["name"])

            self.update_mfg_dict[name] = games

        return self.update_mfg_dict
    
#================#
class RAWG_Pull:
#================#    
    '''
    This class uses the RAWG API to search for platforms and video games
    '''

    def __init__(self):
        self.api_key = "key=8583455b78234c0b940762d0141319c4"
        self.base_url = "https://api.rawg.io/api/"
        self.results_total = 20

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

        # if DEBUG:
        #     print(response_json)
        
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

    def search(self, category, name):

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

        self.searchable_name = "+".join(name.split())
        search = requests.get(self.search_url + self.category + "&" + self.query + self.searchable_name)
        search_json = json.loads(search.content.decode('utf-8'))
        # self.results_total = search_json["results"]["total"]
        if search_json["success"] == False:
            return search_json["message"]

        if DEBUG:
            print(f'{"item":<5}{"Name":<54}{"Lowest Price":<10}')

        for i in range(self.results_total):
            name = (search_json["results"]["items"][i]["title"][:-7])
            # year = (search_json["results"]["items"][i]["title"][-5:-1])
            lowest_price = ((re.findall(r"[$,\d]+[.,\d]+[.,\d]+[.,\d]", search_json["results"]["items"][i]["text"])))
            if lowest_price:
                lowest_price = lowest_price[0] 
            else:
                lowest_price = "Free"
            self.search_results_dict[name] = lowest_price
            
            if DEBUG:
                print(f'{i:<5}{name:<54}{lowest_price:<10}')
        
        return self.search_results_dict

import requests
import json
import re
import sys

DEBUG = True
#================#
class RAWG_Search:
#================#    
    '''
    This class uses the RAWG API to search for platforms and video games
    '''

    def __init__(self):
        self.api_key = "key=8583455b78234c0b940762d0141319c4"
        self.base_url = "https://api.rawg.io/api/"
        self.results_total = 20

    def search(self, category, name):

        self.category = category + "?"
        # print(self.category)
        self.searchable_name = "+".join(name.split())
        self.search_results_dict = {}

        self.search_url = self.base_url + self.category + self.api_key + "&search=" + self.searchable_name
        # print(self.url_name)

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
    
    def top_games(self):
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
        
        # if DEBUG:
        #     print("\nGame:  ", name)
        #     print("Search URL:  ", search.url)
        #     # print("Search:  ", search.content)
        #     print("Success?  ", search_json["success"])
        #     print("Total Results:  ", search_json["results"]["total"])

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

#=====================#    
class Top_Games_Update:
#=====================#
    
    
    def __init__(self):
        pass
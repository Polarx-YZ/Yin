import json
 
def init():
    with open("config.json", "r") as file:
        global config 
        config = json.load(file)
    with open("data/quotes.json", "r") as file:
        global quotes
        quotes = json.load(file)
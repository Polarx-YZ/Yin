import json

def init():
    with open("config.json", "r") as file:
        global config 
        config = json.load(file)
    print(config)
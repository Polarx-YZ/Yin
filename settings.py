import json

class Settings():
    def __init__(self):
        with open("config.json", "r") as file:
            self.config = config.json.load(file)

def init():
    with open("config.json", "r") as file:
        global config 
        config = json.load(file)
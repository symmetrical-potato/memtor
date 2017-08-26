import json


with open('cyberleninka.json') as file:
    data = json.load(file)

print(data)
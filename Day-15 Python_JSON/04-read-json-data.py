import json

with open("rg-data.json", "r") as file:
    data = json.load(file)
# json.load() = JSON file → Python object

print(data)

for rg in data:
    print(rg["name"] , rg["location"])

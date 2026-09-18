import json


# Python Dictionary → JSON String
data = {
    "name": "Amit",
    "role": "DevOps Engineer",
    "cloud": "Azure"
}

json_data = json.dumps(data)
print(type(json_data))
print(json_data)



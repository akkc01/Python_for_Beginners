import json


# json string to python object--
json_data = '''
{
    "name": "Amit",
    "role": "DevOps Engineer",
    "cloud": "Azure"
}
'''

data = json.loads(json_data)
print(data)




data = '{"name": "Amit", "cloud": "Azure"}'
result = json.loads(data)
print(result["name"])
print(result["cloud"])



# Python Dictionary → JSON String

data = {
    "name": "Amit",
    "role": "DevOps Engineer",
    "cloud": "Azure"
}

json_data = json.dumps(data)
print(json_data)

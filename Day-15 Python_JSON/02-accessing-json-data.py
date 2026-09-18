import json

json_data = '''
{
    "name": "Amit",
    "role": "DevOps Engineer",
    "cloud": "Azure"
}
'''
# accessing json data
data = json.loads(json_data)

print(data["name"])
print(data["role"])
print(data["cloud"])

# output : {'name': 'Amit', 'role': 'DevOps Engineer', 'cloud': 'Azure'}
# Now data is a Python dictionary.

# using the get() method
print(data.get("name"))
print(data.get("name","akkc"))  # just passing the default value


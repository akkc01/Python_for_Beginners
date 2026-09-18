import json

json_data = {
  "name": "aks-prod",
  "properties": {
    "location": "centralindia",
    "nodeCount": 3,
    "networkProfile": {
      "networkPlugin": "azure",
      "serviceCidr": "10.0.0.0/16"
    }
  }
}

data = json.loads(json_data)

#Access nested values:
print(data["properties"]["location"])

# Node count:
print(data["properties"]["nodeCount"])

# Network plugin:
print(data["properties"]["networkProfile"]["networkPlugin"])

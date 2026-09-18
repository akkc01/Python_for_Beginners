import json

# Read
with open("rg-output.json", "r") as file:
    data = json.load(file)

# Modify
data.append({
    "name": "rg-network-akkc",
    "location": "centralindia",
    "subscription": "akkc-Prod-Subscription",
    "environment": "shared-akkc"
})

# Write
with open("rg-output.json", "w") as file:
    json.dump(data, file, indent=4)


# output to console
with open("rg-output.json", "r") as file:
    data = json.load(file)
print(data)
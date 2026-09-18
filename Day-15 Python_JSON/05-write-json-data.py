import json

data = [
    {
        "name": "rg-dev",
        "location": "centralindia",
        "subscription": "Prod-Subscription",
        "environment": "shared"
    },
    {
        "name": "rg-prod",
        "location": "eastus",
        "subscription": "Dev-Subscription",
        "environment": "development"
    }
]

with open("rg-output.json", "w") as file:
    json.dump(data, file, indent=4)
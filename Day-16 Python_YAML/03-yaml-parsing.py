import yaml

with open("configmap.yaml", "r") as file:
    events = yaml.parse(file)

    for event in events:
        print(event)
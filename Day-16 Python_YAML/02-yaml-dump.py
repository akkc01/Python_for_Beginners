import yaml

data = {
    "name": "axion",
    "replicas": 3,
    "environment": "production"
}

dump = yaml.dump(data)
print(dump)

# upar wale data ko output.yaml me write kar dega.
with open("output.yaml", "w") as file:
    yaml.dump(data, file)


print("--------------------------------------------------------------------------")

# suing safe_dump()
data1 = {
"name": "axion",
"replicas": 3,
"enabled": True,
"version": 1.5,
"tags": ["python", "yaml", "kubernetes"]
}
print(yaml.safe_dump(data1))

with open("axion.yaml", "w") as file:
    yaml.safe_dump(data1, file)


print("--------------------------------------------------------------------------")
data3 = {
"name": "akkc",
"replicas": 10
}
with open("akkc.yaml", "w") as file:
    yaml.safe_dump(data3, file)

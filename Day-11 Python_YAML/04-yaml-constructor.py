import yaml

def custom_constructor(loader, node):
    value = loader.construct_scalar(node)
    return value.upper()

yaml.SafeLoader.add_constructor("!custom", custom_constructor)


yaml_data = """
value: !custom hello kaise hn Dosto, Aap sab ?
"""

data = yaml.safe_load(yaml_data)
print(data)
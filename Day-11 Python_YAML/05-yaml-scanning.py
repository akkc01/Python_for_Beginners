import yaml

with open("hpa.yaml", "r") as file:
    tokens = yaml.scan(file)

    for token in tokens:
        print(token)


print("--------------------------------------------------------------------------")
# If you don't want to print anything in the terminal and only want to save the output to a file.
with open("hpa.yaml", "r") as file:
    tokens = yaml.scan(file)

    with open("tokens.txt", "w") as output:
        for token in tokens:
            print(token, file=output)


# If you don't want to print anything in the terminal and only want to save the output to a file.
# do the same but diff way--
with open("hpa.yaml", "r") as file:
    tokens = yaml.scan(file)

    with open("tokens1.txt", "w") as output:
        for token in tokens:
            output.write(str(token) + "\n")
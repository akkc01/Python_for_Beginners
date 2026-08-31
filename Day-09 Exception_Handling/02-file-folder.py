import os

try:
    os.makedirs("rahul/python")
    print("python folder created")

except FileExistsError:
    print("devops folder already exists")



try:
    with open("rahul/python/devops.txt", "x") as f:
        f.write("Hello Dosto")
    print("File created")

except FileExistsError:
    print("File already exists")

# Open the file in read mode ("r")
file = open("readme.txt", "r")

# read() reads the entire file content at once
# It returns the complete content as a single string
content = file.read()
print("read():")
print(f"{content}\n")
file.close()


# Open the file again in read mode
file = open("readme.txt", "r")

# readline() reads only one line at a time
# It returns that line as a string
line = file.readline()
print("readline():")
print(f"{line}\n")
file.close()


# Open the file again in read mode
file = open("readme.txt", "r")

# readlines() reads all lines from the file
# It returns all lines as a list of strings
lines = file.readlines()
print("readlines():")
print(f"{lines}\n")
file.close()
# read() — Complete file read
file = open("readme.txt", "r") # # Open the file in read mode ("r")
content = file.read()  # read() reads the entire file content at once, It returns the complete content as a single string
print("read():")
print(f"{content}\n")
file.close()   # Close the file


# readline() — Read one line
file = open("readme.txt", "r")
line = file.readline()  # readline() reads only one line at a time, It returns that line as a string
print("readline():")
print(f"{line}\n")
file.close()


# readline() - Read Multiple 
file = open("readme.txt", "r")
line1 = file.readline()  # readline() reads only one line at a time, It returns that line as a string
line2 = file.readline()  # Read the second line
line3 = file.readline()  # Read the third line
print("readline():")
print(f"{line1}\n")
print(f"{line2}\n")
print(f"{line3}\n")
file.close()


# readlines() — Read all lines as a list
file = open("readme.txt", "r")
lines = file.readlines()  # readlines() reads all lines from the file, It returns all lines as a list of strings
print("readlines():")
print(f"{lines}\n")
file.close()


# with open() — Recommended approach
# Instead of manually doing close(), Python automatically closes the file when the with block finishes.
with open("readme.txt", "r") as file:  # Open the file in read mode using a context manager
    content = file.read()  # read() reads the entire file content
    print(content)
# File is automatically closed here
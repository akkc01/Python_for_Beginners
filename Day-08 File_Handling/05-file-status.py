# closed — Check whether file is closed
file = open("readme.txt", "r")  # Open the file in read mode ("r")
print(file.closed)  # Check whether the file is closed
file.close()
print(file.closed)  # Check again whether the file is closed


# mode — Check file mode
file = open("readme.txt", "r")  # Open the file in read mode ("r")
print(file.mode)  # mode returns the mode in which the file was opened
file.close()


#  name — Get file name
file = open("readme.txt", "r")  # Open the file in read mode ("r")
print(file.name)  # name returns the name of the opened file
file.close()

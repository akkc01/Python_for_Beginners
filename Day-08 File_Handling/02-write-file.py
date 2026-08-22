# write() — Write content to file

# write() writes a string into the file.
file = open("readme.txt", "w")  # Open the file in write mode ("w")
file.write("Hello, Python!")  # write() writes the given string into the file
file.close()
# Important: "w" mode deletes the existing content and writes new content.


# writelines() — Write multiple lines
file = open("readme.txt", "w")  # Open the file in write mode ("w")
lines = ["Hello\n", "Welcome to Python\n", "File Handling\n"]  # Create a list of strings
file.writelines(lines)  # writelines() writes multiple strings into the file
file.close()

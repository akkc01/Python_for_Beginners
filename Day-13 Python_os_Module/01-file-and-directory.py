import os

# Returns the current working directory.
print(os.getcwd())


# Changes the current working directory.
os.chdir("/tmp")
print(os.getcwd())


# Returns a list of files and directories in the current directory.
print(os.listdir())


# Returns a list of files and directories in a specific directory.
print(os.listdir("/tmp"))


# Creates a single directory.
os.mkdir("test")


# Creates directories recursively.
os.makedirs("project/config/dev")


# Creates directories recursively and does not raise an error
# if the directory already exists.
os.makedirs("project/logs", exist_ok=True)


# Removes a file.
os.remove("test.txt")


# Removes a file.
# os.unlink() is another name for removing a file.
os.unlink("test.txt")


# Removes an EMPTY directory.
os.rmdir("test")


# Renames a file or directory.
os.rename("old.yaml", "new.yaml")


# Renames a file or directory and replaces the destination if it exists.
os.replace("old.yaml", "new.yaml")



# DIRECTORY WALKING

# Recursively walks through a directory and its subdirectories.
for root, dirs, files in os.walk("."):

    # Current directory path.
    print(root)

    # Directories inside the current directory.
    print(dirs)

    # Files inside the current directory.
    print(files)


# FIND YAML FILES RECURSIVELY
# Recursively finds all YAML files inside the manifests directory.
for root, dirs, files in os.walk("manifests"):

    for file in files:

        # Checks whether the file ends with .yaml.
        if file.endswith(".yaml"):

            # Combines directory path and filename.
            print(os.path.join(root, file))


# SCAN DIRECTORY
# Iterates through files and directories in a directory.
with os.scandir(".") as entries:

    for entry in entries:

        # Returns the name of the file or directory.
        print(entry.name)

        # Returns True if the entry is a file.
        if entry.is_file():
            print("File")


        # Returns True if the entry is a directory.
        if entry.is_dir():
            print("Directory")


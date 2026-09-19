import os

# PATH OPERATIONS

# Converts a relative path into an absolute path.
print(os.path.abspath("deployment.yaml"))


# Returns the filename from a path.
print(os.path.basename(
    "/Users/amit/project/deployment.yaml"
))


# Returns the directory part of a path.
print(os.path.dirname(
    "/Users/amit/project/deployment.yaml"
))


# Joins multiple path components correctly.
print(os.path.join(
    "project",
    "config",
    "deployment.yaml"
))


# Splits a path into directory and filename.
print(os.path.split(
    "/Users/amit/project/deployment.yaml"
))


# Splits filename and extension.
print(os.path.splitext("deployment.yaml"))


# Returns True if the path is absolute.
print(os.path.isabs("/Users/amit/project"))


# Normalizes a path by resolving . and ..
print(os.path.normpath(
    "project/./config/../deployment.yaml"
))


# Returns the real/canonical path.
print(os.path.realpath("deployment.yaml"))





# COMMON PATH

paths = [
    "/Users/amit/project/app.py",
    "/Users/amit/project/config.yaml"
]

# Returns the common path shared by multiple paths.
print(os.path.commonpath(paths))


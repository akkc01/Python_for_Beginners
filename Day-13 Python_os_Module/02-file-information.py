import os

# Returns the size of a file in bytes.
print(os.path.getsize("deployment.yaml"))


# Returns the last modification time of a file as a timestamp.
print(os.path.getmtime("deployment.yaml"))


# Returns the last access time of a file as a timestamp.
print(os.path.getatime("deployment.yaml"))


# Returns metadata change time on macOS/Linux.
# It is NOT necessarily the file creation time.
print(os.path.getctime("deployment.yaml"))


# Returns True if the path exists.
print(os.path.exists("deployment.yaml"))


# Returns True if the path is a file.
print(os.path.isfile("deployment.yaml"))


# Returns True if the path is a directory.
print(os.path.isdir("venv"))



# FILE METADATA

# Returns detailed metadata about a file or directory.
info = os.stat("deployment.yaml")

print(info)


# Returns the file size in bytes.
print(info.st_size)


# Returns the last modification timestamp.
print(info.st_mtime)


# FILE PERMISSIONS

# Changes file permissions.
# 0o755 means owner can read/write/execute,
# while group and others can read/execute.
os.chmod("script.sh", 0o755)
import os

# ENVIRONMENT VARIABLES

# Returns all environment variables.
print(os.environ)


# Returns the value of an environment variable.
print(os.environ.get("USER"))


# Returns the value of an environment variable.
print(os.getenv("USER"))


# Returns the value of ENV.
# If ENV does not exist, returns "development".
print(os.getenv("ENV", "development"))


# Sets an environment variable for the current Python process.
os.environ["ENV"] = "production"

print(os.environ["ENV"])


# Deletes an environment variable.
del os.environ["ENV"]


# Creates an environment variable.
os.environ["TEMP"] = "hello"


# Deletes an environment variable safely.
# None means no error if the variable does not exist.
os.environ.pop("TEMP", None)

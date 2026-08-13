
# Type Conversion

# String to Integer
age = "30"
age = int(age)

print(age)
print(type(age))


# Integer to Float
number = 10
number = float(number)

print(number)
print(type(number))


# Integer to String
number = 100
number = str(number)

print(number)
print(type(number))


# String to Float
salary = "75000.50"
salary = float(salary)

print(salary)
print(type(salary))


# List to Tuple
languages = ["Python", "Java", "Go"]
languages = tuple(languages)

print(languages)
print(type(languages))


# Tuple to List
languages = ("Python", "Java", "Go")
languages = list(languages)

print(languages)
print(type(languages))


# Set
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)
print(type(unique_numbers))


# Dictionary
user = {
    "name": "Amit",
    "role": "Cloud Engineer"
}

print(user)
print(type(user))


# Checking Multiple Data Types
name = "Amit"                    # str
age = 30                         # int
salary = 75000.50               # float
complex_number = 3 + 5j          # complex
is_active = True                 # bool
languages = ["Python", "Go"]     # list
coordinates = (10, 20)           # tuple
unique_numbers = {1, 2, 3}       # set
user = {"name": "Amit"}          # dict
result = None                    # NoneType

print(type(name))
print(type(age))
print(type(salary))
print(type(complex_number))
print(type(is_active))
print(type(languages))
print(type(coordinates))
print(type(unique_numbers))
print(type(user))
print(type(result))


# Real-World Example
application_name = "MyApp"                    # str
replicas = 3                                  # int
cpu_limit = 2.5                               # float
version = 1 + 2j                              # complex
is_deployed = True                            # bool
services = ["Docker", "Kubernetes"]           # list
ports = (80, 443)                             # tuple
environments = {"dev", "qa", "prod"}          # set

application = {
    "name": application_name,
    "replicas": replicas,
    "deployed": is_deployed
}                                             # dict

status = None                                 # NoneType

print(application_name)
print(replicas)
print(cpu_limit)
print(version)
print(is_deployed)
print(services)
print(ports)
print(environments)
print(application)
print(status)
# Python Variables

# A variable is a name used to store a value in memory.
# Python variables are created when you assign a value to them.


# Creating a Variable

name = "Amit"
age = 30
salary = 75000

print(name)
print(age)
print(salary)


# Variable with Different Data Types

name = "Amit"          # String
age = 30               # Integer
salary = 75000.50      # Float
is_active = True       # Boolean

print(name)
print(age)
print(salary)
print(is_active)


# Checking Variable Type

name = "Amit"
age = 30

print(type(name))
print(type(age))


# Assigning Multiple Variables

name, age, city = "Amit", 30, "Pune"

print(name)
print(age)
print(city)


# Assigning the Same Value to Multiple Variables

x = y = z = 100

print(x)
print(y)
print(z)


# Reassigning a Variable

name = "Amit"

print(name)

name = "Kumar"

print(name)


# Variable Value Can Change Its Data Type

value = 100

print(value)
print(type(value))

value = "Python"

print(value)
print(type(value))


# Variable Names are Case-Sensitive

name = "Amit"
Name = "Kumar"

print(name)
print(Name)


# Valid Variable Names

first_name = "Amit"
last_name = "Verma"
age1 = 30
_cloud = "Azure"
user_name = "admin"

print(first_name)
print(last_name)
print(age1)
print(_cloud)
print(user_name)


# Invalid Variable Names
# Variable names cannot start with a number.
# Variable names cannot contain spaces.
# Python keywords cannot be used as variable names.

# 1name = "Amit"          # Invalid
# first name = "Amit"     # Invalid
# class = "Python"        # Invalid


# Variable Naming Convention

first_name = "Amit"
last_name = "Verma"
date_of_birth = "1995"

print(first_name)
print(last_name)
print(date_of_birth)


# Constants

# Python does not have a strict constant keyword.
# By convention, constants are written in uppercase.

PI = 3.14159
MAX_CONNECTIONS = 100
APP_NAME = "MyApplication"

print(PI)
print(MAX_CONNECTIONS)
print(APP_NAME)


# Variables with Expressions

a = 10
b = 20

sum_value = a + b
difference = b - a
product = a * b

print(sum_value)
print(difference)
print(product)


# Variables with User Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)


# Deleting a Variable

name = "Amit"

print(name)

del name

# print(name)    # NameError because the variable was deleted


# Checking if a Variable Exists

name = "Amit"

if "name" in globals():
    print("Variable exists")


# Multiple Data Types in Variables

username = "admin"
port = 8080
version = 1.5
enabled = True
services = ["Docker", "Kubernetes", "Terraform"]

print(username)
print(port)
print(version)
print(enabled)
print(services)


# Real-World Example

application_name = "MyApp"
environment = "production"
replicas = 3
cpu_limit = 2.0
is_deployed = True

print("Application:", application_name)
print("Environment:", environment)
print("Replicas:", replicas)
print("CPU Limit:", cpu_limit)
print("Deployed:", is_deployed)

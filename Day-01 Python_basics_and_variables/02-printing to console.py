# 🖨️ Python print()
# The print() function is used to display output on the screen in Python.


# Basic Syntax

print("Hello, World!")


# Printing Text

print("Hello")
print("Welcome to Python")


# Printing Numbers

print(10)
print(10 + 20)
print(10 * 5)


# Printing Variables

name = "Amit"
age = 30

print(name)
print(age)


# Printing Multiple Values

name = "Amit"
age = 30

print(name, age)


# sep Parameter
# The sep parameter defines what is placed between multiple values.

print("Amit", "Kumar", "Verma", sep="-")

print("2026", "08", "12", sep="/")


# end Parameter
# By default, print() adds a newline after printing.

print("Hello")
print("World")

print("Hello", end="-")
print("World")

print("Hello", end="**")
print("World")


# Escape Characters

# New Line - \n
print("Hello Dosto\nMera Naam\nAmit Hai")

# # Tab - \t
print("Hello Dosto\tMera Naam\tAmit Hai")
print("Name\tAge")
print("Amit\t30")

Quote
print("Hi Friends \"To Kaise Hn Aap log?\"")


# Printing with Variables

# Using comma

name = "Amit"
age = 30

print("Name:", name)
print("Age:", age)
print("Hi Dosto, Mera Naam", name, "Hai aur Mai", age, "Saal Ka Hoon.")


# Using f-string

name = "Amit"
age = 30

print(f"My name is {name} and I am {age} years old.")


# Printing Expressions

a = 10
b = 20

print(a + b)
print(a * b)
print(a > b)


# Printing Different Data Types

name = "Amit"
age = 30
salary = 75000.50
is_active = True

print(name)
print(age)
print(salary)
print(is_active)


# Printing Lists

languages = ["Python", "Java", "Go"]

print(languages)


# Printing Dictionaries

user = {
    "name": "Amit",
    "role": "DevOps Engineer"
}

print(user)


# Important print() Parameters

# *objects  -> Values to print
# sep       -> Separator between values
# end       -> Character/string printed at the end
# file      -> Where the output is written
# flush     -> Whether to forcibly flush the output

print("Python", "Docker", "Kubernetes", sep=" | ", end="\n")


# Real-World Example

name = "Amit"
role = "Cloud & DevOps Engineer"
experience = 7

print("Name:", name)
print("Role:", role)
print("Experience:", experience, "years")
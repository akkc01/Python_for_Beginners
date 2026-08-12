# ⌨️ Python input()
#
# The input() function is used to take input from the user through the keyboard.


# Basic Syntax

name = input("Enter your name: ")

print(name)


# Taking String Input

name = input("Enter your name: ")

print(name)
print(type(name))


# Taking Integer Input

age = int(input("Enter your age: "))

print(age)
print(type(age))


# Taking Float Input

salary = float(input("Enter your salary: "))

print(salary)
print(type(salary))


# Taking Boolean Input

value = input("Are you active? ")

is_active = value.lower() == "yes"

print(is_active)


# Taking Multiple Inputs

# Using Multiple input() Statements

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)


# Taking Multiple Values in One Line

name, city = input("Enter name and city: ").split()

print("Name:", name)
print("City:", city)


# Taking Multiple Numbers

a, b = map(int, input("Enter two numbers: ").split())

print("Sum:", a + b)


# Using input() with if

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")


# Using input() with Loops

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Important Point
# input() always returns a string.

age = input("Enter your age: ")

print(type(age))


# Type Conversion

age = int(input("Enter your age: "))

print(age)
print(type(age))


# Common Type Conversions

# String
name = input("Enter name: ")

# Integer
age = int(input("Enter age: "))

# Float
salary = float(input("Enter salary: "))

# Boolean
value = input("Are you active? ")
is_active = value.lower() == "yes"

# Multiple values
name, city = input("Enter name and city: ").split()

# Multiple integers
a, b = map(int, input("Enter two numbers: ").split())


# Real-World Example

name = input("Enter your name: ")
age = int(input("Enter your age: "))
role = input("Enter your role: ")

print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Role:", role)

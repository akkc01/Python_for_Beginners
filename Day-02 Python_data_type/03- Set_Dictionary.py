# 8. Set (set)
# Used to store unique values.
# Sets are unordered and mutable.

numbers = {1, 2, 3, 4, 5}

print(numbers)
print(type(numbers))


# Duplicate Values are Removed

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)


# 9. Dictionary (dict)
# Used to store data in key-value pairs.

user = {
    "name": "Amit",
    "age": 30,
    "role": "DevOps Engineer"
}

print(user)
print(type(user))


# Accessing Dictionary Values

print(user["name"])
print(user["role"])


# 10. None (NoneType)
# Used to represent no value or absence of a value.

result = None

print(result)
print(type(result))


# Checking Data Type

name = "Amit"
age = 30
salary = 75000.50
is_active = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))


# Set (set)
# Used to store unique values.
# Sets are unordered and mutable.

numbers = {1, 2, 3, 4, 5}

print(numbers)
print(type(numbers))


# Duplicate Values are Removed
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

# ----------------------------------------------------
#  Dictionary (dict)
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


# Dictionary Operations--
friends_data = {
    "name": "Amit",
    "age": 30,
    "city": "Pune"
}

print(f"Hi, It's our Dictionary: {friends_data}")
print(friends_data["name"])
print(friends_data.get("name"))
friends_data["email"] = "amit@example.com"
print(f"Hi, It's our Dictionary: {friends_data}")

friends_data.update({
    "phone": "9876543210",
    "country": "India"
})

print(f"Hi, It's our Dictionary: {friends_data}")

friends_data["age"] = 31 # existing values change
print(f"Hi, It's our Dictionary: {friends_data}")
friends_data.update({"age": 32})
print(f"Hi, It's our Dictionary: {friends_data}")

del friends_data["city"]
print(f"Hi, It's our Dictionary: {friends_data}")
friends_data.pop("email")
print(f"Hi, It's our Dictionary: {friends_data}")

country = friends_data.pop("country")
print(f"Hi removed Country is: {country}")
print(f"Hi, It's our Dictionary: {friends_data}")

friends_data.popitem() # remove last key:value
print(f"Hi, It's our Dictionary: {friends_data}")
friends_data.clear()
print(f"Hi, It's our Dictionary: {friends_data}")




# None (NoneType)
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


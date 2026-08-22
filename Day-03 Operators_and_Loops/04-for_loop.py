# Python Loops ----
# Loops are used to execute a block of code repeatedly. Python mainly provides two types of loops:

    # 1. for loop
    # 2. while loop

# Python also provides:
    # - break
    # - continue
    # - pass



# for LOOP ----------------------------
# A for loop is used to iterate over a sequence such as: list, tuple, string, set, dictionary, or range.

# Basic for Loop
for i in range(54):
    print(i)


# for Loop with range()
for i in range(1, 55):   # range(start, stop)
    print(i)


# range(start, stop, step)
for i in range(1, 10, 3):
    print(i)


# Reverse Loop
print("Reverse Range Start")
for i in range(10, 0, -1):
    print(i)


# Loop Through a String
print("looping on string")
name = "Python"
for character in name:
    print(character)


# Loop Through a List
languages = ["Python", "Java", "Go", "C++"]
for lang in languages:
    print(lang)


# Loop Through a Tuple
numbers = (10, 20, 30, 40)
for num in numbers:
    print(num)


# Loop Through a Set
languages = {"Python", "Java", "Go"}
for language in languages:
    print(language)


# Loop Through a Dictionary
user = {
    "name": "Amit",
    "age": 30,
    "role": "DevOps Engineer"
}

for key in user:
    print(key)

# Get Dictionary Values
for value in user.values():
    print(value)

# Get Dictionary Keys and Values
for key, value in user.items():
    print(key, ":", value)


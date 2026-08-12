# 🔄 Python Loops
#
# Loops are used to execute a block of code repeatedly.
#
# Python mainly provides two types of loops:
#
# 1. for loop
# 2. while loop
#
# Python also provides:
# - break
# - continue
# - pass


# ============================================================
# 1. for LOOP
# ============================================================
# A for loop is used to iterate over a sequence such as:
# list, tuple, string, set, dictionary, or range.


# Basic for Loop

for i in range(5):
    print(i)


# Output:
# 0
# 1
# 2
# 3
# 4


# for Loop with range()

for i in range(1, 6):
    print(i)


# Output:
# 1
# 2
# 3
# 4
# 5


# range(start, stop, step)

for i in range(1, 10, 2):
    print(i)


# Output:
# 1
# 3
# 5
# 7
# 9


# Reverse Loop

for i in range(5, 0, -1):
    print(i)


# Output:
# 5
# 4
# 3
# 2
# 1


# ============================================================
# Loop Through a String
# ============================================================

name = "Python"

for character in name:
    print(character)


# ============================================================
# Loop Through a List
# ============================================================

languages = ["Python", "Java", "Go", "C++"]

for language in languages:
    print(language)


# ============================================================
# Loop Through a Tuple
# ============================================================

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# ============================================================
# Loop Through a Set
# ============================================================

languages = {"Python", "Java", "Go"}

for language in languages:
    print(language)


# ============================================================
# Loop Through a Dictionary
# ============================================================

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


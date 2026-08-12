
# ============================================================
# break
# ============================================================
# break is used to immediately stop the loop.


for i in range(1, 10):
    if i == 5:
        break

    print(i)


# Output:
# 1
# 2
# 3
# 4


# break with while Loop

count = 1

while count <= 10:
    if count == 6:
        break

    print(count)
    count += 1


# ============================================================
# continue
# ============================================================
# continue skips the current iteration
# and moves to the next iteration.


for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# Output:
# 1
# 2
# 4
# 5


# continue with while Loop

count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)


# ============================================================
# pass
# ============================================================
# pass does nothing.
# It is used as a placeholder when code is required syntactically
# but you do not want to execute anything yet.


for i in range(5):
    pass


# ============================================================
# Nested Loops
# ============================================================
# A loop inside another loop is called a nested loop.


for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# ============================================================
# Nested Loop Example - Multiplication Table
# ============================================================

for i in range(1, 4):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)


# ============================================================
# for Loop with if
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)


# ============================================================
# Find Even and Odd Numbers
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# ============================================================
# Loop with else
# ============================================================
# Python allows an else block with loops.
# The else block executes when the loop finishes normally.


for i in range(5):
    print(i)
else:
    print("Loop completed")


# ============================================================
# for Loop with else and break
# ============================================================
# If break is executed, the else block does not execute.


numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        print("Number found")
        break
else:
    print("Number not found")


# ============================================================
# enumerate()
# ============================================================
# enumerate() provides both index and value.


languages = ["Python", "Java", "Go"]

for index, language in enumerate(languages):
    print(index, language)


# ============================================================
# zip()
# ============================================================
# zip() allows us to iterate over multiple sequences together.


names = ["Amit", "Rahul", "Neha"]
ages = [30, 28, 25]

for name, age in zip(names, ages):
    print(name, age)


# ============================================================
# List Comprehension
# ============================================================
# List comprehension provides a short way to create lists.


numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# List Comprehension with Condition

even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]

print(even_numbers)


# ============================================================
# Real-World Example
# ============================================================

services = [
    "Azure",
    "Terraform",
    "Docker",
    "Kubernetes",
    "Ansible"
]

for service in services:
    print("Working with:", service)


# ============================================================
# Real-World Example - Deployment Check
# ============================================================

services = {
    "frontend": "running",
    "backend": "running",
    "database": "stopped"
}

for service, status in services.items():

    if status == "running":
        print(service, "is healthy")

    else:
        print(service, "needs attention")


# ============================================================
# Summary
# ============================================================
#
# for       -> Iterates over a sequence
# while     -> Runs while a condition is True
# break     -> Stops the loop
# continue  -> Skips the current iteration
# pass      -> Placeholder
# enumerate -> Gets index and value
# zip       -> Iterates over multiple sequences
# range     -> Generates a sequence of numbers
# nested    -> Loop inside another loop

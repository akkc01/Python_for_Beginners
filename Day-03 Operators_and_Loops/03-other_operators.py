# Identity Operators --------
# Identity operators compare whether two variables, refer to the same object in memory.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)


#  Membership Operators ----------
# Used to check whether a value exists in a sequence.
languages = ["Python", "Java", "Go"]

print("Python" in languages)
print("C++" in languages)
print("C++" not in languages)


# Membership with String
name = "Amit Kumar"
print("Amit" in name)
print("Python" in name)


# Membership with Dictionary
user = {
    "name": "Amit",
    "role": "DevOps Engineer"
}

print("name" in user)
print("age" in user)


# 7. Bitwise Operators ------------
# Bitwise operators work at the binary level.

a = 10
b = 3

# Bitwise AND
print(a & b)

# Bitwise OR
print(a | b)

# Bitwise XOR
print(a ^ b)


# Bitwise NOT
print(~a)


# Left Shift
print(a << 1)


# Right Shift
print(a >> 1)



# Operator Precedence --------------
# Python follows a specific order when evaluating expressions.
# Common order:
    # 1. ()
    # 2. **
    # 3. *, /, //, %
    # 4. +, -
    # 5. Comparison operators
    # 6. not
    # 7. and
    # 8. or


result = 10 + 5 * 2
print(result)


# Parentheses change the order of execution.
result = (10 + 5) * 2
print(result)


# Arithmetic Operator Example

price = 100
quantity = 5

total = price * quantity

print("Total:", total)


# Comparison Operator Example
marks = 75

if marks >= 60:
    print("Pass")
else:
    print("Fail")


# Logical Operator Example
age = 25
experience = 5

if age >= 18 and experience >= 3:
    print("Eligible")



# Membership Operator Example
services = [
    "Azure",
    "AWS",
    "Docker",
    "Kubernetes"
]
if "Docker" in services:
    print("Docker is available")



# Real-World DevOps Example
cpu_usage = 75
memory_usage = 80
service_status = "running"

if cpu_usage > 90 or memory_usage > 90:
    print("High resource utilization")

if service_status == "running":
    print("Service is healthy")

if "Docker" in services:
    print("Docker is installed")


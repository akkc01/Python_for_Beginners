# Integer (int)
# Used to store whole numbers.
# Integers can be positive, negative, or zero.

age = 30
count = 100
negative_number = -50
zero = 0

print(age)
print(count)
print(negative_number)
print(zero)

# Check the data type
print(type(age))


# Integer Arithmetic Operations
a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation


# Integer Conversion
number = "50"

number = int(number)

print(number)
print(type(number))


# Check Integer Type


print(isinstance(age, int))

# ============================================================
# Float (float)
# Used to store decimal numbers.
# Floats can be positive, negative, or zero.
# They are commonly used for salary, percentage, temperature, price, etc.

salary = 75000.50
percentage = 95.5
temperature = -10.5
zero = 0.0

print(salary)
print(percentage)
print(temperature)
print(zero)

# Check the data type
print(type(salary))



# Float Arithmetic Operations
a = 10.5
b = 2.5

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation


# Float Conversion
number = "95.5"

number = float(number)

print(number)
print(type(number))



# Integer to Float
number = 100

number = float(number)

print(number)
print(type(number))



# Check Float Type
print(isinstance(salary, float))



# Complex (complex)
# ============================================================
# Used to store complex numbers.
# A complex number contains:
# 1. Real part
# 2. Imaginary part
# Python uses 'j' to represent the imaginary part.

number = 3 + 5j

print(number)
print(type(number))

# Get real and imaginary parts
print(number.real)
print(number.imag)

# Complex number operations
a = 3 + 2j
b = 1 + 4j

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division



# Boolean (bool)
# ============================================================
# Used to represent True or False.
# Boolean values are mainly used in conditions and comparisons.

is_active = True
is_deleted = False

print(is_active)
print(is_deleted)
print(type(is_active))

# Boolean values with conditions
age = 25

is_adult = age >= 18

print(is_adult)
print(type(is_adult))


# Boolean operators
a = True
b = False

print(a and b)  # AND
print(a or b)   # OR
print(not a)    # NOT


# Boolean from comparison
x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x > y)    # False
print(x <= y)   # True
print(x >= y)   # False
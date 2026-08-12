
# ============================================================
# 3. Comparison Operators
# ============================================================
# Used to compare two values.
# The result is always True or False.


a = 10
b = 20

print(a == b)    # Equal to
print(a != b)    # Not equal to
print(a > b)     # Greater than
print(a < b)     # Less than
print(a >= b)    # Greater than or equal to
print(a <= b)    # Less than or equal to


# Example

age = 25

print(age >= 18)


# ============================================================
# 4. Logical Operators
# ============================================================
# Used to combine multiple conditions.


age = 30
has_license = True


# and
# Returns True if both conditions are True.

print(age >= 18 and has_license)


# or
# Returns True if at least one condition is True.

print(age >= 18 or has_license)


# not
# Reverses the result.

print(not has_license)


# Example

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful")

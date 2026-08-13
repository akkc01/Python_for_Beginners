# Comparison Operators -----------
# Used to compare two values. The result is always True or False.

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


# Logical Operators--------------------
# Used to combine multiple conditions.

print(f"Hi Now Working with Logical operators")
age = 20
has_license = True

# Returns True if both conditions are True.
print(age >= 18 and has_license)


# Returns True if at least one condition is True.
print(age >= 18 or has_license)

# Reverses the result.
print(not has_license)

# Example
username = "admin"
password = "123456"

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Login Failed, Please Enter Right Credencials")


username = str(input("Enter your Username: "))
password = int(input("Enter Your Password: "))

if username == "admin" and password == 12345:
    print("Login successful")
else:
    print("Login Failed, Please Enter Right Credentials")


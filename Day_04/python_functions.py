# Functions in Python

# Function is define to add two numbers
def add(a, b): 
    return a + b

# Function id defined to sum two numbers taken as input from the user
def sum():
    a = int(input(f"Enter your First Number:\n"))
    b = int(input(f"Enter your Second Number: \n"))
    sum = a+b
    print(f"Sum of {a} and {b} is:",sum)




# Calling the Add Function
print(add(50,60))

x=20
y=40
print(add(x,y))

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# result = add(a, b)
# print(f"Sum of {a} and {b} is: {result}")



# Calling the Sum Function

env = str(input("Enter the Environment: "))

if env=="prod":
    print("Sum of the Numbers are allowed in production environment")
    sum()   # Calling the Sum Function
elif env=="stagging" or env=="dev":
    print("Sum of Numbers are not allowed in stagging and development environment")
else:
    print("Invalid Environment")
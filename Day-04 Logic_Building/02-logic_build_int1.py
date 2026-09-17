# Here we will going to practice of Operators and logic building
# Retry until valid input
# here break statement is used to immediately exit the loop once a valid operator is entered.


x = int(input("Enter first number : "))
y = int(input("Enter second number : "))


while True:
    opr = input("Enter the operator (+, -, *, /, %): ")

    if opr == "+":
        print(f"The sum of {x} and {y} is: {x+y}")
        break

    elif opr == "-":
        print(f"The difference of {x} and {y} is: {x-y}")
        break

    elif opr == "*":
        print(f"The product of {x} and {y} is: {x*y}")
        break

    elif opr == "/":
        print(f"The division of {x} and {y} is: {x/y}")
        break

    elif opr == "%":
        print(f"The modulus of {x} and {y} is: {x%y}")
        break

    else:
        print("Invalid operator! Please try again.\n")




# Same logic with list and in operator


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

valid_opr = ["+", "-", "*", "/", "%"]

while True:
    opr = input("Enter operator (+, -, *, /, %): ")

    if opr in valid_opr:
        break
    else:
        print("Invalid operator! Please try again.")

if opr == "+":
    print(a + b)
elif opr == "-":
    print(a - b)
elif opr == "*":
    print(a * b)
elif opr == "/":
    print(a / b)
elif opr == "%":
    print(a % b)
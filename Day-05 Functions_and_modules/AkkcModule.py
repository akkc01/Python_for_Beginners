def akkc():
    print("Hi Friends, This is from the akkc module.")


def akkc2():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 > num2:
            print(f"The number {num1} is greater than the number {num2}")
        elif num2 > num1:
            print(f"The number {num2} is greater than the number {num1}")
        else:
            print(f"Both numbers are equal: {num1}")

        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Calling the function from the same file
# akkc2()



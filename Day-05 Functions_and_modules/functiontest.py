# define function1
def oddEven(num1):
    if num1 % 2 == 0:
        print(f"Your number {num1} is Even")
    else:
        print(f"Your number {num1} is Odd")

# define function2
def oddEven1(num1):
    if num1 % 2 == 0:
        return f"Your number {num1} is Even"
    else:
        return f"Your number {num1} is Odd"

# define function3
def oddEven2(num1):
    if num1 % 2 == 0:
        return f"Your number {num1} is Even"
    else:
        return f"Your number {num1} is Odd"


# # Calling the functions
# oddEven(501)
# print(oddEven1(5000))

# x = int(input("Enter your number: "))
# print(oddEven2(x))
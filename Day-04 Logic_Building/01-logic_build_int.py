# Here we will going to practice of Operators and logic building

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

opr = input("Enter the operator : (options: +, -, *, /, %) ")

if opr == "+":
    print(f"The sum of {x} and {y} is : {x+y}\n")
elif opr == "-":
    print(f"The difference of {x} and {y} is : {x-y}\n")
elif opr == "*":
    print(f"The product of {x} and {y} is : {x*y}\n")
elif opr == "/":
    print(f"The division of {x} and {y} is : {x/y}\n")
elif opr == "%":
    print(f"The Modulus of {x} and {y} is : {x%y}\n")
else:
    print(f"Invalid Operator \n")



if x > y:
    print(f"{x} is greater than {y} ")
else:
    print(f"{y} is greater than {x} ")
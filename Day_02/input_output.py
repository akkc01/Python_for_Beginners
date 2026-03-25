
# age = int(input("Enter your age: "))    # input() function is used to take input from the user. It returns a string. We can convert it to int using int() function.
# user = str(input("Enter your name: "))  # str() function is used to convert the input to string. It is not necessary here as input() already returns a string, but it is used for clarity.
# print("Hello ",user,"! Your age is ",age)


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("The sum of a and b is ",a+b)
# print("The difference of a and b is ",a-b)
# print("The product of a and b is ",a*b)
# print("The quotient of a and b is ",a/b)



env = input("Enter the environment you want to work in (dev, staging, prod): ")


if env=="prod":
    print("App Deployment is not allowed in production environment")
elif env=="staging" or env=="dev":
    print("App Deployment is allowed only in staging and development environment")
else:
    print("Invalid environment")



if env=="prod":
    print("Deployment is not allowed on Friday in production environment")

elif env=="staging":
    print("Take backup of the database and Test the application on staging environment before deploying to production environment")

elif env=="dev":
    print("Deployment is allowed on all days in staging and development environment")

else:
    print("Invalid environment")
# Python Data Types--
# Data types define the type of value stored in a variable. Python has several built-in data types.

# String (str) Used to store text.
name = "Amit"
city = 'Pune'
message = """Welcome to Python"""

print(name)
print(city)
print(message)


# 2. String Indexing
name = "Python"

print(name[0])      # P
print(name[1])      # y
print(name[-1])     # n
print(name[-2])     # o


# 3. String Length
print(len(name))


# 4. String Slicing
print(name[0:3])    # Pyt
print(name[:3])     # Pyt
print(name[2:])     # thon
print(name[1:5])    # ytho
print(name[:])      # Python


# 5. Slicing with Step
print(name[::2])    # Pto
print(name[::3])    # Ph



# 6. Reverse String
print(name[::-1])   # nohtyP


# 7. String Concatenation
first_name = "Amit"
last_name = "Kumar"

full_name = first_name + " " + last_name
print(full_name)


# 8. String Repetition
message = "Hello "
print(message * 3)



# 9. Membership Operators
text = "Python is easy"

print("Python" in text)          # True
print("Java" in text)            # False
print("Java" not in text)        # True


# 10. upper()
name = "amit kumar"
print(name.upper())


# 11. lower()
name = "AMIT KUMAR"
print(name.lower())


# 12. capitalize()
name = "amit kumar"
print(name.capitalize())


# 13. title()
name = "amit kumar verma"
print(name.title())


# 14. swapcase()
text = "Hello PYTHON"
print(text.swapcase())


# 15. casefold()
username = "ADMIN"
print(username.casefold())

if username.casefold() == "admin":
    print("Valid User")


# 16. strip()
name = "   Amit   "
print(name.strip())


# 17. lstrip()
name = "   Amit"
print(name.lstrip())


# 18. rstrip()
name = "Amit   "
print(name.rstrip())


# 19. strip() with Characters
text = "###Python###"
print(text.strip("#"))


# 20. replace()
message = "I like Java"
message = message.replace("Java", "Python")

print(message)


# Limit number of replacements
text = "apple apple apple"
print(text.replace("apple", "mango", 2))


# 21. find()
text = "I am learning Python"
print(text.find("Python"))       # Position
print(text.find("Java"))         # -1


# 22. index()
text = "I am learning Python"
print(text.index("Python"))

# If the text is not found, index() raises ValueError.
# print(text.index("Java"))

# 23. count()
text = "banana"
print(text.count("a"))           # 3
text = "Python is easy and Python is powerful"

print(text.count("Python"))      # 2


# 24. startswith()
url = "https://example.com"
print(url.startswith("https"))


# 25. endswith()
filename = "data.csv"
print(filename.endswith(".csv"))


# 26. split()
name = "Amit Kumar Verma"
result = name.split()

print(result)


# Split using delimiter
data = "Amit,Rahul,Ramesh"
print(data.split(","))


# 27. join()
friends = ["Amit", "Rahul", "Ramesh"]
result = ", ".join(friends)
print(result)


words = ["Python", "is", "easy"]
print(" ".join(words))


# 28. isalpha()
print("Python".isalpha())         # True
print("Python123".isalpha())      # False


# 29. isdigit()
print("12345".isdigit())          # True
print("123abc".isdigit())         # False


# 30. isdecimal()
print("12345".isdecimal())        # True


# 31. isalnum()
print("Python123".isalnum())      # True
print("Python@123".isalnum())     # False


# 32. isspace()
print("   ".isspace())            # True


# 33. islower()
print("python".islower())         # True


# 34. isupper()
print("PYTHON".isupper())         # True


# 35. istitle()
print("Python Programming".istitle())


# 36. f-Strings
name = "Amit"
age = 30

print(f"My name is {name} and I am {age} years old.")


# 37. Expressions inside f-Strings
a = 10
b = 20

print(f"Sum = {a + b}")


# 38. Number Formatting with f-Strings
price = 1234.5678

print(f"{price:.2f}")


# 39. format() Method
name = "Amit"
age = 30

print("My name is {} and I am {} years old.".format(name, age))


# 40. Old % Formatting
name = "Amit"
age = 30

print("My name is %s and I am %d years old." % (name, age))


# 41. Escape Sequences
print("Hello\nPython")
print("Hello\tPython")
print("He said \"Hello\"")
print("C:\\Users\\Amit")


# 42. Multiline String
message = """
Hello Amit,
Welcome to Python.
Keep Learning!
"""

print(message)


# 43. Raw String
path = r"C:\Users\Amit\Documents"
print(path)

# 44. String Immutability
name = "Python"

# This is NOT allowed:
# name[0] = "J"
# Create a new string instead:
name = "J" + name[1:]

print(name)


# Using replace()
name = "Python"
name = name.replace("P", "J")

print(name)


# 45. Iterate Through String
name = "Python"
for char in name:
    print(char)


# 46. String Comparison
a = "Python"
b = "Python"

print(a == b)                  # True
print("Python" == "python")    # False
print("A" != "B")              # True


# 47. Case-Insensitive Comparison
username = "ADMIN"
if username.casefold() == "admin":
    print("Valid User")


# 48. partition()
email = "amit@gmail.com"

print(email.partition("@"))


# 49. removeprefix()
# Python 3.9+
url = "https://example.com"
print(url.removeprefix("https://"))


# 50. removesuffix()
# Python 3.9+
filename = "report.pdf"
print(filename.removesuffix(".pdf"))

# 51. String to Integer
age = "30"
age = int(age)

print(age)
print(type(age))


# 52. Integer to String
age = 30
age = str(age)

print(age)
print(type(age))


# 53. String to Float
price = "99.50"

price = float(price)

print(price)
print(type(price))

# 54. Unicode
message = "Hello नमस्ते 😊"

print(message)


# 55. ord()
print(ord("A"))

# 56. chr()
print(chr(65))


# 57. Practical Example - Username Validation
username = input("Enter your username: ")
username = username.strip()

if username.isalnum():
    print("Valid username")
else:
    print("Username contains invalid characters")


# 58. Practical Example - Email Validation Basics
email = input("Enter your email: ")
email = email.strip().lower()

if "@" in email and "." in email:
    print("Email format looks valid")
else:
    print("Invalid email format")


# 59. Practical Example - File Extension Check
filename = "report.pdf"

if filename.endswith(".pdf"):
    print("PDF file")
else:
    print("Not a PDF file")



# 60. Practical Example - Count Vowels
text = "Python Programming"

vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
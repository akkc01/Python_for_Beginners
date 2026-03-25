# Printing Output
print("Hello World!, This is AKKC from Bharat")

# Variables & Arithmetic Operations
a=50
b=20
print("The value of a is ",a)
print("The value of b is ",b)
print("The sum of a and b is ",a+b)
print("The difference of a and b is ",a-b)
print("The product of a and b is ",a*b)
print("The quotient of a and b is ",a/b)
print("The floor division of a and b is ",a//b)
print("The modulus of a and b is ",a%b)
print("The exponentiation of a and b is ",a**b)


# = is an assignment operator, it is used to assign a value to a variable
# == is a comparison operator, it is used to compare two values and returns True or False

# Comparison Operators

print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)


# if-elif-else with Logical Operators

c=100
if c>b and c>a:
    print("c is greater than a and b")
elif c>b or c>a:
    print("c is greater than either a or b")
else:
    print("c is not greater than a and b")


#  Indexing

akkc = "AKKC"
print(akkc[0])
print(akkc[1])

# Data Types
print(type(a))
print(type(b))
print(type(akkc))

# Assignment Operators
c+=50
print("The value of c is ",c)
d=c+30
print("The value of d is ",d)
d-=70
e=d
print("The value of e is ",e)

print(500>d>50) # its same as (500>d and d>50)
print(500>d and d>50)



# Logical Operators to know whether it is even or odd
z=99
if z%2==0:
    print("z is even")
else:    
    print("z is odd")



# 
age = 103
if age>=18 and age<=45:
    print("You are a Young Man")
elif age>=60 and age<=100:
    print("You are a Senior Citizen")
elif age<=17:
    print("You are a child or a teenager")
else:    
    print("You are Immortal") 



marks = 99

if marks >= 90:
    print("Grade A+")
elif marks >= 85:
    print("Grade A")
elif marks >= 75:
    print("Grade B+")
elif marks >= 65:
    print("Grade B")
elif marks >= 55:
    print("Grade C+")
elif marks >= 35:
    print("Grade C")
else:
    print("Fail")   





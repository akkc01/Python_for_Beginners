class Person:

    # The __init__() constructor does not need to be called explicitly. It is called automatically when an object is created.
    # self is used inside a class to access the attributes and methods that belong to the current object (instance).
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A method is a function defined inside a class, whereas a regular function is defined outside a class.
    def welcome(self):
        print(f"Welcome {self.name}! This is my first method.")

# Create an object
p1 = Person("Amit", 25)

# Access object attributes
print("Name:", p1.name)
print("Age:", p1.age)

# Call object method
p1.welcome()

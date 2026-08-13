# python file extension = filename.py

print("Hello\nWorld!") # console me output ke liye print() function ka use hota hai

print("Hi Rahul \t How are you?") 
print()

# variables
age = 25 # integer
name = "Rahul" # string
study = "Python" #string
is_student = True # boolean
balance = 411000.50 # float
study_friends = ["Amit", "Rahul", "Maneesh", "Bhawani", "Dinesh"] # list
friends_age = (25, 26, 27, 28, 29) # tuple
friends_data = {"name": "Rahul", "age": 25, "study": "Python"} # dictionary

print(f"Hi, Its our Dictionary: {friends_data}")
print(friends_data["name"])

if "name" in friends_data:
    print("Name exists")

print(friends_data.keys())
print(list(friends_data.keys()))
print(friends_data.values())
print(friends_data.items())
print(len(friends_data))
for key, value in friends_data.items():
    print(f"{key} = {value}")



print("Hi Friends My Name is:", name, "My Age is:",age, "I am learning:", study, "I am a student:", is_student, "My Accountbalance is:", balance)

print(type(age))
print(type(name))
print(type(study))
print(type(is_student))
print(type(balance))
print(type(study_friends))
print(type(friends_age))
print(type(friends_details))
print("My Study Friends are:", study_friends[1],"and", study_friends[3])
print("My Friends Age are:", friends_age[0],"and", friends_age[2])
print("My Friends Details are:", friends_details["name"],"and", friends_details["age"])


# List Operations---
print(f"This is study group friends: {study_friends}")
study_friends.append("Ramesh") # it will append values in list at last
print(f"This is study group friends after adding new friend: {study_friends}")
study_friends.insert(1, "Suresh")
print(f"This is study group friends: {study_friends}")
study_friends.extend(["Ravi", "Mohan"])
print(f"This is study group friends: {study_friends}")
study_friends.remove("Dinesh")
print(f"This is study group friends: {study_friends}")
study_friends.pop(3)
print(f"This is study group friends: {study_friends}")
del study_friends[1]
print(f"This is study group friends: {study_friends}")
study_friends.clear()
print(f"This is study group friends: {study_friends}")


# Dictionary Operations--

friends_data = {
    "name": "Amit",
    "age": 30,
    "city": "Pune"
}

print(f"Hi, It's our Dictionary: {friends_data}")
print(friends_data["name"])
print(friends_data.get("name"))
friends_data["email"] = "amit@example.com"
print(f"Hi, It's our Dictionary: {friends_data}")

friends_data.update({
    "phone": "9876543210",
    "country": "India"
})

print(f"Hi, It's our Dictionary: {friends_data}")

friends_data["age"] = 31 # existing values change
print(f"Hi, It's our Dictionary: {friends_data}")
friends_data.update({"age": 32})
print(f"Hi, It's our Dictionary: {friends_data}")

del friends_data["city"]
print(f"Hi, It's our Dictionary: {friends_data}")
friends_data.pop("email")
print(f"Hi, It's our Dictionary: {friends_data}")

country = friends_data.pop("country")
print(f"Hi removed Country is: {country}")
print(f"Hi, It's our Dictionary: {friends_data}")

friends_data.popitem() # remove last key:value
print(f"Hi, It's our Dictionary: {friends_data}")
friends_data.clear()
print(f"Hi, It's our Dictionary: {friends_data}")


# input() function

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hi my Name is:", name, "My Age is:", age)



name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

print("Hi my Name is:", name, "My Age is:", age)

p,q = input("Enter two numbers: ").split()
print("The two numbers are:", p, "and", q)


a = 10
b = 20
c = a + b

print("The sum of a and b is:", c)


num1 = int(input(" Please Enter first number: "))
num2 = int(input("Please Enter second number: "))
c = num1 + num2

print("The sum of num1 and num2 is:", c)

# Print = output block
# input = terraformt.fvars

# List (list)
# Used to store multiple values. Lists are ordered and mutable.

languages = ["Python", "Java", "Go"]
print(languages)
print(type(languages))
print(languages[0])


# Modifying a List
languages[0] = "C++"
print(languages)


# List is a collection of items which is orederd and cha
list = [10, 20, 30, 35, 45, 65]
print(type(list))
list.append(75)
print(list)
list.insert(2, 25)
print(list)
list.remove(65)
print(list)

study_friends = ["Amit", "Rahul", "Maneesh", "Bhawani", "Dinesh"] # list

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





# 7. Tuple (tuple)
# Used to store multiple values.
# Tuples are ordered and immutable.

coordinates = (10, 20)
colors = ("Red", "Green", "Blue")

print(coordinates)
print(colors)
print(type(coordinates))


# Accessing Tuple Values

print(coordinates[0])
print(coordinates[1])

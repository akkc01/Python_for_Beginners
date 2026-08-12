# 6. List (list)
# Used to store multiple values.
# Lists are ordered and mutable.

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

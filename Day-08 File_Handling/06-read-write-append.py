# # file = open("file", "mode")
# # mode- r, r+, w, w+, a, x, b, t


# # Read
# file = open("rahul.txt", "r")
# content = file.read()
# print(content)
# file.close()


# with open("rahul.txt", "r") as file:  # Jab hub with se file open karte hn to file ko close() karne ki need nhi h, ye apne aap handle karta h.  
#     content = file.read()
#     print(content)


# with open("rahul.txt", "r") as f:
#     bhawani = f.readline()
# print(bhawani)


# with open("rahul.txt", "r") as f:
#     bhawani = f.readlines()
# print(bhawani)


# with open("rahul.txt", "r") as f:
#     bhawani = f.readlines()
# print(bhawani[4])  # Specific line print ke liye



# with open("rahul.txt", "w+") as file:
#     content = file.write("Hello Dosto Kaise ho Aap Log")
# print(content)



# # write
# with open("rahul.txt", "w") as file:
#     file.write("Hello Dosto, Kaise hain Aap Log")



# with open("rahul.txt", "w+") as file:
#     file.write("Hello Dosto, Kaise hain Aap Log")
#     file.seek(0)       # cursor ko file ke start par le jane ke liye, agar curser ko 5 character ke baad le jaana h to 5 likh denge
#     content = file.read()
# print(content)



# # Append
# with open("rahul.txt", "a") as file:
#     file.write("Welcome to the DevOps Junoon.\n")

# # Read
# with open("rahul.txt", "r") as file:
#     content = file.read()
# print(content)



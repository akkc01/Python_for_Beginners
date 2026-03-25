# # For Loops
# # Python have 2 types of loops - for and while loop


# a=int(input("Enter a number: "))
# for i in range(a):
#     print(i)

# print("\n") # This is used to print a new line

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     if i == 6:
#         break
#     print(i)
#     #exit() # This will exit the loop after printing the first number
# print("List has been printed ")

# print("\n")

# for i in range(5):
#   for j in range(3):
#     print(i, j)

# print("\n")


# for i in range(10):
#    print("This is iteration number ",i)
#    itr = input("Do you want to continue? (y/n): ")
#    if itr.lower() == 'n':
#        print("Exiting the loop")
#        break
   
# print("\n")



# # Table Printing
# number = int(input(f"Enter a number to get Table: \n"))
# print(f"Table of - {number} is Below:- \n")
# for i in range(1,11):   # range(start, end, increase/decrease) will generate numbers from 1 to 10 (11 is exclusive)
#     print(number," x ",i," = ",number*i)    


choice = input("Enter Your Choice (press q to quit): ")
while choice!='q':
    number = int(input(f"Enter a number to get Table: \n"))
    print(f"Table of - {number} is Below:- \n")

    for i in range(1,11):   # range(start, end, increase/decrease) will generate numbers from 1 to 10 (11 is exclusive)
        print(number," x ",i," = ",number*i)   
    choice = input("Enter Your Choice (press q to quit): ")

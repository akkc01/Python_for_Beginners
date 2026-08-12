# Today Day 04 
# Logic Building Day

day = str(input(f"Enter the Day of the week : ").lower())   # lower() fun. is used to convert the input into  lowercase
print("Today is", day)

# Logical operators to know whether its office day or Class Day
if day=="saturday" or day=="sunday":
    print("From First Logic. Today I will Attend Class At DevOps Insiders School")
elif day=="monday" or day=="tuesday" or day=="wednesday":
    print("From First Logic. Its Office Day Dude!, Get Ready for Office")
else:
    print("From First Logic, Its WFH Day, Dude! Enjoy your day")



# Logical operator

if day=="sunday":
    print(f"From Second Logic, I will Attend Class At DevOps Insiders.")
elif day=="saturday":
    print(f"From Second Logic, I will Attend Class At DevOps Insiders.")
elif day=="monday":
    print(f"From Second Logic, Its Office Day Dude! .")
elif day=="tuesday":
    print(f"From Second Logic, Its Office Day Dude!.")
elif day=="wednesday":
    print(f"From Second Logic, Its Office Day Dude! .")
elif day=="thursday":
    print(f"From Second Logic, Its WFH Day, Revise the Azure Concepts and AWS Concepts.")
else:
    print(f"From Second Logic, Its Day to Revise the Terraform Concepts and Practice")



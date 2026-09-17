# This code is for printing the multiplication table of a num entered by user.
# it will keep asking user to enter a num until user press q to quit loop.


usr_choice= input("Enter anything to continue (press q to quit): ")
while usr_choice!='q':
    num = int(input(f"Enter a num to get Table: \n"))
    print(f"Table of - {num} is Below:- \n")

    for i in range(1,11):   # range(start, end, increase/decrease) will generate numbers from 1 to 10 (11 is exclusive)
        print(num," x ",i," = ",num*i)   
    usr_choice= input("Enter anything to continue (press q to quit): ")



# Now Optimized code with lower() function to handle both uppercase and lowercase inputs forquitting the loop.
# user can enter 'q' or 'n' in any case(upper or lower) to quit the loop.
usr_choice= input("Enter anything to continue (press q or n to quit): ")
while usr_choice.lower() != 'q' and usr_choice.lower() != 'n':
    num = int(input(f"Enter a num to get Table: \n"))
    print(f"Table of - {num} is Below:- \n")

    for i in range(1,11):   # range(start, end, increase/decrease) will generate numbers from 1 to 10 (11 is exclusive)
        print(num," x ",i," = ",num*i)   
    usr_choice= input("Enter anything to continue (press q or n to quit): ")

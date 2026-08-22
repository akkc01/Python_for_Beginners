# append using "a" mode
# Python doesn't have a separate append() file method. We use "a" mode to append data.

# Single line append
file = open("readme.txt", "a")  # Open the file in append mode ("a")
file.write("Hello Python\n")  # Add new content at the end of the file
file.close()
# Existing content delete nahi hota.


# Multiple lines append
file = open("readme.txt", "a")  # Open the file in append mode ("a")
file.write("Python\n")  # Add Python at the end
file.write("Docker\n")  # Add Docker at the end
file.write("Kubernetes\n")  # Add Kubernetes at the end
file.close()


# Append using writelines()
file = open("readme.txt", "a")  # Open the file in append mode ("a")
lines = ["Azure\n", "Terraform\n", "Ansible\n"]  # Create multiple lines
file.writelines(lines)  # Append all strings at the end of the file
file.close()


# Append user input
file = open("readme.txt", "a")  # Open the file in append mode ("a")
name = input("Enter your name: ")  # Take input from the user
file.write(name + "\n")  # Append the user's name at the end of the file
file.close()


# Append multiple user inputs
file = open("readme.txt", "a")  # Open the file in append mode ("a")
for i in range(3):  # Run the loop 3 times
    name = input("Enter your name: ")  # Take name from the user
    file.write(name + "\n")  # Append the name at the end of the file
file.close()


# Append with timestamp/log
file = open("application.log", "a")  # Open the log file in append mode
file.write("Application started\n")  # Append a new log message
file.write("Deployment completed\n")  # Append another log message
file.write("Application stopped\n")  # Append another log message
file.close()


# Append using with open() — Recommended
with open("readme.txt", "a") as file:  # Open the file in append mode
    file.write("New content added\n")  # Append new content at the end
# File automatically closes here]



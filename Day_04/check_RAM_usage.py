import psutil       
# use pip3 install psutil to install the library

RAM_usage = psutil.virtual_memory().percent
print(f"Current RAM usage: {RAM_usage}% \n")


def ram_usage_threshold():
    threshold = int(input("Enter the RAM usage threshold percentage: "))
    if RAM_usage > threshold:
        print(f"Warning: RAM usage is above the threshold! Current usage: {RAM_usage}%, Now Email is Sending...")
    else:
        print(f"RAM usage is within the threshold and is acceptable. Current usage: {RAM_usage}%")


ram_usage_threshold()
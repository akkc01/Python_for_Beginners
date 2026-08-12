import psutil       
# use pip3 install psutil to install the library

RAM_usage = psutil.virtual_memory().percent
# total = psutil.virtual_memory().total
print(f"Current RAM usage: {RAM_usage}% \n")
# print(f"Total RAM: {total} bytes")

# memory = psutil.virtual_memory()
# total = memory.total
# available = memory.available
# used = memory.used
# percent = memory.percent

# print("Total RAM:", total)
# print("Available RAM:", available)
# print("Used RAM:", used)
# print("RAM Usage:", percent, "%")


import psutil

memory = psutil.virtual_memory()

total = memory.total / (1024 ** 3)
available = memory.available / (1024 ** 3)
used = memory.used / (1024 ** 3)

print(f"Total RAM     : {total:.2f} GB")
print(f"Available RAM : {available:.2f} GB")
print(f"Used RAM      : {used:.2f} GB")
print(f"RAM Usage     : {memory.percent}%")

# def ram_usage_threshold():
#     threshold = int(input("Enter the RAM usage threshold percentage: "))
#     if RAM_usage > threshold:
#         print(f"Warning: RAM usage is above the threshold! Current usage: {RAM_usage}%, Now Email is Sending...")
#     else:
#         print(f"RAM usage is within the threshold and is acceptable. Current usage: {RAM_usage}%")


# ram_usage_threshold()



print("\n\n")
# disk = psutil.disk_usage("/")

# total = disk.total / (1024 ** 3)
# used = disk.used / (1024 ** 3)
# free = disk.free / (1024 ** 3)

# print(f"Total Disk : {total:.2f} GB")
# print(f"Used Disk  : {used:.2f} GB")
# print(f"Free Disk  : {free:.2f} GB")
# print(f"Disk Usage : {disk.percent}%")



disk = psutil.disk_usage("/")

print("Raw disk object:")
print(disk)

print("\nBytes:")
print("Total:", disk.total)
print("Used :", disk.used)
print("Free :", disk.free)
print("Percent:", disk.percent)

print("\nGB:")
print(f"Total: {disk.total / (1024 ** 3):.2f} GB")
print(f"Used : {disk.used / (1024 ** 3):.2f} GB")
print(f"Free : {disk.free / (1024 ** 3):.2f} GB")
print(f"Used %: {(disk.used / disk.total) * 100:.2f}%")


print("\n\n")


disk = psutil.disk_usage("/")

print(disk)
print()
print("Total :", disk.total / (1024 ** 3), "GB")
print("Used  :", disk.used / (1024 ** 3), "GB")
print("Free  :", disk.free / (1024 ** 3), "GB")
print("Usage :", disk.percent, "%")
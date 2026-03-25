import psutil       
# use pip3 install psutil to install the library

cpu_usage = psutil.cpu_percent(interval=1)
print(f"Current CPU usage: {cpu_usage}% \n")


def cpu_usage_threshold():
    threshold = int(input("Enter the CPU usage threshold percentage: "))
    if cpu_usage > threshold:
        print(f"Warning: CPU usage is above the threshold! Current usage: {cpu_usage}%, Now Email is Sending...")
    else:
        print(f"CPU usage is within the threshold and is acceptable. Current usage: {cpu_usage}%")


cpu_usage_threshold()

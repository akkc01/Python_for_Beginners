import psutil

print(psutil.cpu_percent())

# print with an interval
print(psutil.cpu_percent(interval=1))

# Returns the number of CPUs/logical processors.
print(psutil.cpu_count())

#get physical cores
print(psutil.cpu_count(logical=False))


# Returns CPU time statistics.
print(psutil.cpu_times())

# Returns CPU frequency information.
print(psutil.cpu_freq())

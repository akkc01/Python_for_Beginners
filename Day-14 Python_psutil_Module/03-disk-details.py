import psutil

# Returns disk usage for a particular path.
disk = psutil.disk_usage("/")
print(disk)

print("Total:", disk.total)
print("Used:", disk.used)
print("Free:", disk.free)
print("Usage:", disk.percent)


# Returns information about mounted disks/partitions.
partitions = psutil.disk_partitions()
for partition in partitions:
    print(partition)

for partition in psutil.disk_partitions():
    print("Device:", partition.device)
    print("Mount:", partition.mountpoint)
    print("Filesystem:", partition.fstype)


# Returns disk I/O statistics.
io = psutil.disk_io_counters()
print(io)



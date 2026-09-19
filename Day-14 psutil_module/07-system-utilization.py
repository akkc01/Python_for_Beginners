import psutil

print("CPU Usage:", psutil.cpu_percent(), "%")

memory = psutil.virtual_memory()
print("Memory Usage:", memory.percent, "%")

disk = psutil.disk_usage("/")
print("Disk Usage:", disk.percent, "%")

network = psutil.net_io_counters()
print("Network Sent:", network.bytes_sent)
print("Network Received:", network.bytes_recv)

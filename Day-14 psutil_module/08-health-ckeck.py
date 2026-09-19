import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

print("CPU:", cpu, "%")
print("Memory:", memory, "%")
print("Disk:", disk, "%")

if cpu > 80:
    print("WARNING: High CPU usage")
if memory > 80:
    print("WARNING: High memory usage")
if disk > 80:
    print("WARNING: Low disk space")

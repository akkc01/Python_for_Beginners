import psutil

# Returns a list of currently running process IDs (PIDs).
print(psutil.pids())


# Represents a particular process.
process = psutil.Process(123)


# Returns the process name.
process = psutil.Process(123)
print(process.name())


# Returns the executable path.
print(process.exe())


# Returns the command-line arguments used to start the process.
print(process.cmdline())


# Returns the process status.
print(process.status())


# Returns CPU usage of a specific process.
process = psutil.Process(123)
print(process.cpu_percent())


# Returns memory usage of a process.
process = psutil.Process(123)
memory = process.memory_info()


# Returns the number of threads used by a process.
print(process.num_threads())


# Returns the process creation time as a Unix timestamp.
print(process.create_time())


# Instead of manually getting PIDs and creating Process objects, you can iterate through running processes.
for process in psutil.process_iter():
    print(process.pid, process.name())


# You can request multiple attributes:
for process in psutil.process_iter(
    ["pid", "name", "username"]
):
    print(process.info)



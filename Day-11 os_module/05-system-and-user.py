import os

# SYSTEM / COMMANDS

# Executes an operating system command.
os.system("ls")


# Returns the Process ID (PID) of the current Python process.
print(os.getpid())


# Returns the Parent Process ID (PPID).
print(os.getppid())


# Returns the number of logical CPUs.
print(os.cpu_count())


# Returns the operating system family.
# "posix" on macOS/Linux and "nt" on Windows.
print(os.name)


# Returns detailed system information on Unix-like systems.
print(os.uname())


# Returns the operating system name.
print(os.uname().sysname)


# Returns the machine architecture.
print(os.uname().machine)



# USER INFORMATION

# Returns the current login username when supported.
print(os.getlogin())


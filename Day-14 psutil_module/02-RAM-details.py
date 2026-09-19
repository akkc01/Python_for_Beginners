import psutil

# Returns information about RAM/memory.
memory = psutil.virtual_memory()
print(memory)


print(memory.total)
print(memory.available)
print(memory.percent)
print(memory.used)
print(memory.free)



memory = psutil.virtual_memory()
print("Total:", memory.total)
print("Available:", memory.available)
print("Used:", memory.used)
print("Free:", memory.free)
print("Usage:", memory.percent)

# Returns information about swap memory.
swap = psutil.swap_memory()
print(swap)


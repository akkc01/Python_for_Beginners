import subprocess


# result = subprocess.run(["ls", "-l"],capture_output=True,text=True)
result = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)

print(result.stdout)

# stdout
result1 = subprocess.run(
    ["echo", "Hello this is from Sub-Process"],
    capture_output=True,
    text=True
)
print(result1.stdout)


#stderr
import subprocess
result = subprocess.run(
    ["ls", "/does-not-exist"],
    capture_output=True,
    text=True
)
print("STDOUT:")
print(result.stdout)
print("STDERR:")
print(result.stderr)

import subprocess
result = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)

print("Exit Code:", result.returncode)
print("Output:")
print(result.stdout)
print("Error:")
print(result.stderr,"\n")




import subprocess
try:
    subprocess.run(
        ["ls", "/invalid/path"],
        check=True
    )
except subprocess.CalledProcessError as e:
    print("Command failed")
    print(e.returncode,"\n")




import subprocess
try:
    subprocess.run(
        ["sleep", "10"],
        timeout=3
    )
except subprocess.TimeoutExpired:
    print("Command timed out")

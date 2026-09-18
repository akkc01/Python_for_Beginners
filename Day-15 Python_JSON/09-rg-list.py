import subprocess
import json

result = subprocess.run(
    ["az", "group", "list", "--output", "json"],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("Azure CLI failed")
    print(result.stderr)
    exit(1)

resource_groups = json.loads(result.stdout)

for rg in resource_groups:
    print(
        f"Name: {rg['name']} | "
        f"Location: {rg['location']}"
    )
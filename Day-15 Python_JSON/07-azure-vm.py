import subprocess
import json

result = subprocess.run(
    ["az", "vm", "list", "--output", "json"],
    capture_output=True,
    text=True
)

vms = json.loads(result.stdout)

for vm in vms:
    print(vm["name"])



#import subprocess
import json

result = subprocess.run(
    ["az", "vm", "list", "--output", "json"],
    capture_output=True,
    text=True
)

vms = json.loads(result.stdout)

for vm in vms:
    print(
        f"Name: {vm['name']}"
    )
    print(
        f"Resource Group: {vm['resourceGroup']}"
    )
    print(
        f"Location: {vm['location']}"
    )
    print("-" * 40)
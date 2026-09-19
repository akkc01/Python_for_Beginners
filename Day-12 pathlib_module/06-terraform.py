from pathlib import Path
import subprocess

terraform_dir = Path("terraform")
if not terraform_dir.exists():
    raise FileNotFoundError(
        "Terraform directory does not exist"
    )
result = subprocess.run(
    ["terraform", "validate"],
    cwd=terraform_dir,
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("Terraform validation failed")
    print(result.stderr)
else:
    print("Terraform validation passed")
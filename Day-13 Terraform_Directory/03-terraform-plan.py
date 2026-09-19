from pathlib import Path
import os
import subprocess

# pathlib → filesystem paths
terraform_dir = Path("terraform")

plan_file = terraform_dir / "tfplan"

# os → environment variables
environment = os.getenv("ENVIRONMENT", "dev")

# subprocess → Terraform
subprocess.run(
    ["terraform", "plan", "-out", str(plan_file)],
    cwd=terraform_dir,
    check=True
)

print(f"Planning infrastructure for {environment}")
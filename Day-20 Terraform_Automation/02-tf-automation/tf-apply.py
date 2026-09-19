from terraform_utils.terraform import Terraform
from pathlib import Path


# Get the directory where this Python script exists
project_root = Path(__file__).parent

# Terraform working directory
workdir = (
    project_root
    / "projects"
    / "axion-app"
    / "environment"
    / "dev"
)
terraform = Terraform(working_dir=workdir)


terraform.fmt()
terraform.init()
terraform.validate()
terraform.plan()
terraform.apply()

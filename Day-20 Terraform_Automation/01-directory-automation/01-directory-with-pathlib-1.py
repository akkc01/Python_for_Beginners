from pathlib import Path

# cd /Users/amitkumar/Documents/Study-Akkc/Python/Day-20 Terraform_Automation/02-command-automation/projects    , then run this file.

# Root Project Directory
root = Path("E-Learning-app")

# Environment Directory Structure
parent = root / "environment"

environments = [
    "dev",
    "qa",
    "prod"
]

terraform_files = [
    "main.tf",
    "variables.tf",
    "backend.tf",
    "terraform.tfvars",
    "output.tf",
    "providers.tf"
]


# Create root directory
try:
    root.mkdir()

    print(f"Root folder '{root}' created")

except FileExistsError:
    print(f"Root folder '{root}' already exists")


# Create Environment directory
try:
    parent.mkdir()

    print(f"Environment folder '{parent}' created")

except FileExistsError:
    print(f"Environment folder '{parent}' already exists")


# Create dev / qa / prod directories
for env in environments:

    env_path = parent / env

    try:
        env_path.mkdir()

        print(f"Folder '{env_path}' created")

    except FileExistsError:
        print(f"Folder '{env_path}' already exists")


    # Create Terraform files
    for file in terraform_files:

        file_path = env_path / file

        try:
            file_path.touch(exist_ok=False)

            print(f"File '{file_path}' created")

        except FileExistsError:
            print(f"File '{file_path}' already exists")


print("\nTerraform Environment structure completed!")



# Terraform Module Directory Structure

child_module = root / "modules"

modules = [
    "Resource-Group",
    "VNET",
    "SUBNET",
    "AKS",
    "ACR"
]

module_files = [
    "main.tf",
    "variables.tf"
]


# Create modules directory
try:
    child_module.mkdir()

    print(f"\nModules folder '{child_module}' created")

except FileExistsError:
    print(f"\nModules folder '{child_module}' already exists")


# Create module directories
for module in modules:

    module_path = child_module / module

    try:
        module_path.mkdir()

        print(f"Folder '{module_path}' created")

    except FileExistsError:
        print(f"Folder '{module_path}' already exists")


    # Create module Terraform files
    for file in module_files:

        file_path = module_path / file

        try:
            file_path.touch(exist_ok=False)

            print(f"File '{file_path}' created")

        except FileExistsError:
            print(f"File '{file_path}' already exists")


print("\nTerraform Module structure completed!")

print("\nAll Terraform directory structures are ready!")
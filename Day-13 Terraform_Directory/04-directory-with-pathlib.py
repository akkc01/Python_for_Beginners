from pathlib import Path

# Parent directory
parent = Path("Environment")

# Child directories
environments = ["dev", "qa", "prod"]

# Terraform files
terraform_files = [
    "main.tf",
    "variables.tf",
    "backend.tf",
    "terraform.tfvars",
    "output.tf",
    "providers.tf"
]


# Create parent directory
try:
    parent.mkdir()

    print(f"Parent folder '{parent}' created")

except FileExistsError:
    print(f"Folder '{parent}' already exists")


# Create child directories and files
for env in environments:

    # Create dev / qa / prod path
    env_path = parent / env

    # Create environment directory
    try:
        env_path.mkdir()

        print(f"Folder '{env}' created")

    except FileExistsError:
        print(f"Folder '{env}' already exists")


    # Create Terraform files
    for file in terraform_files:

        file_path = env_path / file

        try:
            # touch() creates a new empty file
            file_path.touch(exist_ok=False)

            print(f"File '{file}' created")

        except FileExistsError:
            print(f"File '{file}' already exists")


print("Terraform Directory structure process completed!")



# Terraform Module Directory Structure
child_module = Path("modules")

# Child directories
modules = [
    "Resource-Group",
    "VNET",
    "SUBNET"
]

# Terraform files
module_files = [
    "main.tf",
    "variables.tf"
]


# Create parent directory
try:
    child_module.mkdir()

    print(f"Folder '{child_module}' created")

except FileExistsError:
    print(f"Folder '{child_module}' already exists")


# Create child directories and files
for module in modules:

    # Create module path
    module_path = child_module / module

    # Create module directory
    try:
        module_path.mkdir()

        print(f"Folder '{module}' created")

    except FileExistsError:
        print(f"Folder '{module}' already exists")


    # Create Terraform files
    for file in module_files:

        file_path = module_path / file

        try:
            # exist_ok=False means:
            # create the file only if it doesn't already exist
            file_path.touch(exist_ok=False)

            print(f"File '{file}' created")

        except FileExistsError:
            print(f"File '{file}' already exists")


print("Terraform module structure process completed!")
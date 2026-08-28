import os

# Parent directory
parent = "environment-error"

# Child directories
environments = ["dev", "qa", "prod"]

# Terraform files
files = [
    "main.tf",
    "variables.tf",
    "backend.tf",
    "terraform.tfvars",
    "output.tf",
    "providers.tf"
]


# Create parent directory
try:
    os.makedirs(parent)
    print(f"Parent folder '{parent}' created")

except FileExistsError:
    print(f"Folder '{parent}' already exists")


# Create child directories and files
for env in environments:

    env_path = os.path.join(parent, env)

    # Create dev / qa / prod
    try:
        os.makedirs(env_path)
        print(f"Folder '{env}' created")

    except FileExistsError:
        print(f"Folder '{env}' already exists")


    # Create Terraform files
    for file in files:

        file_path = os.path.join(env_path, file)

        try:
            # "x" means create a new file
            with open(file_path, "x") as f:
                pass

            print(f"File '{file}' created")

        except FileExistsError:
            print(f"File '{file}' already exists")


print("Terraform Directory structure process completed!")


# Child Modules Directory Structures----------------------------------
child_module = "modules-with-error"

# Child directories
modules = ["Resource-Group", "VNET", "SUBNET"]

# Terraform files
files = [
    "main.tf",
    "variables.tf",
]


# Create parent directory
try:
    os.makedirs(child_module)
    print(f"Folder '{child_module}' created")

except FileExistsError:
    print(f"Folder '{child_module}' already exists")


# Create child directories and files
for module in modules:

    module_path = os.path.join(child_module, module)

    # Create module folder
    try:
        os.makedirs(module_path)
        print(f"Folder '{module}' created")

    except FileExistsError:
        print(f"Folder '{module}' already exists")


    # Create Terraform files
    for file in files:

        file_path = os.path.join(module_path, file)

        try:
            # "x" = create new file, don't overwrite existing file
            with open(file_path, "x") as f:
                pass

            print(f"File '{file}' created")

        except FileExistsError:
            print(f"File '{file}' already exists")


print("Terraform module structure process completed!")
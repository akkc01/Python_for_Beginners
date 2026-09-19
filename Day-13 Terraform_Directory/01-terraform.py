import os

# Parent directory
parent = "environment"

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
os.makedirs(parent)

# Create child directories and files
for env in environments:

    env_path = os.path.join(parent, env)

    # Create dev / qa / prod
    os.makedirs(env_path)

    # Create Terraform files
    for file in files:
        file_path = os.path.join(env_path, file)

        with open(file_path, "w") as f:
            pass

print("Terraform Directory structure created successfully!")



# Parent directory
child_module = "modules"

# Child directories
modules = ["Resource-Group", "VNET", "SUBNET"]

# Terraform files
files = [
    "main.tf",
    "variables.tf",
]


os.makedirs(child_module)

# Create child directories and files
for module in modules:

    module_path = os.path.join(child_module, module)

    # Create dev / qa / prod
    os.makedirs(module_path)

    # Create Terraform files
    for file in files:
        file_path = os.path.join(module_path, file)

        with open(file_path, "w") as f:
            pass

print("Terraform module structure created successfully!")




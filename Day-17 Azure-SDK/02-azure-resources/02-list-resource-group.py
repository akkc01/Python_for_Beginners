from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient

credential = DefaultAzureCredential()

client = ResourceManagementClient(
    credential=credential,
    subscription_id="1bfd01bb-a3e6-4aee-a2ec-5901c46baccc"
)

# Returns all resource groups in the subscription.
resource_groups = client.resource_groups.list()

for resource_group in resource_groups:
    print(resource_group.name)
    print("-------------------------------------------------------------\n")


print("***********************************************************************************************\n")

# Gets information about a specific resource group.
resource_group = client.resource_groups.get(
    "aks-rg"
)
print(resource_group)

# You can access properties:
print(resource_group.name)
print(resource_group.location)
print(resource_group.tags)


print("***********************************************************************************************\n")
# # Check if a Resource Group Exists
# # A simple approach is to call `get()` and handle the error:

from azure.core.exceptions import ResourceNotFoundError

try:
    # Attempts to get the resource group.
    resource_group = client.resource_groups.get("aks-rg")
    print("Resource Group exists")

except ResourceNotFoundError:
    print("Resource Group does not exist")

print("***********************************************************************************************\n")


# Creates a resource group in the specified Azure region.
resource_group = client.resource_groups.create_or_update(
    "python-rg",
    {
        "location": "eastus"
    }
)

print(f"Resource Group Created by Python Script: {resource_group.name}")
print(f"Location is: {resource_group.location}")

print("***********************************************************************************************\n")


# Creates or updates a resource group with tags.
resource_group = client.resource_groups.create_or_update(
    "python-rg",
    {
        "location": "eastus",
        "tags": {
            "environment": "development",
            "owner": "devops",
            "project": "axion"
        }
    }
)

print(f"Resource Group Need to Tag update is: {resource_group.name}")
print(f"Updated tags are: {resource_group.tags}")
print("***********************************************************************************************\n")


# Updates the tags of an existing resource group.
resource_group = client.resource_groups.update(
    "python-rg",
    {
        "tags": {
            "environment": "production",
            "owner": "devops",
            "project": "jarvis"
        }
    }
)
print(f"Resource Group: {resource_group.name} and Updated tags are: {resource_group.tags}")
print("***********************************************************************************************\n")



# # Deletes the resource group.
# poller = client.resource_groups.begin_delete(
#     "python-rg"
# )
# # Waits until the deletion operation completes.
# poller.result()

# print("Resource Group deleted")




# 12. List Resources in a Resource Group
# The `resources` collection can be used to list resources.

# Lists resources inside a specific resource group.
resources = client.resources.list_by_resource_group(
    "aks-test-rg"
)
for resource in resources:
    print(resource.name)
    print(resource.type)
    print(resource.location)
    print("--------------------------------------------")

print("***********************************************************************************************\n")


# Gets the properties of a resource group.
resource_group = client.resource_groups.get(
    "aks-test-rg"
)
print("Name:", resource_group.name)
print("Location:", resource_group.location)
print("Tags:", resource_group.tags)

print("***********************************************************************************************\n")


# Lists all resources in the subscription.
resources = client.resources.list()

for resource in resources:
    print("Name:", resource.name)
    print("Type:", resource.type)
    print("Location:", resource.location)

    # Extracts Resource Group name from the resource ID.
    resource_group = resource.id.split("/")[4]
    print("Resource Group:", resource_group)
    print("Resource ID:", resource.id)
    print("Tags:", resource.tags)
    print("--------------------------------------------")
    
print("***********************************************************************************************\n")
#This is useful when you want to discover resources across the entire subscription.



# Returns True if the resource group exists.
exists = client.resource_groups.check_existence(
    "python-rg"
)
print(exists)
print("***********************************************************************************************\n")


# Lists all resource groups.
resource_groups = client.resource_groups.list()

# Prints resource group information.
for resource_group in resource_groups:
    print("Name:", resource_group.name)
    print("Location:", resource_group.location)
    print("Tags:", resource_group.tags)
    print("-------------------------")

print("***********************************************************************************************\n")


from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient

# Creates the authentication credential.
credential = DefaultAzureCredential()

# Creates the Resource Management client.
client = ResourceManagementClient(
    credential=credential,
    subscription_id="1bfd01bb-a3e6-4aee-a2ec-5901c46baccc"
)

# Lists all resources in the subscription.
resources = client.resources.list()


for resource in resources:

    resource_group = resource.id.split("/")[4]

    print(
        f"Name: {resource.name} | "
        f"Type: {resource.type} | "
        f"Location: {resource.location} | "
        f"Resource Group: {resource_group} | "
        f"Resource ID: {resource.id} | "
        f"Tags: {resource.tags}"
    )
    print("------------------------------------------------------------------------------")


# for resource in resources:
#     print("Name:", resource.name)
#     print("Type:", resource.type)
#     print("Location:", resource.location)

#     # Extracts Resource Group name from the resource ID.
#     resource_group = resource.id.split("/")[4]
#     print("Resource Group:", resource_group)
#     print("Resource ID:", resource.id)
#     print("Tags:", resource.tags)
#     print("------------------------------------------------------------------------------")
# #This is useful when you want to discover resources across the entire subscription.



# # Gets a specific Azure resource.
# resource = client.resources.get(
#     "dev-rg",
#     "Microsoft.Storage",
#     "storageAccounts",
#     "axionstorage"
# )

# print(resource)

# # Gets the resource ID.
# print(resource.id)

# # Returns the Azure resource type.
# print(resource.type)

# # Returns the Azure region where the resource exists.
# print(resource.location)

# # Returns tags attached to the resource.
# print(resource.tags)




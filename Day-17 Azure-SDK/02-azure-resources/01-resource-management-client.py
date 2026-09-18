from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient

# Creates the Azure authentication credential.
credential = DefaultAzureCredential()

# Creates the Resource Management client.
client = ResourceManagementClient(
    credential=credential,
    subscription_id="1bfd01bb-a3e6-4aee-a2ec-5901c46baccc"
)

print(client)

# This is the main client used to interact with Azure Resource Manager. 
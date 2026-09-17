# pip install azure-mgmt-storage azure-identity

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

# Creates the Azure authentication credential.
credential = DefaultAzureCredential()

# Creates the Storage Management client.
client = StorageManagementClient(
    credential=credential,
    subscription_id="1bfd01bb-a3e6-4aee-a2ec-5901c46baccc"
)

# Lists all Storage Accounts in the subscription.
storage_accounts = client.storage_accounts.list()

for storage in storage_accounts:
    # Prints the Storage Account name.
    print("Name:", storage.name)
    # Prints the Azure region.
    print("Location:", storage.location)
    # Prints the Storage Account resource ID.
    print("Resource ID:", storage.id)
    print("---------------------------------------")
# First login through Azure CLI: az login

# Then use:
from azure.identity import AzureCliCredential

# Creates a credential that uses the Azure CLI authentication.
credential = AzureCliCredential()

# Requests an access token to verify authentication.
token = credential.get_token(
    "https://management.azure.com/.default"
)

print("Authentication successful!")
print(token)
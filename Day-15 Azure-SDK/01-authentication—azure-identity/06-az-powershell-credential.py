
# AzurePowerShellCredential authenticates your Python application using the Azure PowerShell authentication context.

# Python:

from azure.identity import AzurePowerShellCredential

# Creates a credential using Azure PowerShell authentication.
credential = AzurePowerShellCredential()

# Requests an access token to verify authentication.
token = credential.get_token(
    "https://management.azure.com/.default"
)

print("Authentication successful!")
print(token)
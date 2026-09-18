
# AzureDeveloperCliCredential authenticates your Python application using the Azure Developer CLI (azd) authentication.

# First login: azd auth login

# Then Python:
from azure.identity import AzureDeveloperCliCredential

# Creates a credential using Azure Developer CLI authentication.
credential = AzureDeveloperCliCredential()

# Requests an access token to verify authentication.
token = credential.get_token(
    "https://management.azure.com/.default"
)

print("Authentication successful!")
print(token)
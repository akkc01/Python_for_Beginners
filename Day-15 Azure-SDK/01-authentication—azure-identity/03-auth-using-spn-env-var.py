

from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()

# Expoert this to your Local PC-
# export AZURE_TENANT_ID="your-tenant-id"
# export AZURE_CLIENT_ID="your-client-id"
# export AZURE_CLIENT_SECRET="your-client-secret"


try:
    token = credential.get_token(
        "https://management.azure.com/.default"
    )

    print("Authentication successful!")

except Exception as e:
    print("Authentication failed!")
    print(e)
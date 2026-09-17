from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()

try:
    token = credential.get_token(
        "https://management.azure.com/.default"
    )

    print("Authentication successful!")
    print("Token expires at:", token.expires_on)

except Exception as e:
    print("Authentication failed!")
    print(e)

    
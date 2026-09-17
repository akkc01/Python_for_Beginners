from azure.identity import ManagedIdentityCredential

# Uses the system-assigned Managed Identity
# of the Azure resource where this code is running.
credential = ManagedIdentityCredential()

try:

    # Requests an access token for Azure Resource Manager.
    token = credential.get_token(
        "https://management.azure.com/.default"
    )

    print("Authentication successful!")
    print("Token expires at:", token.expires_on)

except Exception as e:

    print("Authentication failed!")
    print(e)




# User-Assigned Managed Identity-----------

from azure.identity import ManagedIdentityCredential

# Uses a specific User-Assigned Managed Identity
# by providing its Client ID.
credential = ManagedIdentityCredential(
    client_id="YOUR_MANAGED_IDENTITY_CLIENT_ID"
)

try:

    # Requests an access token for Azure Resource Manager.
    token = credential.get_token(
        "https://management.azure.com/.default"
    )

    print("Authentication successful!")
    print("Token expires at:", token.expires_on)

except Exception as e:

    print("Authentication failed!")
    print(e)



# # 4. System-Assigned vs User-Assigned

# |                                  | System-Assigned               | User-Assigned                                |
# | -------------------------------- | ----------------------------- | -------------------------------------------- |
# | Identity lifecycle               | Tied to Azure resource        | Independent Azure resource                   |
# | Client ID                        | Automatically generated       | You have a specific Client ID                |
# | Can attach to multiple resources | Generally no                  | Yes                                          |
# | Deleted with resource            | Yes                           | No                                           |
# | Python                           | `ManagedIdentityCredential()` | `ManagedIdentityCredential(client_id="...")` |
# | Secret required                  | No                            | No                                           |

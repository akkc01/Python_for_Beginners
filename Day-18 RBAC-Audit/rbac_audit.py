from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.subscription import SubscriptionClient

credential = DefaultAzureCredential()

subscription_client = SubscriptionClient(credential)

for sub in subscription_client.subscriptions.list():

    subscription_id = sub.subscription_id
    subscription_name = sub.display_name

    print(f"\nSubscription: {subscription_name}")
    print(f"ID: {subscription_id}")

    auth_client = AuthorizationManagementClient(
        credential,
        subscription_id
    )

    assignments = auth_client.role_assignments.list_for_scope(
        f"/subscriptions/{subscription_id}"
    )

    for assignment in assignments:

        print(
            assignment.principal_id,
            assignment.role_definition_id,
            assignment.scope
        )


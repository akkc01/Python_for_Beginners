from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient


class AzureValidator:

    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.credential = (
            DefaultAzureCredential()
        )

        self.resource_client = (
            ResourceManagementClient(
                self.credential,
                self.subscription_id
            )
        )

    # ========================================================
    # Resource Group Validation
    # ========================================================

    def check_resource_group(
        self,
        resource_group
    ):

        try:

            result = (
                self.resource_client
                .resource_groups
                .get(resource_group)
            )

            print(
                f"PASS: Resource group exists: "
                f"{result.name}"
            )

            return True

        except Exception as error:

            print(
                f"FAIL: Resource group not found: "
                f"{resource_group}"
            )

            print(error)

            return False
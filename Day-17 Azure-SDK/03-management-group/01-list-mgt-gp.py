
from azure.identity import DefaultAzureCredential
from azure.mgmt.managementgroups import ManagementGroupsAPI

credential = DefaultAzureCredential()
client = ManagementGroupsAPI(
    credential
)

for group in client.management_groups.list():
    print(group.name)

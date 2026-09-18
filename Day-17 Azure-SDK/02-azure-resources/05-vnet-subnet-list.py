from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

credential = DefaultAzureCredential()

client = NetworkManagementClient(
    credential=credential,
    subscription_id="1bfd01bb-a3e6-4aee-a2ec-5901c46baccc"
)

# Returns all Virtual Networks in the subscription.
vnets = client.virtual_networks.list_all()

for vnet in vnets:

    print("VNet Name:", vnet.name)
    print("Resource Group:", vnet.id.split("/")[4])
    print("Location:", vnet.location)
    print("Subnets:")

    # Returns the subnets configured inside this VNet.
    for subnet in vnet.subnets:

        print(
            f"  Name: {subnet.name} | "
            f"Address Prefix: {subnet.address_prefix} | "
            #f"Subnet ID: {subnet.id}"
        )

    print("------------------------------------------------------------------------------")
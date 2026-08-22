# pip install azure-identity azure-mgmt-compute

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient


# Azure subscription ID
subscription_id = "dsf-dgvfdgdf-fhd34-fgre5t-fgdh43"


# Create Azure credential
credential = DefaultAzureCredential()


# Create Compute Management Client
compute_client = ComputeManagementClient(
    credential=credential,
    subscription_id=subscription_id
)


# Get all VMs from the subscription
vms = compute_client.virtual_machines.list_all()


# Print VM details
for vm in vms:

    print(f"VM Name       : {vm.name}")
    print(f"Resource ID   : {vm.id}")
    print(f"Location      : {vm.location}")
    print(f"VM Size       : {vm.hardware_profile.vm_size}")
    print("-" * 50)

from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.subscription import SubscriptionClient
import csv
from datetime import datetime


# --------------------------------------------------
# Configuration
# --------------------------------------------------

OUTPUT_FILE = "azure_rbac_report_principle-id.csv"

# Roles that we consider privileged for this audit
PRIVILEGED_ROLES = {
    "Owner",
    "User Access Administrator",
    "Contributor"
}


# --------------------------------------------------
# Azure Authentication
# --------------------------------------------------

print("[+] Authenticating to Azure...")

credential = DefaultAzureCredential()

subscription_client = SubscriptionClient(credential)


# --------------------------------------------------
# CSV File
# --------------------------------------------------

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow([
        "Subscription Name",
        "Subscription ID",
        "Principal ID",
        "Role",
        "Scope",
        "Privileged",
        "Generated At"
    ])


    # --------------------------------------------------
    # Get all subscriptions
    # --------------------------------------------------

    for subscription in subscription_client.subscriptions.list():

        subscription_id = subscription.subscription_id
        subscription_name = subscription.display_name

        print()
        print("=" * 70)
        print(f"Subscription: {subscription_name}")
        print(f"Subscription ID: {subscription_id}")
        print("=" * 70)


        # --------------------------------------------------
        # Authorization Client
        # --------------------------------------------------

        auth_client = AuthorizationManagementClient(
            credential,
            subscription_id
        )


        # --------------------------------------------------
        # Get all RBAC assignments
        # --------------------------------------------------

        scope = f"/subscriptions/{subscription_id}"
        assignments = auth_client.role_assignments.list_for_scope(
            scope,
            filter="atScope()"
        )


        # --------------------------------------------------
        # Process each assignment
        # --------------------------------------------------

        for assignment in assignments:

            principal_id = assignment.principal_id
            role_definition_id = assignment.role_definition_id
            assignment_scope = assignment.scope


            # --------------------------------------------------
            # Get Role Definition
            # --------------------------------------------------

            try:

                role_definition = auth_client.role_definitions.get_by_id(
                    role_definition_id
                )

                role_name = role_definition.role_name

            except Exception as error:

                print(
                    f"[WARNING] Could not resolve role "
                    f"{role_definition_id}: {error}"
                )

                role_name = "UNKNOWN"


            # --------------------------------------------------
            # Check whether role is privileged
            # --------------------------------------------------

            if role_name in PRIVILEGED_ROLES:
                privileged = "YES"
            else:
                privileged = "NO"


            # --------------------------------------------------
            # Print result
            # --------------------------------------------------

            print(
                f"Principal: {principal_id}"
            )

            print(
                f"Role: {role_name}"
            )

            print(
                f"Scope: {assignment_scope}"
            )

            print(
                f"Privileged: {privileged}"
            )

            print("-" * 70)


            # --------------------------------------------------
            # Write to CSV
            # --------------------------------------------------

            writer.writerow([
                subscription_name,
                subscription_id,
                principal_id,
                role_name,
                assignment_scope,
                privileged,
                datetime.utcnow().isoformat()
            ])


print()
print("=" * 70)
print("[+] RBAC audit completed")
print(f"[+] Report generated: {OUTPUT_FILE}")
print("=" * 70)
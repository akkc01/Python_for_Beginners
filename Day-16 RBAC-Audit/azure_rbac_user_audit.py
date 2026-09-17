from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.subscription import SubscriptionClient

from msgraph import GraphServiceClient

import csv
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

OUTPUT_FILE = "azure_rbac_user_report.csv"

PRIVILEGED_ROLES = {
    "Owner",
    "User Access Administrator",
    "Contributor"
}


# ============================================================
# AUTHENTICATION
# ============================================================

print("[+] Authenticating to Azure...")

credential = DefaultAzureCredential()

subscription_client = SubscriptionClient(
    credential
)

graph_client = GraphServiceClient(
    credentials=credential,
    scopes=["https://graph.microsoft.com/.default"]
)


# ============================================================
# CACHE
# Avoid calling Microsoft Graph repeatedly for same principal
# ============================================================

principal_cache = {}


# ============================================================
# RESOLVE PRINCIPAL
# ============================================================

def get_principal_details(principal_id):

    # Return cached value if already resolved
    if principal_id in principal_cache:
        return principal_cache[principal_id]

    # --------------------------------------------------------
    # Try User
    # --------------------------------------------------------

    try:

        user = graph_client.users.by_user_id(
            principal_id
        ).get()

        if user:

            name = user.display_name or "Unknown User"

            email = (
                user.mail
                or user.user_principal_name
                or "No Email"
            )

            result = {
                "type": "User",
                "name": name,
                "email": email
            }

            principal_cache[principal_id] = result

            return result

    except Exception:
        pass


    # --------------------------------------------------------
    # Try Group
    # --------------------------------------------------------

    try:

        group = graph_client.groups.by_group_id(
            principal_id
        ).get()

        if group:

            result = {
                "type": "Group",
                "name": group.display_name or "Unknown Group",
                "email": group.mail or ""
            }

            principal_cache[principal_id] = result

            return result

    except Exception:
        pass


    # --------------------------------------------------------
    # Try Service Principal
    # --------------------------------------------------------

    try:

        sp = graph_client.service_principals.by_service_principal_id(
            principal_id
        ).get()

        if sp:

            result = {
                "type": "Service Principal",
                "name": sp.display_name or "Unknown SP",
                "email": ""
            }

            principal_cache[principal_id] = result

            return result

    except Exception:
        pass


    # --------------------------------------------------------
    # Unknown Principal
    # --------------------------------------------------------

    result = {
        "type": "Unknown",
        "name": "Unknown",
        "email": ""
    }

    principal_cache[principal_id] = result

    return result


# ============================================================
# CSV
# ============================================================

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow([
        "User Name",
        "User Email",
        "Principal Type",
        "Principal ID",
        "Subscription",
        "Subscription ID",
        "Role",
        "Scope",
        "Privileged",
        "Generated At"
    ])


    # ========================================================
    # GET ALL SUBSCRIPTIONS
    # ========================================================

    for subscription in subscription_client.subscriptions.list():

        subscription_id = subscription.subscription_id

        subscription_name = subscription.display_name

        print()
        print("=" * 80)
        print(f"Subscription : {subscription_name}")
        print(f"Subscription ID : {subscription_id}")
        print("=" * 80)


        # ----------------------------------------------------
        # Authorization Client
        # ----------------------------------------------------

        auth_client = AuthorizationManagementClient(
            credential,
            subscription_id
        )


        # ----------------------------------------------------
        # Subscription scope
        # ----------------------------------------------------

        scope = f"/subscriptions/{subscription_id}"


        # ----------------------------------------------------
        # Get RBAC assignments
        # ----------------------------------------------------

        assignments = auth_client.role_assignments.list_for_scope(
            scope
        )


        # ====================================================
        # PROCESS ASSIGNMENTS
        # ====================================================

        for assignment in assignments:

            principal_id = assignment.principal_id

            role_definition_id = assignment.role_definition_id

            assignment_scope = assignment.scope


            # ------------------------------------------------
            # Get role name
            # ------------------------------------------------

            try:

                role_definition = (
                    auth_client.role_definitions.get_by_id(
                        role_definition_id
                    )
                )

                role_name = role_definition.role_name

            except Exception as error:

                print(
                    f"[WARNING] Could not resolve role "
                    f"{role_definition_id}: {error}"
                )

                role_name = "UNKNOWN"


            # ------------------------------------------------
            # Resolve user / group / service principal
            # ------------------------------------------------

            principal = get_principal_details(
                principal_id
            )


            principal_type = principal["type"]

            principal_name = principal["name"]

            principal_email = principal["email"]


            # ------------------------------------------------
            # Privileged check
            # ------------------------------------------------

            privileged = (
                "YES"
                if role_name in PRIVILEGED_ROLES
                else "NO"
            )


            # ------------------------------------------------
            # Console output
            # ------------------------------------------------

            print(
                f"User       : {principal_name}"
            )

            print(
                f"Email      : {principal_email}"
            )

            print(
                f"Type       : {principal_type}"
            )

            print(
                f"Role       : {role_name}"
            )

            print(
                f"Scope      : {assignment_scope}"
            )

            print(
                f"Privileged : {privileged}"
            )

            print("-" * 80)


            # ------------------------------------------------
            # Write CSV
            # ------------------------------------------------

            writer.writerow([
                principal_name,
                principal_email,
                principal_type,
                principal_id,
                subscription_name,
                subscription_id,
                role_name,
                assignment_scope,
                privileged,
                datetime.utcnow().isoformat()
            ])


# ============================================================
# COMPLETED
# ============================================================

print()
print("=" * 80)

print("[+] RBAC audit completed")

print(
    f"[+] Report generated: {OUTPUT_FILE}"
)

print("=" * 80)
import subprocess
import json
import csv
from datetime import datetime, timezone


# ============================================================
# CONFIGURATION
# ============================================================

OUTPUT_FILE = "azure_rbac_user_report.csv"

# Roles considered privileged
PRIVILEGED_ROLES = {
    "Owner",
    "User Access Administrator",
    "Contributor",
    "Key Vault Administrator",
    "Key Vault Secrets Officer",
    "Key Vault Secrets User",
    "Storage Blob Data Owner",
}


# ============================================================
# AZ CLI HELPER
# ============================================================

def run_az(command):

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:

            print(
                f"[WARNING] Command failed:"
            )

            print(
                " ".join(command)
            )

            if result.stderr:
                print(
                    result.stderr.strip()
                )

            return None

        if not result.stdout.strip():

            return None

        return json.loads(
            result.stdout
        )

    except json.JSONDecodeError:

        print(
            "[WARNING] Invalid JSON returned by Azure CLI"
        )

        return None

    except Exception as error:

        print(
            f"[ERROR] {error}"
        )

        return None


# ============================================================
# CHECK AZURE LOGIN
# ============================================================

print()
print("=" * 90)
print("[+] Checking Azure authentication...")
print("=" * 90)

account = run_az([
    "az",
    "account",
    "show",
    "-o",
    "json"
])


if not account:

    print()
    print("[ERROR] Azure login not found.")
    print()
    print("Run:")
    print("az login")
    print()

    exit(1)


current_user = (
    account
    .get("user", {})
    .get("name", "Unknown")
)

tenant_id = account.get(
    "tenantId",
    "Unknown"
)


print(
    f"[+] Logged in as : {current_user}"
)

print(
    f"[+] Tenant ID    : {tenant_id}"
)


# ============================================================
# LOAD ALL USERS
# ============================================================

print()
print("=" * 90)
print("[+] Loading Entra ID users...")
print("=" * 90)

users = run_az([
    "az",
    "ad",
    "user",
    "list",
    "--all",
    "-o",
    "json"
])


if users is None:

    print(
        "[ERROR] Could not retrieve Entra users."
    )

    users = []


print(
    f"[+] Users loaded: {len(users)}"
)


# ============================================================
# CREATE USER LOOKUP
# ============================================================

principal_lookup = {}


for user in users:

    object_id = user.get(
        "id"
    )

    if not object_id:
        continue


    principal_lookup[
        object_id.lower()
    ] = {

        "type": "User",

        "name": user.get(
            "displayName",
            "Unknown"
        ),

        "email": user.get(
            "userPrincipalName",
            user.get(
                "mail",
                ""
            )
        )
    }


# ============================================================
# LOAD ALL GROUPS
# ============================================================

print()
print("=" * 90)
print("[+] Loading Entra ID groups...")
print("=" * 90)


groups = run_az([
    "az",
    "ad",
    "group",
    "list",
    "--all",
    "-o",
    "json"
])


if groups is None:

    print(
        "[WARNING] Could not retrieve groups."
    )

    groups = []


print(
    f"[+] Groups loaded: {len(groups)}"
)


# ============================================================
# ADD GROUPS TO LOOKUP
# ============================================================

for group in groups:

    object_id = group.get(
        "id"
    )

    if not object_id:
        continue


    principal_lookup[
        object_id.lower()
    ] = {

        "type": "Group",

        "name": group.get(
            "displayName",
            "Unknown Group"
        ),

        "email": group.get(
            "mail",
            ""
        )
    }


# ============================================================
# LOAD ALL SERVICE PRINCIPALS
# ============================================================

print()
print("=" * 90)
print("[+] Loading Service Principals...")
print("=" * 90)


service_principals = run_az([
    "az",
    "ad",
    "sp",
    "list",
    "--all",
    "-o",
    "json"
])


if service_principals is None:

    print(
        "[WARNING] Could not retrieve Service Principals."
    )

    service_principals = []


print(
    f"[+] Service Principals loaded: "
    f"{len(service_principals)}"
)


# ============================================================
# ADD SERVICE PRINCIPALS TO LOOKUP
# ============================================================

for sp in service_principals:

    object_id = sp.get(
        "id"
    )

    if not object_id:
        continue


    principal_lookup[
        object_id.lower()
    ] = {

        "type": "Service Principal",

        "name": sp.get(
            "displayName",
            "Unknown Service Principal"
        ),

        "email": ""
    }


# ============================================================
# PRINCIPAL RESOLVER
# ============================================================

def resolve_principal(principal_id):

    if not principal_id:

        return {

            "type": "Unknown",

            "name": "Unknown",

            "email": ""
        }


    principal = principal_lookup.get(
        principal_id.lower()
    )


    if principal:

        return principal


    return {

        "type": "Unknown",

        "name": "Unknown",

        "email": ""
    }


# ============================================================
# GET SUBSCRIPTIONS
# ============================================================

print()
print("=" * 90)
print("[+] Getting Azure subscriptions...")
print("=" * 90)


subscriptions = run_az([
    "az",
    "account",
    "list",
    "--all",
    "-o",
    "json"
])


if not subscriptions:

    print(
        "[ERROR] No subscriptions found."
    )

    exit(1)


enabled_subscriptions = [

    subscription

    for subscription in subscriptions

    if subscription.get(
        "state"
    ) == "Enabled"
]


print(
    f"[+] Enabled subscriptions: "
    f"{len(enabled_subscriptions)}"
)


# ============================================================
# GENERATE CSV
# ============================================================

generated_at = datetime.now(
    timezone.utc
).isoformat()


with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as csv_file:


    writer = csv.writer(
        csv_file
    )


    writer.writerow([

        "User Name",

        "User Email",

        "Principal Type",

        "Principal ID",

        "Subscription",

        "Subscription ID",

        "Role",

        "Scope",

        "Assignment ID",

        "Privileged",

        "Generated At"

    ])


    # ========================================================
    # PROCESS EACH SUBSCRIPTION
    # ========================================================

    for subscription in enabled_subscriptions:


        subscription_id = subscription.get(
            "id"
        )


        subscription_name = subscription.get(
            "name"
        )


        print()
        print("=" * 90)

        print(
            f"Subscription: "
            f"{subscription_name}"
        )

        print(
            f"Subscription ID: "
            f"{subscription_id}"
        )

        print("=" * 90)


        # ====================================================
        # GET RBAC
        # ====================================================

        assignments = run_az([

            "az",

            "role",

            "assignment",

            "list",

            "--subscription",

            subscription_id,

            "--all",

            "--include-inherited",

            "-o",

            "json"

        ])


        if assignments is None:

            print(
                "[WARNING] Could not retrieve RBAC assignments."
            )

            continue


        if len(assignments) == 0:

            print(
                "[INFO] No role assignments found."
            )

            continue


        print(
            f"[+] Found "
            f"{len(assignments)} "
            f"RBAC assignments"
        )


        # ====================================================
        # PROCESS RBAC
        # ====================================================

        for assignment in assignments:


            principal_id = assignment.get(
                "principalId"
            )


            if not principal_id:

                continue


            role_name = assignment.get(
                "roleDefinitionName",
                "Unknown"
            )


            scope = assignment.get(
                "scope",
                ""
            )


            assignment_id = assignment.get(
                "id",
                ""
            )


            # ------------------------------------------------
            # RESOLVE PRINCIPAL
            # ------------------------------------------------

            principal = resolve_principal(
                principal_id
            )


            principal_name = principal.get(
                "name",
                "Unknown"
            )


            principal_email = principal.get(
                "email",
                ""
            )


            principal_type = principal.get(
                "type",
                "Unknown"
            )


            # ------------------------------------------------
            # PRIVILEGED CHECK
            # ------------------------------------------------

            if role_name in PRIVILEGED_ROLES:

                privileged = "YES"

            else:

                privileged = "NO"


            # ------------------------------------------------
            # PRINT
            # ------------------------------------------------

            print()

            print(
                f"User       : "
                f"{principal_name}"
            )

            print(
                f"Email      : "
                f"{principal_email}"
            )

            print(
                f"Type       : "
                f"{principal_type}"
            )

            print(
                f"Principal  : "
                f"{principal_id}"
            )

            print(
                f"Role       : "
                f"{role_name}"
            )

            print(
                f"Scope      : "
                f"{scope}"
            )

            print(
                f"Privileged : "
                f"{privileged}"
            )


            # ------------------------------------------------
            # CSV
            # ------------------------------------------------

            writer.writerow([

                principal_name,

                principal_email,

                principal_type,

                principal_id,

                subscription_name,

                subscription_id,

                role_name,

                scope,

                assignment_id,

                privileged,

                generated_at

            ])


# ============================================================
# COMPLETE
# ============================================================

print()
print("=" * 90)

print(
    "[+] RBAC audit completed successfully!"
)

print(
    f"[+] Report generated: "
    f"{OUTPUT_FILE}"
)

print("=" * 90)
import subprocess
import json
import csv
from datetime import datetime, timezone


# ============================================================
# CONFIGURATION
# ============================================================

OUTPUT_FILE = "azure_rbac_user_report.csv"

# Roles considered privileged for this audit
PRIVILEGED_ROLES = {
    "Owner",
    "User Access Administrator",
    "Contributor",
}


# ============================================================
# RUN AZ CLI COMMAND
# ============================================================

def run_az_command(command):

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:

            print(
                f"[WARNING] Azure CLI command failed:\n"
                f"{' '.join(command)}"
            )

            if result.stderr:
                print(result.stderr.strip())

            return None

        if not result.stdout.strip():
            return None

        return json.loads(result.stdout)

    except json.JSONDecodeError:

        print("[WARNING] Azure CLI returned invalid JSON.")

        return None

    except Exception as error:

        print(f"[ERROR] {error}")

        return None


# ============================================================
# PRINCIPAL CACHE
# ============================================================

principal_cache = {}


# ============================================================
# GET USER / GROUP / SERVICE PRINCIPAL DETAILS
# ============================================================

def get_principal(principal_id):

    # --------------------------------------------------------
    # Return cached result
    # --------------------------------------------------------

    if principal_id in principal_cache:

        return principal_cache[principal_id]


    # --------------------------------------------------------
    # 1. TRY USER
    # --------------------------------------------------------

    user = run_az_command([
        "az",
        "ad",
        "user",
        "show",
        "--id",
        principal_id,
        "-o",
        "json"
    ])

    if user:

        result = {
            "type": "User",
            "name": user.get(
                "displayName",
                "Unknown"
            ),
            "email": user.get(
                "userPrincipalName",
                user.get("mail", "")
            )
        }

        principal_cache[principal_id] = result

        return result


    # --------------------------------------------------------
    # 2. TRY GROUP
    # --------------------------------------------------------

    group = run_az_command([
        "az",
        "ad",
        "group",
        "show",
        "--group",
        principal_id,
        "-o",
        "json"
    ])

    if group:

        result = {
            "type": "Group",
            "name": group.get(
                "displayName",
                "Unknown"
            ),
            "email": group.get(
                "mail",
                ""
            )
        }

        principal_cache[principal_id] = result

        return result


    # --------------------------------------------------------
    # 3. TRY SERVICE PRINCIPAL
    # --------------------------------------------------------

    service_principal = run_az_command([
        "az",
        "ad",
        "sp",
        "show",
        "--id",
        principal_id,
        "-o",
        "json"
    ])

    if service_principal:

        result = {
            "type": "Service Principal",
            "name": service_principal.get(
                "displayName",
                "Unknown"
            ),
            "email": ""
        }

        principal_cache[principal_id] = result

        return result


    # --------------------------------------------------------
    # 4. UNKNOWN
    # --------------------------------------------------------

    result = {
        "type": "Unknown",
        "name": "Unknown",
        "email": ""
    }

    principal_cache[principal_id] = result

    return result


# ============================================================
# CHECK AZURE LOGIN
# ============================================================

print()
print("=" * 90)
print("[+] Checking Azure authentication...")
print("=" * 90)


account = run_az_command([
    "az",
    "account",
    "show",
    "-o",
    "json"
])


if not account:

    print()
    print("[ERROR] Azure authentication not found.")
    print("[INFO] Please run:")
    print()
    print("       az login")
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
    f"[+] Logged in user : {current_user}"
)

print(
    f"[+] Tenant ID      : {tenant_id}"
)


# ============================================================
# GET ALL SUBSCRIPTIONS
# ============================================================

print()
print("=" * 90)
print("[+] Getting Azure subscriptions...")
print("=" * 90)


subscriptions = run_az_command([
    "az",
    "account",
    "list",
    "--all",
    "-o",
    "json"
])


if not subscriptions:

    print("[ERROR] No subscriptions found.")

    exit(1)


enabled_subscriptions = [
    subscription
    for subscription in subscriptions
    if subscription.get("state") == "Enabled"
]


print(
    f"[+] Enabled subscriptions found: "
    f"{len(enabled_subscriptions)}"
)


# ============================================================
# CREATE CSV
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
        "Assignment ID",
        "Privileged",
        "Generated At"
    ])


    # ========================================================
    # LOOP THROUGH SUBSCRIPTIONS
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
            f"Subscription: {subscription_name}"
        )
        print(
            f"Subscription ID: {subscription_id}"
        )
        print("=" * 90)


        # ====================================================
        # GET RBAC ASSIGNMENTS
        # ====================================================

        assignments = run_az_command([
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
            f"[+] RBAC assignments found: "
            f"{len(assignments)}"
        )


        # ====================================================
        # PROCESS ASSIGNMENTS
        # ====================================================

        for assignment in assignments:

            principal_id = assignment.get(
                "principalId"
            )

            role_name = assignment.get(
                "roleDefinitionName",
                "Unknown"
            )

            assignment_scope = assignment.get(
                "scope",
                ""
            )

            assignment_id = assignment.get(
                "id",
                ""
            )


            # ------------------------------------------------
            # Principal details
            # ------------------------------------------------

            if not principal_id:

                continue


            principal = get_principal(
                principal_id
            )


            principal_type = principal.get(
                "type",
                "Unknown"
            )

            principal_name = principal.get(
                "name",
                "Unknown"
            )

            principal_email = principal.get(
                "email",
                ""
            )


            # ------------------------------------------------
            # Privileged role check
            # ------------------------------------------------

            if role_name in PRIVILEGED_ROLES:

                privileged = "YES"

            else:

                privileged = "NO"


            # ------------------------------------------------
            # Console output
            # ------------------------------------------------

            print()

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


            # ------------------------------------------------
            # CSV output
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
                assignment_id,
                privileged,
                generated_at
            ])


# ============================================================
# COMPLETE
# ============================================================

print()
print("=" * 90)
print("[+] RBAC audit completed successfully!")
print("=" * 90)

print(
    f"[+] Report generated: {OUTPUT_FILE}"
)

print("=" * 90)
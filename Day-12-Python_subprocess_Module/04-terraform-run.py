import subprocess


def run_command(command, step_name):

    print(f"\n{'=' * 50}")
    print(f"Running: {step_name}")
    print(f"{'=' * 50}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(f"❌ {step_name} failed")
        print(result.stderr)
        return False

    print(f"✅ {step_name} completed successfully")
    return True


# ------------------------------------------------
# Terraform Init
# ------------------------------------------------

init_success = run_command(
    ["terraform", "init"],
    "Terraform Init"
)

if not init_success:
    print("❌ Init failed. Stopping pipeline.")
    exit(1)


# ------------------------------------------------
# Terraform Plan
# ------------------------------------------------

plan_success = run_command(
    ["terraform", "plan"],
    "Terraform Plan"
)

if not plan_success:
    print("❌ Plan failed. Apply will NOT run.")
    exit(1)


# ------------------------------------------------
# Terraform Apply
# ------------------------------------------------

apply_success = run_command(
    ["terraform", "apply", "-auto-approve"],
    "Terraform Apply"
)

if not apply_success:
    print("❌ Apply failed.")
    exit(1)


# ------------------------------------------------
# Success
# ------------------------------------------------

print("\n🚀 Terraform deployment completed successfully!")
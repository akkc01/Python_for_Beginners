import subprocess


def run_command(command, step_name):

    print(f"\n{'=' * 60}")
    print(f"Running: {step_name}")
    print(f"Command: {' '.join(command)}")
    print(f"{'=' * 60}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(result.stdout)

    if result.returncode != 0:
        print(f"❌ {step_name} failed")

        if result.stderr:
            print(result.stderr)

        return False

    print(f"✅ {step_name} completed successfully")
    return True


# ------------------------------------------------
# 1. Check kubectl
# ------------------------------------------------

if not run_command(
    ["kubectl", "version", "--client"],
    "Check kubectl"
):
    print("Stopping script.")
    exit(1)


# ------------------------------------------------
# 2. Check Kubernetes cluster
# ------------------------------------------------

if not run_command(
    ["kubectl", "cluster-info"],
    "Check Kubernetes Cluster"
):
    print("❌ Kubernetes cluster is not reachable.")
    exit(1)


# ------------------------------------------------
# 3. Apply Kubernetes manifest
# ------------------------------------------------

if not run_command(
    ["kubectl", "apply", "-f", "deployment.yaml"],
    "Deploy Application"
):
    print("❌ Kubernetes deployment failed.")
    exit(1)


# ------------------------------------------------
# 4. Wait for rollout
# ------------------------------------------------

if not run_command(
    [
        "kubectl",
        "rollout",
        "status",
        "deployment/my-app",
        "--timeout=120s"
    ],
    "Check Deployment Rollout"
):
    print("❌ Deployment rollout failed.")
    exit(1)


# ------------------------------------------------
# 5. Get Pods
# ------------------------------------------------

if not run_command(
    ["kubectl", "get", "pods", "-o", "wide"],
    "Check Pods"
):
    print("❌ Unable to get pods.")
    exit(1)


print("\n🚀 Kubernetes deployment completed successfully!")
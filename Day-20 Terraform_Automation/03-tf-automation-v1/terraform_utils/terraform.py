import subprocess
from pathlib import Path
import json

class Terraform:

    def __init__(self, working_dir="."):
        self.working_dir = Path(working_dir)

    # Generic Terraform command runner
    def run(self, command):
        result = subprocess.run(
            command,
            cwd=self.working_dir,
            capture_output=True,
            text=True
        )
        print(result.stdout)

        if result.returncode != 0:
            print(result.stderr)
            raise RuntimeError(
                f"Terraform command failed: {' '.join(command)}"
            )
        return result.stdout

    # Terraform Init
    def init(self):
        print("Terraform init Started")
        return self.run([
            "terraform",
            "init"
        ])

    # Terraform Format
    def fmt(self):
        print("Terraform fmt Started")
        return self.run([
            "terraform",
            "fmt"
        ])

    # Terraform Validate
    def validate(self):
        print("Terraform Validation Started")
        return self.run([
            "terraform",
            "validate"
        ])

    # Terraform Plan
    def plan(self, plan_file="tfplan"):
        print("Terraform Plan Started")
        return self.run([
            "terraform",
            "plan",
            "-out",
            plan_file
        ])

    # Terraform Plan Json file
    def plan_json(self, plan_file="tfplan"):
        result = self.run([
            "terraform",
            "show",
            "-json",
            plan_file
        ])
        return json.loads(result)

    # Terraform Apply
    def apply(self, plan_file="tfplan"):
        print("Terraform Apply Started")
        return self.run([
            "terraform",
            "apply",
            plan_file
        ])

    # Terraform Destroy
    def destroy(self):
        print("Terraform Destroy Started...")
        return self.run([
            "terraform",
            "destroy",
            "-auto-approve"
        ])
from pathlib import Path

from terraform_utils.terraform import Terraform

from terraform_utils.plan_validator import (
    TerraformPlanValidator
)

from terraform_utils.azure_validator import (
    AzureValidator
)

from terraform_utils.health_check import (
    check_application_health
)


# Project Root, Jis Python file mein ye code likha hai, us file ka parent directory project_root hoga.
project_root = Path(__file__).parent


# Terraform Working Directory
workdir = (
    project_root
    / "projects"
    / "axion-app"
    / "environment"
    / "dev"
)
# Terraform Object
terraform = Terraform(
    working_dir=workdir
)


print("\n========== TERRAFORM FMT ==========")
terraform.fmt()

print("\n========== TERRAFORM INIT ==========")
terraform.init()

print("\n========== TERRAFORM VALIDATE ==========")
terraform.validate()


print("\n========== TERRAFORM PLAN ==========")
terraform.plan()

print("\n========== PLAN JSON ==========")
plan = terraform.plan_json()


print("\n========== PLAN VALIDATION ==========")
validator = TerraformPlanValidator(
    plan
)


validator.check_public_ips()

validator.check_public_ssh()

tag_validation = validator.check_required_tags([
    "environment",
    "application",
    "owner",
    "cost_center"
])

if not tag_validation:
    print("\n PLAN VALIDATION FAILED, Terraform Apply skipped.")
    exit(1)



print("\n========== AZURE VALIDATION ==========")

subscription_id = "b8e77924-89da-41ce-8257-846989faab77"
azure = AzureValidator(
    subscription_id
)


azure.check_resource_group(
    "jarvis-dev-eastus-rg"
)



print("\n========== APPLICATION HEALTH ==========")
check_application_health(
    "https://dev.example.com/health"
)


print("\n========== DEPLOYMENT COMPLETED ==========")
from terraform_utils.plan_validator import (
    TerraformPlanValidator
)


def test_no_unauthorized_public_ip():

    plan = {
        "resource_changes": []
    }

    validator = TerraformPlanValidator(
        plan
    )

    assert validator.check_public_ips() is True


def test_required_tags():

    plan = {
        "resource_changes": [
            {
                "address": "azurerm_resource_group.axion",
                "type": "azurerm_resource_group",

                "change": {
                    "after": {
                        "tags": {
                            "environment": "dev",
                            "application": "axion",
                            "owner": "devops",
                            "cost_center": "engineering"
                        }
                    }
                }
            }
        ]
    }

    validator = TerraformPlanValidator(
        plan
    )

    assert validator.check_required_tags([
        "environment",
        "application",
        "owner",
        "cost_center"
    ]) is True
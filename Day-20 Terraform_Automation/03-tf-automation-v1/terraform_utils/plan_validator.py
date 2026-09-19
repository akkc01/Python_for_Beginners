class TerraformPlanValidator:

    def __init__(self, plan):

        self.plan = plan

        self.resources = (
            plan.get(
                "resource_changes",
                []
            )
        )

    # ========================================================
    # Check Public IP
    # ========================================================

    def check_public_ips(
        self,
        allowed_public_ips=None
    ):

        if allowed_public_ips is None:
            allowed_public_ips = []

        violations = []

        for resource in self.resources:

            if resource.get("type") != "azurerm_public_ip":
                continue

            address = resource.get("address")

            if address not in allowed_public_ips:

                violations.append(address)

        if violations:

            raise RuntimeError(
                "Unauthorized public IP resources detected: "
                f"{violations}"
            )

        print(
            "PASS: Public IP policy validated"
        )

        return True


    # Check Required Tags
    def check_required_tags(
    self,
    required_tags
):

        violations = []
        for resource in self.resources:
            change = resource.get(
                "change",
                {}
            )
            after = change.get("after")
            if not isinstance(after, dict):
                continue

            tags = after.get("tags") or {}
            missing_tags = [
                tag
                for tag in required_tags
                if tag not in tags
            ]

            if missing_tags:
                violations.append({
                    "resource": resource.get(
                        "address"
                    ),
                    "missing_tags": missing_tags
                })

        if violations:
            print(
                "\nFAIL: Required tag validation failed."
            )
            print(
                "\nMissing tags:"
            )
            for violation in violations:

                print(
                    f"  Resource: "
                    f"{violation['resource']}"
                )
                print(
                    f"  Missing tags: "
                    f"{', '.join(violation['missing_tags'])}"
                )
            # print(
            #     "\nTerraform Apply skipped."
            # )
            return False
        print(
            "PASS: Required tags validated"
        )
        return True


    # Check Public SSH
    def check_public_ssh(self):
        violations = []
        for resource in self.resources:
            if resource.get("type") != (
                "azurerm_network_security_rule"
            ):
                continue

            change = resource.get(
                "change",
                {}
            )

            after = change.get("after")

            if not after:
                continue

            port = after.get(
                "destination_port_range"
            )

            source = after.get(
                "source_address_prefix"
            )

            access = after.get(
                "access"
            )

            if (
                port == "22"
                and source == "*"
                and access == "Allow"
            ):

                violations.append(
                    resource.get("address")
                )

        if violations:

            raise RuntimeError(
                "Public SSH access detected: "
                f"{violations}"
            )

        print(
            "PASS: SSH security policy validated"
        )

        return True
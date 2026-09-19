import requests


def check_application_health(
    url,
    expected_status=200,
    timeout=10
):

    print(
        f"\nChecking application: {url}"
    )

    try:

        response = requests.get(
            url,
            timeout=timeout
        )

        print(
            f"HTTP Status: "
            f"{response.status_code}"
        )

        if response.status_code == expected_status:

            print(
                "PASS: Application health check"
            )

            return True

        print(
            "FAIL: Unexpected HTTP status"
        )

        return False

    except requests.RequestException as error:

        print(
            f"FAIL: Application unreachable: "
            f"{error}"
        )

        return False
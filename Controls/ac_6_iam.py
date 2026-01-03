import boto3

iam = boto3.client("iam")

def check_mfa():
    users = iam.list_users()["Users"]
    non_compliant = []

    for user in users:
        mfa_devices = iam.list_mfa_devices(
            UserName=user["UserName"]
        )["MFADevices"]
        if not mfa_devices:
            non_compliant.append(user["UserName"])

    return {
        "control": "IA-2",
        "description": "Multi-Factor Authentication enforced for IAM users",
        "status": "FAIL" if non_compliant else "PASS",
        "non_compliant_users": non_compliant
    }


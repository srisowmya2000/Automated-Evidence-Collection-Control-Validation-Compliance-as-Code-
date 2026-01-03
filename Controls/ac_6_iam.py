import boto3

iam = boto3.client("iam")

def check_admin_users():
    admin_users = []
    users = iam.list_users()["Users"]

    for user in users:
        policies = iam.list_attached_user_policies(
            UserName=user["UserName"]
        )["AttachedPolicies"]

        for policy in policies:
            if "AdministratorAccess" in policy["PolicyName"]:
                admin_users.append(user["UserName"])

    return {
        "control": "AC-6",
        "description": "Least privilege enforced for IAM users",
        "status": "FAIL" if admin_users else "PASS",
        "admin_users": admin_users
    }

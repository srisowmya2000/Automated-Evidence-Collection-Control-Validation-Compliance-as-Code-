import boto3

cloudtrail = boto3.client("cloudtrail")

def check_logging():
    trails = cloudtrail.describe_trails()["trailList"]

    if not trails:
        return {
            "control": "AU-12",
            "description": "Centralized audit logging enabled",
            "status": "FAIL"
        }

    status = cloudtrail.get_trail_status(
        Name=trails[0]["Name"]
    )["IsLogging"]

    return {
        "control": "AU-12",
        "description": "Centralized audit logging enabled",
        "status": "PASS" if status else "FAIL"
    }


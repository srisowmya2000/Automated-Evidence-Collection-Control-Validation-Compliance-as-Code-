import boto3

s3 = boto3.client("s3")

def check_s3_encryption():
    buckets = s3.list_buckets()["Buckets"]
    unencrypted = []

    for bucket in buckets:
        try:
            s3.get_bucket_encryption(Bucket=bucket["Name"])
        except Exception:
            unencrypted.append(bucket["Name"])

    return {
        "control": "SC-13",
        "description": "Encryption at rest enabled for S3 buckets",
        "status": "FAIL" if unencrypted else "PASS",
        "unencrypted_buckets": unencrypted
    }


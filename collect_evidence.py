import json
from Controls.ia_2_mfa import check_mfa
from Controls.ac_6_iam import check_admin_users
from Controls.sc_13_encryption import check_s3_encryption
from Controls.au_12_logging import check_logging

controls = [
    check_mfa,
    check_admin_users,
    check_s3_encryption,
    check_logging
]

results = []

for control in controls:
    try:
        results.append(control())
    except Exception as e:
        results.append({
            "control": "UNKNOWN",
            "description": "Control execution failed",
            "status": "FAIL",
            "error": str(e)
        })

with open("evidence/raw_json/evidence.json", "w") as f:
    json.dump(results, f, indent=2)

print("[+] Evidence successfully collected")


import json
from datetime import datetime, timedelta

with open("evidence/raw_json/evidence.json") as f:
    evidence = json.load(f)

poam = []

for item in evidence:
    if item["status"] == "FAIL":
        poam.append({
            "control_id": item["control"],
            "weakness_description": item["description"],
            "risk_level": "High",
            "remediation": "Review configuration and remediate per FedRAMP guidance",
            "planned_completion_date": (
                datetime.utcnow() + timedelta(days=30)
            ).strftime("%Y-%m-%d"),
            "status": "Open"
        })

with open("reports/poam.json", "w") as f:
    json.dump(poam, f, indent=2)

print("[+] POA&M generated")


import json

with open("evidence/raw_json/evidence.json") as f:
    evidence = json.load(f)

passed = []
failed = []

for item in evidence:
    if item.get("status") == "PASS":
        passed.append(item["control"])
    else:
        failed.append(item["control"])

print("=== FedRAMP Control Validation Summary ===")
print("PASSED CONTROLS:", passed)
print("FAILED CONTROLS:", failed)


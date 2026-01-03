import json

with open("evidence/raw_json/evidence.json") as f:
    evidence = json.load(f)

html = """
<html>
<head>
<title>FedRAMP Compliance Report</title>
</head>
<body>
<h1>FedRAMP Compliance Status</h1>
<table border="1" cellpadding="8">
<tr>
<th>Control</th>
<th>Description</th>
<th>Status</th>
</tr>
"""

for item in evidence:
    color = "green" if item["status"] == "PASS" else "red"
    html += f"""
    <tr>
        <td>{item.get("control")}</td>
        <td>{item.get("description")}</td>
        <td style="color:{color}">{item.get("status")}</td>
    </tr>
    """

html += "</table></body></html>"

with open("reports/fedramp_status.html", "w") as f:
    f.write(html)

print("[+] HTML compliance report generated")

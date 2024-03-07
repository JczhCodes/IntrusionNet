import pty
import os
import subprocess
import time

def execute_command_with_pty(command):
    # Spawn a new process with a pseudo-terminal
    master_fd, slave_fd = pty.openpty()
    
    # Use the slave end of the pty as the subprocess's stdin/stdout/stderr
    process = subprocess.Popen(command, stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, shell=True, close_fds=True)
    
    time.sleep(10)

    # Close the slave end in the parent process to avoid leaking file descriptors
    os.close(slave_fd)

    os.write(master_fd,b' /n')

    print("here")
    
    # Read output from the master end of the pty
    while True:
        output = os.read(master_fd, 1024).decode('utf-8')
        if output:
            print(output, end='')
        if process.poll() is not None:
            print("Probably here")
            break
    
    # Clean up
    os.close(master_fd)

# Example usage
if __name__ == "__main__":
    command = input("Enter command: ")
    execute_command_with_pty(command)

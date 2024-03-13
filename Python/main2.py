import fcntl
import os
import ptyprocess
import re
import select
import sys
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

executed_commands = []
openai_assistant_id = "asst_lKHOtM6sZupcMachal2E5J2Z"
pos_of_last_read_message = -1

def env_setup():
    """
    Prompt for OPENAI_API_KEY and save it to a .env file if not already present.
    """
    global pos_of_last_read_message  # Declare global if needed elsewhere, though not modified here
    dotenv_path = '.env'
    load_dotenv(dotenv_path=dotenv_path)

    if not os.getenv('OPENAI_API_KEY'):
        api_key = input("Please enter your OPENAI_API_KEY: ").strip()
        with open(dotenv_path, 'a') as f:
            f.write(f'OPENAI_API_KEY="{api_key}"\n')
        os.environ['OPENAI_API_KEY'] = api_key
        print("API Key saved to .env file and loaded for this session.")

def initialize_openai_client():
    """
    Initialize OpenAI client.
    """
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")
    return OpenAI(api_key=OPENAI_API_KEY)

def create_convo(client):
    return client.beta.threads.create()

def send_message(client, thread_id, message):
    global pos_of_last_read_message
    pos_of_last_read_message += 1
    return client.beta.threads.messages.create(thread_id=thread_id, role="user", content=message)

def create_run(client, thread_id):
    return client.beta.threads.runs.create(thread_id=thread_id, assistant_id=openai_assistant_id)

def check_run_status(client, run_id, thread_id):
    return client.beta.threads.runs.retrieve(run_id=run_id, thread_id=thread_id)

def get_assistant_response(client, thread_id, assistant_id):
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    assistant_responses = [msg for msg in messages.data if msg.assistant_id == assistant_id]
    return assistant_responses

def make_non_blocking(fd):
    """
    Set the file descriptor to non-blocking mode.
    """
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

def remove_ansi_escape_sequences(text):
    """
    Removes ANSI escape sequences from the given text.
    """
    ansi_escape_pattern = re.compile(r'''
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    ''', re.VERBOSE)
    return ansi_escape_pattern.sub('', text)


def execute_command(command):
    """
    Execute a given command using ptyprocess and monitor its output, allowing for potential interaction.
    This version includes a basic structure for interaction that could be extended to use OpenAI's API.
    """
    base_command = command.split()[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_command}_results_{timestamp}.txt"

    try:
        # Start the command in a new pseudo-terminal
        pty_proc = ptyprocess.PtyProcessUnicode.spawn(command.split(), echo=False)
        
        time.sleep(60)

        # pty_proc.write('\n')

       # Open a file for writing the output
        with open(filename, 'w') as file:
            # Initial assumption: the command is non-interactive
            interactive = False
            interaction_timeout = 60  # seconds
            last_output_time = time.time()

            while True:
                # Check if there is output to read
                if pty_proc.isalive():
                    # Non-blocking read with a timeout
                    r, w, x = select.select([pty_proc.fd], [], [], 0.1)
                    if r:
                        output = pty_proc.read()
                        cleaned_output = remove_ansi_escape_sequences(output)
                        print(cleaned_output, end='')
                        file.write(cleaned_output)
                        file.flush()  # Force flushing to disk after each write

                    # If no output has been received for a certain period, assume the command might be waiting for input
                    elif not interactive and time.time() - last_output_time > interaction_timeout:
                        interactive = True
                        # Placeholder for sending input or interacting with OpenAI API
                        # Example: write 'help\n' to the process; replace with actual dynamic input as needed
                        # pty_proc.write('\n')
                    
                    elif pty_proc.eof():
                        break
                    
                else:
                    # Process has finished
                    break
    except Exception as e:
        print(f"Error executing command: {e}")
    finally:
        if pty_proc.isalive():
            # Ensure the process is terminated
            pty_proc.terminate(force=True)

def main(ip_address):
        # Initialization of client, assistant and thread
    client = initialize_openai_client()
    # assistant_id = create_assistant(client)
    thread = create_convo(client)
    send_message(client, thread.id, f"The IP of the client's machine is {ip_address}. Begin!")
    
    # Main Loop
    while True:
        run = create_run(client, thread.id)  # Initiate conversation with the assistant
        while True:
            run_status = check_run_status(client, run.id, thread.id)
            if run_status.status == "completed":
                messages_response = get_assistant_response(client, thread.id, assistant_id="asst_fQtvoPQoorPE05G1D1Pe2udI")
                break  # Exit the inner loop if the run is completed
            time.sleep(10)  # Wait before checking the status again
        
       # Check the type of messages_response to handle both list and string cases
        if isinstance(messages_response, str):
            print(messages_response)  # Or handle the "No new messages." case as needed
            break  # or continue based on your application's logic
        elif isinstance(messages_response, list):
            for message in messages_response:
                # Assuming message structure is consistent with the provided JSON
                if message.assistant_id and message.content:
                    command = message['content'][0]['text']['value']
                    if command not in executed_commands:
                        executed_commands.append(command)
                        print(f"Executing command: {command}")
                        execute_command(command)  # Adjust this function if needed to handle command execution and response

                    with open(filename, 'r') as file:
                        file_content = file.read()
                        send_message(client, thread.id, file_content)  # Send the output back to the thread
                
        time.sleep(10)  # Optional: Wait before starting a new run or processing further


if __name__ == "__main__":
    # Check for IP address
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        env_setup()
        main(ip_address)
    else:
        print("Please provide an IP address")
        sys.exit(1)
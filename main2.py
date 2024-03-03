import datetime
import fcntl
import os
import select
import subprocess
import time
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

def get_assistant_response(client, thread_id):
    global pos_of_last_read_message
    conversation = client.beta.threads.messages.list(thread_id=thread_id)
    total_messages = len(conversation.data)
    if pos_of_last_read_message == total_messages - 1:
        return "No new messages."
    new_messages = conversation.data[pos_of_last_read_message + 1:]
    pos_of_last_read_message = total_messages - 1
    return new_messages

def make_non_blocking(fd):
    """
    Set the file descriptor to non-blocking mode.
    """
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

def execute_command(command):
    """
    Execute a given command and monitor its output, allowing for potential interaction.
    This version includes a basic structure for interaction that could be extended to use OpenAI's API.
    """
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True, bufsize=1)
    
    # Use non-blocking IO on the subprocess' stdout and stderr
    stdout_fileno = process.stdout.fileno()
    stderr_fileno = process.stderr.fileno()
    make_non_blocking(stdout_fileno)
    make_non_blocking(stderr_fileno)

    # Initial assumption: the command is non-interactive
    interactive = False
    interaction_timeout = 2  # seconds
    last_output_time = time.time()

    while True:
        # Check if the command has produced output
        reads = [stdout_fileno, stderr_fileno]
        readable, writable, exceptional = select.select(reads, [], reads, 0.1)

        output_received = False
        for fd in readable:
            if fd == stdout_fileno:
                output = process.stdout.read()
                if output:
                    print(output)
                    output_received = True
            elif fd == stderr_fileno:
                output = process.stderr.read()
                if output:
                    print(output)
                    output_received = True
        
        # Update the time of the last output received
        if output_received:
            last_output_time = time.time()

        # If no output has been received for a certain period, assume the command might be waiting for input
        if not interactive and time.time() - last_output_time > interaction_timeout:
            interactive = True
            # Placeholder for sending input or interacting with OpenAI API
            # process.stdin.write('your next command\n')
            # process.stdin.flush()

        if process.poll() is not None:
            # Process has finished
            break
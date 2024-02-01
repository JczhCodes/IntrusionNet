from openai import OpenAI
import time
from dotenv import load_dotenv
import os
import subprocess
import sys
import logging

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get API key and Assistant ID from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ASSISTANT_ID = os.getenv('OPENAI_ASSISTANT_ID')

# Function definitions
def initialize_openai_client():
    """
    Initialize OpenAI client.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client

def create_assistant(client):
    """
    Create an Assistant.
    """
    assistant = client.beta.assistants.create(
        name="AI-PenTest-Tool",
        instructions="""
                    You are a Cyber Security Specialist. Respond with only the necessary pentest commands.

                    - When provided with an IP, give initial reconnaissance commands.
                    - If there is a login feature, always test username without password first.
                    - For subsequent steps, provide relevant commands based on the situation. For each query, Provide only 1 command at a time. 
                    - If there is multiple commands, wait for the return of the results before providing the next command
                    - Only when all ports are done being pen tested, your output should be "Pen Test is Complete"

                    Commands should be presented plainly:
                    command
                    """,
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-preview"
    )
    assistant_id = assistant.id  # Retrieve the Assistant ID
    write_to_env_if_empty("OPENAI_ASSISTANT_ID", assistant_id)
    return assistant

def create_thread(client):
    """
    Create a new thread.
    """
    thread = client.beta.threads.create()
    return thread

def send_message(client, thread_id, content):
    """
    Send a message in the thread.
    """
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )
    return message

def list_messages(client, thread_id):
    """
    List messages in a thread.
    """
    return client.beta.threads.messages.list(thread_id=thread_id)

def create_run(client, thread_id, assistant_id):
    """
    Create a Run.
    """
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    return run

def check_run_status(client, run_id, thread_id):
    """
    Check the run status.
    """
    run_status = client.beta.threads.runs.retrieve(run_id=run_id, thread_id=thread_id)
    return run_status

def execute_command(command, output_file='command_result.txt', timeout=None):
    """
    Execute a shell command and return its output and error separately, 
    and write the output to a specified file, also print the command and its output.
    """
    print(f"Executing command: {command}")  # Print the command being executed
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=timeout)
        # logging.info("Command output: %s", output)
        print(output)  # Print the output to console

        with open(output_file, 'a') as file:
            file.write(f"Command: {command}\nOutput:\n{output}\n")  # Write command and output to file

        return output, None
    except subprocess.CalledProcessError as e:
        #logging.error("Error executing command: %s", e.output)
        print("Error executing command:", e.output)  # Print the error to console

        with open(output_file, 'a') as file:
            file.write(f"Command: {command}\nError executing command: {e.output}\n")  # Write command and error to file

        return None, e.output
    except subprocess.TimeoutExpired as e:
        #logging.error("Command timed out: %s", command)
        print(f"Command timed out: {command}")  # Print the timeout error to console

        with open(output_file, 'a') as file:
            file.write(f"Command: {command}\nError: Timeout\n")  # Write command and timeout error to file

        return None, "Timeout"

def is_pen_test_complete(message):
    """
    Determine if the pen test is complete
    """
    # Implement logic to determine if the assistant indicates the test is complete
    # For example, look for a specific phrase in the message
    return message.strip().lower() == "pen test is complete"

def read_file_content(file_path):
    """
    Read the contents of a file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_to_env_if_empty(key, value):
    """
    Write a key-value pair to the .env file only if the key is empty or does not exist.
    """
    # Load existing environment variables
    load_dotenv()

    # Check if the key is empty or does not exist
    if not os.getenv(key):
        with open(".env", "a") as env_file:
            env_file.write(f"{key}={value}\n")

def main():
    # Initialize client, assistant and thread
    client = initialize_openai_client()
    assistant = create_assistant(client)
    thread = create_thread(client)

    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
    else:
        print("Please provide an IP address.")
        sys.exit(1)

    # Start the pen test
    send_message(client, thread.id, f"I want to pen test this machine {ip_address}")
    run = create_run(client, thread.id, OPENAI_ASSISTANT_ID)  # Use the assistant ID from env variable

    # Main loop
    while True:
        # Wait for the assistant's response
        while True:
            run_status = check_run_status(client, run.id, thread.id)
            if run_status.status == 'completed':
                messages_response = list_messages(client, thread.id)
                break
            time.sleep(5)

        # Extract and potentially execute the command
        print(messages_response)
        message_content = messages_response.data[0].content[0].text.value
        # print("Assistant Response:", message_content)

        # Check if the pen test is complete
        if is_pen_test_complete(message_content):
            print("Pen test is complete.")
            break

        # Check if the message is a command to execute
        if message_content.strip() and not message_content.startswith("Pen Test is Complete"):
            print("Starting to execute command")
            command_output, error = execute_command(message_content)
            message_content_to_send = command_output if command_output is not None else "Error executing command: " + (error if error else "Unknown error")
        else:
            message_content_to_send = "Command execution skipped or not a command"

        # Send back the results and continue the test
        send_message(client, thread.id, message_content_to_send)
        run = create_run(client, thread.id, OPENAI_ASSISTANT_ID)


if __name__ == "__main__":
    main()
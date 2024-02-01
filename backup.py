from openai import OpenAI
import time
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

# Get API key and Assistant ID from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ASSISTANT_ID = os.getenv('OPENAI_ASSISTANT_ID')

def initialize_openai_client():
    """
    Initialize OpenAI client.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client

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

def create_assistant(client):
    """
    Create an Assistant.
    """
    assistant = client.beta.assistants.create(
        name="AI-PenTest-Tool",
        instructions="""
                    You are a Cyber Security Specialist. Respond with only the necessary pentest commands.

                    - Your responses should only be code, without explanation or formatting
                    - When provided with an IP, give initial reconnaissance commands.
                    - For subsequent steps, provide relevant commands based on the situation.
                    - When Pen Test is done, your output should be "Pen Test is Complete"

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

def read_file_content(file_path):
    """
    Read the contents of a file.
    """
    with open(file_path, 'r') as file:
        return file.read()
    
def execute_command(command):
    """
    Execute a shell command and return its output.
    """
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        print("Command output:", output)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e.output)

def is_pen_test_complete(message):
    """
    Determine if the pen test is complete
    """
    # Implement logic to determine if the assistant indicates the test is complete
    # For example, look for a specific phrase in the message
    return "pen test complete" in message.lower()

# Example usage
client = initialize_openai_client()
assistant = create_assistant(client)
thread = create_thread(client)
send_message(client, thread.id, "I want to pen test this machine 192.168.1.205")
run = create_run(client, thread.id, OPENAI_ASSISTANT_ID)  # Use the assistant ID from env variable

while True:
    run_status = check_run_status(client, run.id, thread.id)
    if run_status.status == 'completed':
        messages_response = list_messages(client, thread.id)
        break
    time.sleep(5)  # Wait for 5 seconds before checking the status again

message_content = messages_response.data[0].content[0].text.value
print(messages_response)
print(message_content)

nmap_scan_content = read_file_content("nmap_scan_result.txt")
send_message(client, thread.id, nmap_scan_content)
run = create_run(client, thread.id, OPENAI_ASSISTANT_ID)

while True:
    run_status = check_run_status(client, run.id, thread.id)
    if run_status.status == 'completed':
        messages_response = list_messages(client, thread.id)
        break
    time.sleep(5)  # Wait for 5 seconds before checking the status again

message_content = messages_response.data[0].content[0].text.value
print(messages_response)
print(message_content)
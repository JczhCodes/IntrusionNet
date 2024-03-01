import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI

executed_commands = []
openai_assistant_id = "asst_lKHOtM6sZupcMachal2E5J2Z"
pos_of_last_read_message = -1

def env_setup():
    """
    Check if OPENAI_API_KEY and save it to a .env file if not already present.
    """
    # Load existing environment variables
    dotenv_path = '.env'
    load_dotenv(dotenv_path=dotenv_path)

    # Check if the OPENAI_API_KEY is already set
    if not os.getenv('OPENAI_API_KEY'):
        # If not set, prompt the user to enter it
        api_key = input("Please enter your OPENAI_API_KEY: ").strip()
        
        # Append or create the .env file with the OPENAI_API_KEY
        with open(dotenv_path, 'a') as f:
            f.write(f'OPENAI_API_KEY="{api_key}"\n')
        
        # Update the current environment variable for this execution
        os.environ['OPENAI_API_KEY'] = api_key
        print("API Key saved to .env file and loaded for this session.")

def initialize_openai_client():
    """
    Initialize OpenAI client
    """
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")

    return OpenAI(api_key=OPENAI_API_KEY)

def create_convo(client):
    """
    Create a new thread.
    A thread represents a conversation.
    """
    return client.beta.threads.create()

def send_message(client, thread_id, message):
    """
    Send the message into the conversation
    """
    pos_of_last_read_message += 1
    return client.beta.threads.messages.create(thread_id=thread_id, role="user", content=message)

def create_run(client, thread_id):
    """
    Make assistant read the convo
    """
    return client.beta.threads.runs.create(thread_id=thread_id, assistant_id=openai_assistant_id)

def check_run_status(client, run_id, thread_id):
    """
    Check if assistant finish reading the convo
    """
    return client.beta.threads.runs.retrieve(run_id=run_id, thread_id=thread_id)

def get_assistant_response(client, thread_id):
    """
    Reterive assistant's new response
    """
    conversation = client.beta.threads.messages.list(thread_id=thread_id)
    total_messages = len(conversation.data)
    while pos_of_last_read_message != total_messages:
        return "No new messages."
    
    new_messages = conversation.data[pos_of_last_read_message + 1:]

    pos_of_last_read_message = total_messages - 1

    return new_messages

def execute_command(command):
    """
    Execute a shell command and return its output and error separately,
    and write the output to a specified file, also print the command and its output.
    """
    base_command = command.split()[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_command}_results_{timestamp}.txt"

    try:
        with open()
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

assistant_id = None

def env_setup():
    """
    Check if OpenAI Key and Assistant ID exists
    Else prompt and create and save to .env file
    Prompt for OPENAI_API_KEY and check if assistant is created and save it to a .env file if not already present.
    """
    global assistant_id  # Declare the use of the global variable
    dotenv_path = '.env'
    load_dotenv(dotenv_path=dotenv_path)
    api_key_exists = False
    assistant_id_exists = False

    if not os.getenv('OPENAI_API_KEY'):
        api_key = input("Please enter your OPENAI_API_KEY: ").strip()
        with open(dotenv_path, 'a') as f:
            f.write(f'OPENAI_API_KEY="{api_key}"\n')
        os.environ['OPENAI_API_KEY'] = api_key
        print("API Key saved to .env file and loaded for this session.")
    else:
        api_key_exists = True

    client = initialize_openai_client()

    if not os.getenv('ASSISTANT_ID'):
        assistant_id = create_assistant(client)
        with open(dotenv_path, 'a') as f:
            f.write(f'ASSISTANT_ID="{assistant_id}"\n')
        os.environ['ASSISTANT_ID'] = assistant_id
        print("Assistant ID saved to .env file and loaded for this session.")
    else:
        assistant_id_exists = True
        assistant_id = os.getenv('ASSISTANT_ID')  # Ensure the global variable is updated

    if api_key_exists and assistant_id_exists:
        print("API Key and Assistant ID are already set.")
    
    return client

def initialize_openai_client():
    """
    Initialize OpenAI client.
    """
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")
    return OpenAI(api_key=OPENAI_API_KEY)

def create_assistant(client):
    """
    Create an Assistant.
    """
    assistant = client.beta.assistants.create(
        name="AI-PenTest-Tool",
        instructions="""
""",
        model="gpt-4-turbo-preview"
    )
    return assistant.id

def create_convo(client):
    return client.beta.threads.create()

def send_message(client, thread_id, message):
    return client.beta.threads.messages.create(thread_id=thread_id, role="user", content=message)

def create_run(client, thread_id, assistant_id):
    return client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)

def check_run_status(client, run_id, thread_id):
    return client.beta.threads.runs.retrieve(run_id=run_id, thread_id=thread_id)

def get_assistant_response(client, thread_id):
    thread_messages_response = client.beta.threads.messages.list(thread_id, limit=1, order="desc")
    
    # Check if there are any messages in the thread
    if not thread_messages_response.data:
        print("No messages found in the thread.")
        return None
    
    # The latest message is expected to be the first item in the 'data' list
    latest_message = thread_messages_response.data[0]

    # Extract the 'content' field from the latest message
    # Assuming 'content' is a list with at least one item and that item has a 'text' field
    if latest_message.content and len(latest_message.content) > 0:
        latest_message_content = latest_message.content[0].text.value
        print(f"Latest message: {latest_message_content}")
        return latest_message_content
    else:
        print("Latest message has no content.")
        return None


def main(ip_address):
    # Setup API Key and Assistant
    client = env_setup()
    # Setup conversation
    thread = create_convo(client)
    
    # Send the first message to OpenAI
    send_message(client, thread.id, f"The IP of the client's machine is {ip_address}. Begin!")

    # Start the conversation loop
    while True:
        # Wait for the run to complete
        run = create_run(client, thread.id, assistant_id)
        while True:
            run_status_response = check_run_status(client, run.id, thread.id)
            if run_status_response.status == "completed":  # Assuming the response has a 'status' attribute
                message_response = get_assistant_response(client, thread.id)
                if message_response:  # Check if a message was received
                    break  # Exit the inner loop if the run is completed
            time.sleep(1)  # Add a short delay to avoid overwhelming the API with requests
        
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        main(ip_address)
    else:
        print("Please provide an IP address")
        sys.exit(1)
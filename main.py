from openai import OpenAI
import time
from dotenv import load_dotenv
import os

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

def create_assistant(client):
    """
    Create an Assistant.
    """
    assistant = client.beta.assistants.create(
        name="AI-PenTest-Tool",
        instructions="""
        You are a Cyber Security Specialist with a vast knowledge of all fields of Cyber Security. You will only respond to the query with the appropriate commands needed for the pentest. If a code is required, respond with just the code snippet.You do not require to explain. Respond with the COMMANDS ONLY. 1. A IP will be provided. Provide a steps for reconnaissance. 2. Based on the output given, Provide commands to continue.
        """,
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-preview"
    )
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

# Example usage
client = initialize_openai_client()
# assistant = create_assistant(client)
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
print(message_content)
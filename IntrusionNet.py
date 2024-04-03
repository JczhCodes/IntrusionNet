import os
import pexpect
import re
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI

def env_setup():
    """
    Check if OpenAI Key and Assistant ID exists
    Else prompt and create and save to .env file
    Prompt for OPENAI_API_KEY and check if assistant is created and save it to a .env file if not already present.
    """
    dotenv_path = '.env'
    load_dotenv(dotenv_path=dotenv_path)

    # Check and set OPENAI_API_KEY
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        openai_api_key = input("Please enter your OPENAI_API_KEY: ").strip()
        with open(dotenv_path, 'a') as f:
            f.write(f'OPENAI_API_KEY="{openai_api_key}"\n')
        print("API Key saved to .env file.")
    os.environ['OPENAI_API_KEY'] = openai_api_key  # Ensure it's available in the current session
    return openai_api_key

def initialize_openai_client(api_key):
    """
    Initialize OpenAI client.
    """
    return OpenAI(api_key=api_key)

def create_assistant(client):
    """
    Create an Assistant.
    """
    dotenv_path = '.env'
    load_dotenv(dotenv_path=dotenv_path)
    assistant_id = os.getenv('ASSISTANT_ID')
    if not assistant_id:
        assistant = client.beta.assistants.create(
            name="AI-PenTest-Tool",
            instructions="""
    """,
            model="gpt-4-turbo-preview"
        )

        assistant_id = assistant.id
        # Save the new ASSISTANT_ID to the .env file and load it into the environment
        with open(dotenv_path, 'a') as f:
            f.write(f'ASSISTANT_ID="{assistant_id}"\n')
        print("New Assistant ID saved to .env file and loaded for this session.")
        os.environ['ASSISTANT_ID'] = assistant_id  # Make it available in the current session
    else:
        print("Assistant ID already exists.")
    return assistant_id

def create_convo(client):
    """
    
    """
    return client.beta.threads.create()

def create_message(client, thread_id, message):
    return client.beta.threads.messages.create(thread_id=thread_id, role="user", content=message)

def send_message(client, thread_id, assistant_id):
    return client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)

def check_run_status(client, run_id, thread_id):
    return client.beta.threads.runs.retrieve(run_id=run_id, thread_id=thread_id)

def get_assistant_response(client, thread_id):
    conversation = client.beta.threads.messages.list(thread_id, limit=1, order="desc")

    if not conversation.data:
        print("No messages found in the thread.")
        return None
    else:
        return conversation.data[0].content[0].text.value

def clean_assistant_response(response):
    # First, try to extract content within triple backticks
    matches = re.findall(r"```(.*?)```", response, re.DOTALL)
    if matches:
        # If found, use the first match
        cleaned_command = matches[0]
    else:
        # If no triple backticks content, remove any surrounding single backticks and work with the response directly
        cleaned_command = re.sub(r"^`|`$", "", response).strip()
    
    # After handling triple or single backticks, remove 'bash' prefix if present
    cleaned_command = re.sub(r"^(bash\s+)?", "", cleaned_command).strip()

    # Replace escaped newlines and condense multiple spaces into one
    cleaned_command = re.sub(r"\\n", " ", cleaned_command)  # Replace escaped newlines with space
    cleaned_command = re.sub(r"\s{2,}", " ", cleaned_command)  # Condense multiple spaces into one

    return cleaned_command if cleaned_command else None


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
    
def execute_command(client, thread_id, command):
    """
    Executes the provided command in a interactive shell, handles EOF
    and continues interaction based on specific output
    """
    try:
        process = pexpect.spawn(command, encoding='utf-8', codec_errors='ignore')

        msf6_regex = r"msf6.*>\s"

        command_shell = r"(shell.*opened|Command Shell Session \d+\* Opened)"

        index = process.expect([pexpect.EOF, msf6_regex, command_shell], timeout = 200)

        if index == 0:
            output = process.before
            output = remove_ansi_escape_sequences(output)
            create_message(client, thread_id, output)

        elif index == 1 or index == 2:
            output = process.before + process.after
            output = remove_ansi_escape_sequences(output)
            create_message(client, thread_id, output)

    except pexpect.exceptions.EOF:
        create_message(client, thread_id, "Command has completed.")

    except pexpect.exceptions.TIMEOUT:
        create_message(client, thread_id, "Command has timed out.")

    except pexpect.exceptions.ExceptionPexpect:
        create_message(client, thread_id, "Command was not found or was not executable. Please provide commands only.")

def main(ip_address):
    # Setup API Key
    api_key = env_setup()
    client = initialize_openai_client(api_key)
    assistant = create_assistant(client)
    # Setup conversation
    thread = create_convo(client)
    
    # Send the first message to OpenAI
    create_message(client, thread.id, f"The IP of the client's machine is {ip_address}. Begin!")

    # Start conversation loop
    while True:
        run = send_message(client, thread.id, assistant)        
        while True:
            response_ready_check = check_run_status(client, run.id, thread.id).status
            if response_ready_check == "completed":
                break
            else: 
                time.sleep(10)

        response = get_assistant_response(client, thread.id)
        print("\nIntrusionNet:\n",response, "\n")
        command_to_execute = clean_assistant_response(response)
        print("Executing Command: ", command_to_execute)

        if command_to_execute == "Penetration test is complete.":
            break

        execute_command(client, thread.id, assistant, command_to_execute)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        try:
            main(ip_address)
        except KeyboardInterrupt:
            print("You have ended the process.")
    else:
        print("Please provide an IP address")
        sys.exit(1)
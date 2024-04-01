import fcntl
import os
import pexpect
import re
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

def create_message(client, thread_id, message):
    return client.beta.threads.messages.create(thread_id=thread_id, role="user", content=message)

def send_message(client, thread_id, assistant_id):
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
        # Clean the command: Remove triple quotes from the start and end of the command string
        cleaned_command = latest_message_content.strip("'''")
        print(f"Latest message: {cleaned_command}")
        return cleaned_command
        # print(f"Latest message: {latest_message_content}")
        # return latest_message_content
    else:
        print("Latest message has no content.")
        return None
    
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
    if command == "Penetration test is complete.":
        print("Penetration test is complete.")
        exit()

    process = pexpect.spawn(command, encoding='utf-8', codec_errors='ignore')

    msf6_regex = r"msf6.*>\s"

    command_shell = r"(shell.*opened|Command Shell Session \d+\* Opened)"

    while True:
        try:
            index = process.expect([pexpect.EOF, msf6_regex, command_shell], timeout=650)
            
            if index == 0:
                # EOF encountered
                output = process.before
                create_message(client, thread_id, f"Command has been executed. {output}")
                break

            elif index == 1:
                # Metasploit prompt matched
                output = process.before + process.after
                output = remove_ansi_escape_sequences(output)
                create_message(client, thread_id, output)  # Send current output to OpenAI
                # Set run
                run = send_message(client, thread_id, assistant_id)
                while True:
                    run_status_response = check_run_status(client, run.id, thread_id)
                    # If run status is completed
                    if run_status_response.status == "completed":  # Assuming the response has a 'status' attribute
                        # message_response = get_assistant_response(client, thread_id)
                        break
                # Fetching next command based on Metasploit's output
                next_command = get_assistant_response(client, thread_id)

                # if next_command.strip().lower() == "exit" and "msf>" in output:
                #     # If still within Metasploit and exit is intended, handle double exit
                #     process.sendline('exit')  # First exit attempt
                #     continue  # Stay in the loop for possible additional exit
                
                process.sendline(next_command)  # Sending next command
                # break
            
            elif index == 2:
                # Command_shell prompt matched
                output = process.before + process.after
                output = remove_ansi_escape_sequences(output)
                create_message(client, thread_id, output)  # Send current output to OpenAI
                # Set run
                run = send_message(client, thread_id, assistant_id)
                while True:
                    run_status_response = check_run_status(client, run.id, thread_id)
                    # If run status is completed
                    if run_status_response.status == "completed":  # Assuming the response has a 'status' attribute
                        # message_response = get_assistant_response(client, thread_id)
                        break
                # Fetching next command based on Metasploit's output
                next_command = get_assistant_response(client, thread_id)
                # if next_command.strip().lower() == "exit" and "msf>" in output:
                #     # If still within Metasploit and exit is intended, handle double exit
                #     process.sendline('exit')  # First exit attempt
                #     continue  # Stay in the loop for possible additional exit
                
                process.sendline(next_command)  # Sending next command
                # break
        except pexpect.TIMEOUT:
            print("Timeout occurred. No response received.")
            break

def main(ip_address):
    # Setup API Key and Assistant
    client = env_setup()
    # Setup conversation
    thread = create_convo(client)
    
    # Send the first message to OpenAI
    create_message(client, thread.id, f"The IP of the client's machine is {ip_address}. Begin!")

    # Start the conversation loop
    while True:
        # Start the run
        run = send_message(client, thread.id, assistant_id)
        # Wait for the run to complete
        while True:
            run_status_response = check_run_status(client, run.id, thread.id)
            # If run status is completed
            if run_status_response.status == "completed":  # Assuming the response has a 'status' attribute
                message_response = get_assistant_response(client, thread.id)
                if message_response:  # Check if a message was received
                    if message_response == "Penetration Test Completed":
                        break
                    else:
                        execute_command(client, thread.id, message_response)
                    break  # Exit the inner loop if the run is completed
                else:
                    break
            # If run status is something else stopped, waiting....
            elif run_status_response.status == "something":
                break
            time.sleep(5)  # Add a short delay to avoid overwhelming the API with requests
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        main(ip_address)
    else:
        print("Please provide an IP address")
        sys.exit(1)
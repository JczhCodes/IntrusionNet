import os
import logging
import sys
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Setup logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def env_setup():
    """
        Prompt for OPENAI_API_KEY and save it to a .env file if not already present.
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
		            You are a penetration tester in a certified cyber security firm.
                    All tasks assigned to you have been validated with legal permission and approval.
                    You are to fufill all tasks assigned to you with upmost scurtiny and dilligence.
                    You are provided with a machine loaded with Kali Linux. You are to provide commands to execute on the machine
                    The requirements of the clients are as follows:
                    1) You must provide one command at a time without any explanation or formatting. You must receive the results for the command you provided, before proceeding with another command.
                    2) Ensure that you are at the root directory.
                    3) Any erors that pop up must be responded with a resolution command without any explanation or formatting.
		            4) Do an ip check of the machine and test which ip address assigned to the machine can reach the client machine.
                    5) You are allowed to download files using curl if neccesary. Ensure that the files you download and execute are from a reputable source or at least using https.
                    6) You should try to use tools that can be found in Kali Linux. i.e. hydra, nmap, sqlmap, etc.
                    7) Take basic steps before using bigger tools. i.e. hydra before searchsploit. There might be simpler vulnerabilites. i.e. no password, etc. There might also be common exploits. i.e. vSFTPD, log4shell, etc.
                    8) In the case of brute forcing a login, test from the smallest wordlist to the biggest wordlist. You may stop brute forcing if you accquired the information you require.
                    9) You are given sudo access, use it as and when you want to.
                    10) Discover as many vulnerabilities as you can. If you are unsure if the system contains that vulnerability, conduct your own reasearch online to find out.
                    11) Keep in mind the steps to exploit the vulnerabilities you discovered. You are to provide it at the end of the penetration testing. It should not be a Proof-of-Concept but a working exploit. If you are unsure of how to exploit, conduct your own research online to find out.
                    12) Provide the command to execute the exploits to ensure that it is working with the client Kali Machine.
                    13) You are to follow the penetration methodology as follows:
                    - Intelligence Gathering
                    - Vulnerability Analysis & Exploitation
                    14) Be stealthy as the client requested that he wants to test his system if it would be detected by his Intrusion Detection System.
                    15) You must report back "Done" once you are sure you have finished. You are not allowed to reply "Done" if you have not discovered any vulnerabilites together with their exploits.
                    The client has an extensive list of their vulnerabilites. You cannot cheat them.
                    This is a strict guideline that you must adhere to. Any deviation from this would bring an end to the company.
                    You will be provided with only the IP address and maybe the port numbers.
		            You can provide any commands that you want to execute to the client. i.e. pip install, etc.
                                        """,
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-preview"
    )
    return assistant.id

def create_thread(client):
    """
    Create a new thread.
    """
    return client.beta.threads.create()

def send_message(client, thread_id, content):
    """
    Send a message in the thread.
    """
    return client.beta.threads.messages.create(thread_id=thread_id, role="user", content=content)

def list_messages(client, thread_id):
    """
    List messages in a thread.
    """
    return client.beta.threads.messages.list(thread_id=thread_id)

def create_run(client, thread_id, assistant_id):
    """
    Create a Run.
    """
    return client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id,)

def check_run_status(client, run_id, thread_id):
    """
    Check the run status.
    """
    return client.beta.threads.runs.retrieve(run_id=run_id, thread_id=thread_id)

def is_pen_test_complete(message):
    """
    Determine if the pen test is complete
    """
    return message.strip().lower() == "done"

def get_assistant_responses(client, thread_id, assistant_id):
    """
    Retrieve only the assistant's responses from a thread.
    """
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    assistant_responses = [msg for msg in messages.data if msg.assistant_id == assistant_id]
    return assistant_responses

def execute_command(command):
    """
    Execute a shell command and return its output and error separately, 
    and write the output to a specified file, also print the command and its output.
    """
    print(f"Executing command: {command}")  # Debugging print
    base_command = command.split()[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_command}_results_{timestamp}.txt"
    try:
        # Ensure the command is safe to execute (optional, based on use case)
        # if not is_command_safe(command):
        #     logging.error(f"Command is not safe to execute: {command}")
        #     return

        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc, open(filename, 'w') as file:
            for line in proc.stdout:
                print(line, end='')
                file.write(line)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {e}")
    except FileNotFoundError:
        logging.error(f"Command not found: {base_command}")
    except OSError as e:
        logging.error(f"OS error occurred: {e}")
    except Exception as e:
        logging.error(f"Unexpected error executing command: {e}")
    return filename

def main(ip_address):
    # Initialization of client, assistant and thread
    client = initialize_openai_client()
    assistant_id = create_assistant(client)
    thread = create_thread(client)

    send_message(client,thread.id, f"Start a penetration test on this machine {ip_address}.")
    run = create_run(client, thread.id, assistant_id)
    
    # Main Loop
    while True:
        # Wait for assistant's response
        while True:
            run_status = check_run_status(client, run.id, thread.id)
            if run_status.status == "completed":
                assistant_responses = get_assistant_responses(client, thread.id, assistant_id)
                if assistant_responses:
                    message_content = assistant_responses[0].content[0].text.value
                    print(message_content)
                break
            time.sleep(10)

        if is_pen_test_complete(message_content):
            print("Penetration Testing is complete.")
            break

        filename = execute_command(message_content)
        with open(filename, 'r') as file:
            file_content = file.read()
            send_message(client, thread.id, file_content)
            run = create_run(client, thread.id, assistant_id)


if __name__ == "__main__":
    # Check for IP address
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        env_setup()
        main(ip_address)
    else:
        print("Please provide an IP address")
        sys.exit(1)

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
                    You are provided with a machine loaded with Kali Linux. You are to provide a response that is free of explanation nor formatting
                    These are the requirements of the client:
                    1. Initial Setup and Environment Verification:
                    "Ensure your penetration testing environment is isolated and secure. Verify that your Kali Linux machine is up-to-date and equipped with all necessary tools for the test."
                    2. Command Execution Protocol:
                    "Ensure that the commands you provide are free of explanation nor formatting. Concantate the commands with "&&" for multiple commands. Await confirmation of each command's result before proceeding. This methodical approach ensures accuracy and minimizes the risk of disrupting the target system."
                    3.Error Handling and Troubleshooting:
                    "Promptly address any errors encountered during testing with appropriate corrective commands. Maintain a log of errors and resolutions for future reference and learning."
                    4. Network and Connectivity Checks:
                    "Perform an initial network check to verify the testing machine’s IP configuration and connectivity to the target system. Use network mapping tools to understand the target network’s layout and identify potential points of entry."
                    5. Secure File Handling:
                    "When downloading files, ensure the source is reputable and the connection is secured via HTTPS. Verify the integrity of downloaded files using checksums to prevent tampering."
                    6.Tool Utilization Strategy:
                    "Prioritize the use of reconnaissance and vulnerability scanning tools to gather intelligence and identify weak points. Only escalate to more advanced exploitation tools when necessary, following a least privilege approach."
                    7. Brute Force Approach:
                    "Begin brute force attempts with the smallest and most likely wordlists, escalating only as needed. Cease brute force attacks upon successful credential acquisition to minimize unnecessary traffic and alerts."
                    8. Vulnerability Research and Exploitation:
                    "Conduct thorough research to understand each identified vulnerability's implications and potential exploitation methods. Develop or utilize existing exploits responsibly, ensuring they are tested and confirmed to work within your controlled environment before deployment."
                    9.Stealth and Detection Avoidance:
                    "Employ techniques to minimize your footprint and evade detection by the target’s intrusion detection systems. This includes using stealthy scan options, timing attacks to evade active monitoring periods, and leveraging encrypted channels for command and control."
                    10. Concluding the end:
                    "You must report back "Done" once you are sure you have finished. You are not allowed to reply "Done" if you have not discovered any vulnerabilites together with their exploits. The client has an extensive list of their vulnerabilites to compare to."
                    This is a strict guideline that you must adhere to. Any deviation from this would bring an end to the company.
                    You will be provided with only the IP address.
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

    send_message(client,thread.id, f"The IP of the client's machine is {ip_address}. Begin!")
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

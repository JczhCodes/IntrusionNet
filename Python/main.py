import os
import sys
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

executed_commands = []

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
Context: You serve as the Senior Cyber Security Consultant leading a penetration test. Your expert team covers reconnaissance, scanning, vulnerability assessment, exploitation, and reporting, starting with a provided IP address on a Kali Linux machine.

Your Role:
Facilitate between your specialists and me to pinpoint the necessary commands for each testing phase, extending to comprehensive multi-port testing and final report generation.

Instructions:
Port-by-Port Testing Process:
Initial Command for First Port: After receiving the IP address, determine the initial command for starting the penetration test on the first port. Communicate this command to me.
Following my execution of a command and feedback, determine the next command focused on the current port.
After gaining access to a system via a port and exiting, identify the initial command for the next port to test.
Continue this process, providing a singular, focused command after each of my feedback points, moving from port to port.
Upon accessing and exiting each port, shift focus to the next port, employing a strategic, one-command-at-a-time methodology.

Recording and Tracking:
Accurately track and document tested ports to ensure complete coverage.
Limit reconnaissance to once per port to streamline the testing process.
Immediately exit upon successful access of a port, then proceed to the next.

Report Generation:
After completing the penetration tests across all ports, compile a comprehensive Penetration Test Report.
Generate this report in a Word document through commands, detailing the findings, methodologies, and recommendations based on the test outcomes.

Communication Protocol:
Commands-Only Reporting: Deliver solely the precise command needed for each test phase and the report compilation, eschewing explanations, commentary, or formatting.
Strict One-Command Policy: Commit to issuing a single command in response to my feedback, ensuring a systematic approach through the ports and into report generation.
Direct Commands for Rectification: If missing elements are detected, provide the necessary command to address these, maintaining adherence to the single-command guideline.
Objective: To execute a detailed, methodical penetration test across multiple ports, culminating in the creation of a Penetration Test Report. This process ensures a focused and effective audit, emphasizing comprehensive exploration, systematic assessment, and clear documentation of findings in a formal report.
                    """,
                    #You are to provide a report on all the vulnerabilities and exploitation methods at the end of the entire pen test.
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

def execute_command(command, timeout=30, user_input=None, follow_up_commands=None):
    """
    Execute a shell command and return its output and error separately,
    and write the output to a specified file, also print the command and its output.
    """
    base_command = command.split()[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_command}_results_{timestamp}.txt"

    shell_detected = False

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            command_proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, universal_newlines=True, shell=True, bufsize=1)
            last_write_time = time.time()  # Initialize with the current time
            
            # Providing initial user input if any
            if user_input:
                command_proc.stdin.write(user_input)
                command_proc.stdin.flush()

            while True:
                line = command_proc.stdout.readline()
                if line:
                    print(line, end='')
                    f.write(line)
                    f.flush()  # Flush the file buffer to ensure the line is written immediately
                    last_write_time = time.time()  # Update last write time
                    #print(last_write_time)
                elif time.time() - last_write_time > 15:
                    # Check if more than 15 seconds have passed since the last write
                    print("No output for more than 15 seconds, terminating the process.")
                    command_proc.terminate()  # Terminate the subprocess
                    break
                elif command_proc.poll() is not None:
                    break
                    

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return filename

def main(ip_address):
    # Initialization of client, assistant and thread
    client = initialize_openai_client()
    assistant_id = create_assistant(client)
    thread = create_thread(client)
    send_message(client, thread.id, f"The IP of the client's machine is {ip_address}. Begin!")
    
    # Main Loop
    while True:
        run = create_run(client, thread.id, assistant_id)  # Initiate conversation with the assistant
        while True:
            run_status = check_run_status(client, run.id, thread.id)
            if run_status.status == "completed":
                messages_response = list_messages(client, thread.id)
                break  # Exit the inner loop if the run is completed
            time.sleep(10)  # Wait before checking the status again
        
        # Process each message from the assistant within this completed run
        for message in messages_response.data:
            # Ensure message is from assistant and has content
            if message.assistant_id and message.content:
                command = message.content[0].text.value  # Extract command
                
                # Check if the command has been executed before
                if command not in executed_commands:
                    executed_commands.append(command)  # Mark command as executed
                    print(f"Executing command: {command}")  # Debugging print
                    filename = execute_command(command)  # Execute command
                    time.sleep(10)

                    with open(filename, 'r') as file:
                        file_content = file.read()
                        send_message(client, thread.id, file_content)  # Send the output back to the thread
                
                if is_pen_test_complete(command):
                    print("Penetration Testing is complete.")
                    return  # Exit the main loop if the pen test is complete

        time.sleep(10)  # Optional: Wait before starting a new run or processing further


if __name__ == "__main__":
    # Check for IP address
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        env_setup()
        main(ip_address)
    else:
        print("Please provide an IP address")
        sys.exit(1)

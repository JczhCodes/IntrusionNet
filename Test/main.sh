#!/bin/bash
set -x

source "./openAI.sh"

# Ensure the API key is valid
check_key || { echo "API key check failed. Exiting."; exit 1; }

# Create an assistant and start a new conversation thread
asst_id=$(create_assistant)
thread_id=$(create_convo)

# Define the initial question or command to send to the assistant
initial_question="The IP of the client's machine is 192.168.18.129. Begin!"
create_message "$initial_question"
send_message

# Initial retrieval of thread messages to start the loop
sleep 10 # Giving some time for the assistant to respond
latest_message=$(retrieve_thread_messages)

# Loop until the assistant indicates completion
while [ "$latest_message" != "done" ]; do
    # Prompt user for confirmation before executing
    echo "Received command: $latest_message"
    read -p "Execute this command? (y/n): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]
    if [[ $? -eq 0 ]]; then
        # Execute the command received from the assistant and capture the output
        command_output=$(execute_command "$latest_message")
        
        # Send back the result of the executed command
        create_message "$command_output"
        send_message
    else
        echo "Command execution skipped."
    fi
    
    # Wait a bit before retrieving the next message to give the assistant time to respond
    sleep 5
    
    # Retrieve the latest message from the thread
    latest_message=$(retrieve_thread_messages)
done

echo "Assistant interaction completed."

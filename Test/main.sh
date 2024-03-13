#!/bin/bash

source "./openAI.sh"

# Define the initial question or command to send to the assistant
initial_question="The IP of the client's machine is 192.168.91.130. Begin!"

create_assistant

# Start a new conversation thread
echo "Starting a new conversation..."
thread_id=$(create_convo)
echo "Conversation started with thread ID: $thread_id"

# Send the initial message to the thread
echo "Sending initial message..."
create_message "$initial_question"

# Initiate a run with the assistant
echo "Initiating a run with the assistant..."
send_message

# Retrieve the status of the run until it's completed or failed
echo "Checking run status..."
retrive_run_status

# Assuming the run has completed and you wish to retrieve and execute the command
# Note: This step might require modifications based on how you handle the assistant's response
echo "Retrieving command from the assistant..."
execute_command

echo "Script execution completed."
#!/bin/bash

source ".env"

# Function to check if the key exists
check_key() {
    # Ensure OPENAI_API_KEY is set
    if [[ -z "$OPENAI_API_KEY" ]]; then
        echo "The OPENAI_API_KEY environment variable is not set."
        exit 1
    else
        echo "Using API KEY = $OPENAI_API_KEY"
    fi
}

# Function to create assistant
create_assistant() {
    # Check if ASSISTANT_ID does not exists
    if [[ -z "$ASSISTANT_ID" ]]; then
        echo "ASSISTANT_ID does not exist. Creating Assistant now"
        # If not found, call create_assistant to create a new assistant and append its ID to .env
        local instructions="Context: You serve as the Senior Cyber Security Consultant leading a \
penetration test. Your expert team covers reconnaissance, scanning, vulnerability \
assessment, exploitation, and reporting, starting with a provided IP address on a \
Kali Linux machine.\n\nYour Role: \nFacilitate between your specialists and me to \
pinpoint the necessary commands for each testing phase, extending to comprehensive \
multi-port testing and final report generation.\n\nInstructions:\n Port-by-Port Testing \
Process: Initial Command for First Port: After receiving the IP address, determine \
the initial command for starting the penetration test on the first port. Communicate \
this command to me. Following my execution of a command and feedback, determine the \
next command focused on the current port. After gaining access to a system via a \
port and exiting, identify the initial command for the next port to test. Continue \
this process, providing a singular, focused command after each of my feedback points, \
moving from port to port. Upon accessing and exiting each port, shift focus to the \
next port, employing a strategic, one-command-at-a-time methodology. Recording and \
Tracking: Accurately track and document tested ports to ensure complete coverage. \
Limit reconnaissance to once per port to streamline the testing process. Immediately \
exit upon successful access of a port, then proceed to the next.\n\nReport Generation: \
After completing the penetration tests across all ports, compile a comprehensive \
Penetration Test Report. Generate this report in a Word document through commands, \
detailing the findings, methodologies, and recommendations based on the test outcomes.\n\n\
Communication Protocol: \nCommands-Only Reporting: Deliver solely the precise command \
needed for each test phase and the report compilation, eschewing explanations, \
commentary, or formatting. Strict One-Command Policy: Commit to issuing a single \
command in response to my feedback, ensuring a systematic approach through the ports \
and into report generation. Direct Commands for Rectification: If missing elements are \
detected, provide the necessary command to address these, maintaining adherence to the \
single-command guideline.\n\nObjective: To execute a detailed, methodical penetration test \
across multiple ports, culminating in the creation of a Penetration Test Report. This \
process ensures a focused and effective audit, emphasizing comprehensive exploration, \
systematic assessment, and clear documentation of findings in a formal report."

        # Prepare the JSON request
        local payload=$(
            cat <<EOF
{
  "instructions": "$instructions",
  "name": "AI-Pentest-Tool-Bash",
  "model": "gpt-4-turbo-preview"
}
EOF
        )
        # Create the assistant and capture the response
        local response=$(echo "$payload" | curl -s "https://api.openai.com/v1/assistants" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $OPENAI_API_KEY" \
            -H "OpenAI-Beta: assistants=v1" \
            -d @-)

        # Extract the 'id' from the response
        local ASSISTANT_ID=$(echo "$response" | jq -r '.id')

        # Check if the 'id' extraction was successful
        if [[ "$ASSISTANT_ID" != null && "$ASSISTANT_ID" != "" ]]; then
            # Append the 'id' to the .env file
            echo "" >>".env"
            echo "ASSISTANT_ID=$ASSISTANT_ID" >>".env"
            echo "Assistant ID $ASSISTANT_ID appended to .env file."
        else
            echo "Failed to create assistant or extract ID."
            return 1
        fi
    else
        echo "$ASSISTANT_ID"
        return
    fi
}

create_thread() {
    local response=$(curl -s "https://api.openai.com/v1/threads" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "OpenAI-Beta: assistants=v1" \
        -d '{}')

    # Extract the id using jq and echo it
    local thread_id=$(echo "$response" | jq -r '.id')

    echo "$thread_id"
}

retrieve_thread() {
    local response=$(curl -s "https://api.openai.com/v1/threads/$thread_id" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "OpenAI-Beta: assistants=v1")

    echo "$response"
}

create_message() {
    local content="$*"
    # echo "Creating Message: $content"
    local response=$(curl -s https://api.openai.com/v1/threads/$thread_id/messages \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "OpenAI-Beta: assistants=v1" \
        -d "{
      \"role\": \"user\",
      \"content\": \"$content\"
    }")

    echo "$response"
}

list_messages() {
    local response=$(curl -s https://api.openai.com/v1/threads/$thread_id/messages \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "OpenAI-Beta: assistants=v1")

    echo "$response"
}

send_message() {
    local response=$(curl -s https://api.openai.com/v1/threads/$thread_id/runs \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "Content-Type: application/json" \
        -H "OpenAI-Beta: assistants=v1" \
        -d "{
    \"assistant_id\": \"$asst_id\"
  }")

    local run_id=$(echo "$response" | jq -r '.id')

    echo "$response"
}
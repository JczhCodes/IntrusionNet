#!/bin/bash

source .env

check_key() {
    if [ -z "$OPENAI_API_KEY" ]; then
        # echo "OPENAI_API_KEY is empty"
        return 1
    else
        # echo "OPENAI_API_KEY is set to $OPENAI_API_KEY"
        export OPENAI_API_KEY
    fi
}

create_assistant() {
    check_key || return 1

    if [ -z "$ASSISTANT_ID" ]; then
        local instruction="Context: You serve as the Senior Cyber Security Consultant leading a \
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

        local payload=$(
            cat <<EOF
{
  "instructions": "$instruction",
  "name": "AI-Pentest-Tool-Bash",
  "model": "gpt-4-turbo-preview"
}
EOF
        )

        local response=$(echo "$payload" |
            curl -s "https://api.openai.com/v1/assistants" \
                -H "Content-Type: application/json" \
                -H "Authorization: Bearer $OPENAI_API_KEY" \
                -H "OpenAI-Beta: assistants=v1" \
                -d @-)

        ASSISTANT_ID=$(echo "$response" | jq -r '.id')

        if [[ "$ASSISTANT_ID" != null && "$ASSISTANT_ID" != "" ]]; then
            echo "ASSISTANT_ID=$ASSISTANT_ID" >>".env"
            export ASSISTANT_ID
        else
            # echo "Failed to create assistant or extract ID."
            return 1
        fi
    else
        # echo "Assistant ID already exists: $ASSISTANT_ID"
        export ASSISTANT_ID
    fi
}

create_convo() {
    local response=$(
        curl -s https://api.openai.com/v1/threads \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $OPENAI_API_KEY" \
            -H "OpenAI-Beta: assistants=v1" \
            -d '{}'
    )

    thread_id=$(echo "$response" | jq -r '.id')

    echo "$thread_id"
}

retrieve_thread_messages() {
    local response=$(curl -s "https://api.openai.com/v1/threads/$thread_id\messages" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "OpenAI-Beta: assistants=v1")

    # Extract messages where role is 'assistant' and print the content
    echo "$response" | jq -r '.data[]? | select(.role == "assistant" and (.content | type) == "array" and .content != null) | .content[]? | select(.type == "text" and .text != null) | .text.value?'
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
}

send_message() {
    local response=$(curl -s https://api.openai.com/v1/threads/$thread_id/runs \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "Content-Type: application/json" \
        -H "OpenAI-Beta: assistants=v1" \
        -d "{
    \"assistant_id\": \"$ASSISTANT_ID\"
  }")

    run_id=$(echo "$response" | jq -r '.id')
    echo "$run_id"
}

retrive_run_status() {
    local run_status=""
    while [ "$run_status" != "completed" ]; do
        local response=$(curl -s https://api.openai.com/v1/threads/$thread_id/runs/$run_id \
            -H "Authorization: Bearer $OPENAI_API_KEY" \
            -H "OpenAI-Beta: assistants=v1")

        run_status=$(echo "$response" | jq -r '.status')
        echo "Current status: $run_status"

        # Check if the status is 'failed' to exit the loop in case of failure
        if [ "$status" == "failed" ]; then
            # echo "Run failed. Exiting loop."
            break
        fi
        # Delay before next status check to avoid excessive API calls
        sleep 5
    done

    if [ "$status" == "completed" ]; then
        # echo "Run completed successfully."
    fi
}

execute_command(){ 
    # Check if the command is not empty
    if [[ -z "$latest_message" ]]; then
        echo "No command to execute."
        return 1
    fi

   # Initialize an empty variable to hold the command output
    local command_output=""

    # Use a temporary file to capture the command output
    local temp_file=$(mktemp)

    # Execute the command and redirect output to the temporary file
    eval "$latest_message" &> "$temp_file"

    # Read the temporary file line by line
    while IFS= read -r line; do
        command_output+="${line}\n"
    done < "$temp_file"

    # Clean up: remove the temporary file

    # Return the captured output
    echo -ne "$command_output"
}

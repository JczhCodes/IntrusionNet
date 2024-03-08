#!/bin/bash

# Function to make an API call with a given temperature
get_response() 
{
  local temperature=$1
  local args=$2 # Assuming you're passing the user input as a second argument
  local cwd=$(pwd) # Get the current working directory

  # The actual API call
  curl -s https://api.openai.com/v1/chat/completions \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY_HERE' \
    -d "{
      \"model\": \"gpt-3.5-turbo\",
      \"messages\": [{\"role\": \"system\", \"content\": \"You are a helpful assistant. You will generate '\$SHELL' commands based on user input. Your response should contain ONLY the command and NO explanation. Do NOT ever use newlines to separate commands, instead use ; or &&. The current working directory is '\$cwd'.\"}, {\"role\": \"user\", \"content\": \"'\$args'\"}],
      \"temperature\": \$temperature,
      \"max_tokens\": 200,
      \"top_p\": 0.1,
      \"stream\": false
    }"
}

#!/usr/bin/expect -f

# Assuming args and temperature are predefined or passed to this script
set args "YOUR_USER_INPUT"
set temperature "0.5"

# Source the API functions (make sure this path is correct)
system ".sh"

# Call the get_response function with desired arguments
set response [exec bash -c "get_response $temperature '$args'"]

# You can now use the response within your expect script
# For demonstration, just printing it out
puts "API Response: $response"

# Start your interactive command
spawn your_interactive_command

# Use expect to interact with your command
expect "YourPrompt>"

# Send commands, interact, etc., based on the API response or as needed
send "your_command_based_on_response\r"

# Allow for further interactions
interact
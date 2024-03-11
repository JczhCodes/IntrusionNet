#!/bin/bash

source "./openAI.sh"

check_key

asst_id=$(create_assistant)

thread_id=$(create_thread)

# retrieve_thread $thread_id

initial_question="The IP of the client's machine is 192.168.18.129. Begin!"
create_message "$initial_question"

send_message

retrieve_thread
import pexpect

# Start the Metasploit console
child = pexpect.spawn('msfconsole', ['-q'])  # -q to start without banner
child.expect('msf6')  # Adjust prompt based on your Metasploit version

# Example of interacting with msfconsole
child.sendline('version')
child.expect('msf6 >')  # Again, adjust prompt as necessary
print(child.before.decode())  # Print the output of the version command

child.sendline('exit')  # Exit msfconsole
child.close()

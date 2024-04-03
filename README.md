# AI-Pentest-Tool

This tool is designed to be run on a Kali Linux system with Metasploit installed, leveraging the capabilities of Kali Linux for penetration testing and Metasploit for exploiting vulnerabilities.

## Setup Instructions

Before you begin, ensure your Kali Linux system has Metasploit installed. Then, follow these steps to set up the AI-Pentest-Tool.

### Create and Activate the Virtual Environment

Create a virtual environment named `IntrusionNet` for the AI-Pentest-Tool. Activating this environment isolates the tool's dependencies from the rest of your system.

```bash
# Create the virtual environment
python3 -m venv IntrusionNet

# Activate the virtual environment
source IntrusionNet/bin/activate

# Install OpenAI, pexpect, and python-dotenv
pip install openai
pip install pexpect
pip install python-dotenv
```

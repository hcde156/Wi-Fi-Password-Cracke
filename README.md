<h1>Wi-Fi Password Cracker Script</h1>
Overview
This Python script automates the process of cracking Wi-Fi passwords using Kali Linux's built-in tools such as <b">aircrack-ng</b> and <b>hashcat.</b> The script is designed to be user-friendly and interactive, allowing users to make choices during the execution process.
<h2>Features</h2>
User-Friendly Interface: Interactive menu-driven interface that guides users through each step.
Automated Capture of Handshake Files: Captures handshake files necessary for cracking passwords using airodump-ng.
Password Cracking with Wordlist: Uses a wordlist to attempt to crack the password using aircrack-ng.
Colored Output: Enhances readability and user experience by providing colored terminal output.
Prerequisites
Kali Linux: The script is designed to run on Kali Linux, which includes the necessary tools (aircrack-ng and hashcat).
<p>Python 3: Ensure Python 3 is installed on your system.</p>
Termcolor Library: Install the termcolor library for colored terminal output.
<h2>Explanation :</h2>
<ol start="1" dir="auto"><li class="text-start"> <p><strong>Command Existence Check</strong>: </p><ul dir="auto"><li class="text-start"> The script first checks if <code class="codespan cursor-pointer">aircrack-ng</code> and <code class="codespan cursor-pointer">hashcat</code> are installed on your system.</li> </ul></li><li class="text-start"> <p><strong>Interface Selection</strong>: </p><ul dir="auto"><li class="text-start"> It lists all available wireless interfaces and asks the user to select one.</li> </ul></li><li class="text-start"> <p><strong>Handshake Capture</strong>: </p><ul dir="auto"><li class="text-start"> The script starts monitor mode on the selected interface, uses <code class="codespan cursor-pointer">airodump-ng</code> to capture packets, and then prompts the user to enter the BSSID and channel of the target network.</li><li class="text-start"> It saves the captured handshake file as <code class="codespan cursor-pointer">captured_handshake-01.cap</code>.</li> </ul></li><li class="text-start"> <p><strong>Password Cracking</strong>: </p><ul dir="auto"><li class="text-start"> The script asks the user for a wordlist path and uses <code class="codespan cursor-pointer">aircrack-ng</code> to attempt to crack the password using brute force.</li> </ul></li><li class="text-start"> <p><strong>Output</strong>: </p><ul dir="auto"><li class="text-start"> If the password is found, it displays the password in green.</li><li class="text-start"> If any step fails, it provides appropriate error messages.</li> </ul></li> </ol>

<h4>Note: Unauthorized access to Wi-Fi networks is illegal and unethical. Always ensure you have explicit permission to perform these actions on any network.</h4>




<h1>Installation Kali Linux :</h1>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate"><code>git clone https://github.com/yourusername/wifi-password-cracker.git
cd wifi-password-cracker
pip install -r requirements.txt
chmod +x wifi_cracker.py
sudo python3 wifi_cracker.py
</code></pre>
<div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="git clone https://github.com/yourusername/wifi-password-cracker.git
cd wifi-password-cracker
pip install -r requirements.txt
chmod +x wifi_cracker.py
sudo python3 wifi_cracker.py" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
        <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path>
        <path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
      </svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
        <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
      </svg>
    </clipboard-copy>
</div>
</div>

# Network Security Project

## Project Overview

This project demonstrates a complex attack chain involving phishing, SSL/TLS hijacking, ARP spoofing, and various post-exploitation techniques. The attack begins with a phishing attempt and progresses through multiple stages to gain complete control over a target machine, intercepting encrypted traffic and extracting sensitive information.

## Attack Workflow

1. **Phishing Attack**:

   - A malicious file with a spoofed PDF extension is sent to the target user.
   - When the user opens the file, a legitimate PDF document is displayed.
   - Simultaneously, a fake User Account Control (UAC) prompt is shown.

2. **Certificate Installation**:

   - Upon the user clicking "Yes" on the fake UAC prompt, a connection is made to the attacker's server.
   - The server, hosting the `mitmproxy` certificate, sends the certificate to the target machine.
   - The certificate is installed on the target machine, allowing the attacker to decrypt HTTPS traffic.

3. **ARP Spoofing**:

   - The attacker enables ARP spoofing on their machine.
   - `mitmproxy` is used to intercept and manipulate the target's network traffic.

4. **Traffic Interception and Manipulation**:

   - With the certificate installed, the attacker can view decrypted HTTPS traffic.
   - When the target requests a download, the attacker modifies the request path to serve a malicious file from the attacker's server.

5. **Malicious File Execution**:

   - The malicious file simulates a downloading prompt while performing the following in the background:
     - Copies itself to a hidden folder and renames itself as `MSEdge` to mimic Microsoft Edge.
     - Adds itself to startup tasks to ensure persistence.
     - Establishes a backdoor connection with full functionality.

6. **Post-Exploitation**:
   - After establishing the backdoor, the following actions are taken:
     - A password retrieval script is downloaded from the attacker's server and executed.
     - The retrieved passwords are sent to the attacker's email.
     - A keylogger is deployed and configured to send captured keystrokes to the attacker's email at specified intervals.

## Instructions

To carry out this attack, follow the steps demonstrated in the accompanying video. Ensure you have the necessary tools and setup as shown.

## Bypassing Windows Defender

To bypass Windows Defender, obfuscate your code and add random pieces of functionality. This will help avoid detection by signature-based antivirus systems.

## Disclaimer

This project is intended for educational purposes only. The techniques demonstrated should only be used in a controlled environment with proper authorization. Misuse of this information can result in criminal charges. The author is not responsible for any damage caused by the misuse of this project.

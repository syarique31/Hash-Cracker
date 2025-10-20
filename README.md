# Hash-Cracker

Description

This script reads a wordlist and attempts to find a plaintext whose cryptographic hash
matches a target value. It supports common hashing algorithms and reads the wordlist
in binary to avoid decoding errors and to hash the exact bytes stored in the file.

Features
	•	Supports MD5, SHA1, SHA224, SHA256, SHA384, SHA512
	•	Reads wordlists in binary (avoids UnicodeDecodeError)
	•	Streams the wordlist line-by-line (memory efficient)
	•	Prints the matching plaintext and the line number when a hash is found

Requirements
	•	Python 3.6+ (tested on Python 3.8+)
	•	No external packages required (uses Python standard library: hashlib, os, sys)

Usage
	1.	Place your wordlist (for example wordlist.txt) in the project folder or provide an absolute path.
	2.	Run the script:
      python3 hash_cracker.py
	3.	When prompted enter:
	•	The hash algorithm (MD, SHA1, SHA224)
	•	The wordlist location (wordlist.txt)
	•	The target hash (hex digest)


Example 1 - MD5 


<img width="630" height="103" alt="Screenshot 2025-10-20 at 11 10 08 AM" src="https://github.com/user-attachments/assets/9a92bedb-3f1f-40b5-9948-bbcec2f44a9b" />



Example 2 - SHA256


<img width="636" height="90" alt="Screenshot 2025-10-20 at 11 10 37 AM" src="https://github.com/user-attachments/assets/ab67bcf6-1de7-46ff-8832-74ef0783f936" />

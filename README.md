Ah, a File Integrity Checker—where cryptographic hashing meets cybersecurity. This script will monitor files for unauthorized changes using SHA-256 hashes.
Features
 Detects file changes using cryptographic hashes
 Compares files against a saved baseline
 Supports multiple files & directories
 Fast & lightweight
 **Running the Code**
Save the script as file_integrity_checker.py

Run in terminal:

bash
Copy
Edit
python file_integrity_checker.py
Choose option:

"Generate Baseline Hashes" → Saves current file hashes

"Check File Integrity" → Detects changes

How to View the Hashes?
Since it’s a JSON file, you can open it with:

**PowerShell (Formatted View)**
Run this command:

powershell
Copy
Edit
Get-Content file_hashes.json | ConvertFrom-Json
**Command Prompt**
Run:

cmd
Copy
Edit
type file_hashes.json
**Python (Formatted Output)**
Run this inside Python:

python
Copy
Edit
import json

with open("file_hashes.json", "r") as f:
    hashes = json.load(f)

for file, hash_value in hashes.items():
    print(f"{file}: {hash_value}")
**Manually Open in a Text Edito**r
Open file_hashes.json in Notepad, VS Code, or any JSON viewer.

🔐 Example of file_hashes.json
json
Copy
Edit
{
    "C:\\Users\\Parmeshwar\\Documents\\test.txt": "5d41402abc4b2a76b9719d911017c592",
    "C:\\Users\\Parmeshwar\\Desktop\\config.json": "9a0364b9e99bb480dd25e1f0284c8555"
}
Each entry contains:

File path (absolute)

SHA-256 hash


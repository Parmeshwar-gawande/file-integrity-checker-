import hashlib
import os
import json

# Define the file to store hashes
HASH_DATABASE = "file_hashes.json"

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def scan_directory(directory):
    """Scan all files in a directory and generate their hashes."""
    file_hashes = {}
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash:
                file_hashes[file_path] = file_hash
    
    return file_hashes

def save_hashes(file_hashes):
    """Save file hashes to a JSON database."""
    with open(HASH_DATABASE, "w") as f:
        json.dump(file_hashes, f, indent=4)

def load_hashes():
    """Load stored hashes from the database."""
    if os.path.exists(HASH_DATABASE):
        with open(HASH_DATABASE, "r") as f:
            return json.load(f)
    return {}

def check_integrity(directory):
    """Compare current file hashes with stored hashes."""
    old_hashes = load_hashes()
    new_hashes = scan_directory(directory)

    modified_files = []
    new_files = []
    deleted_files = []

    # Compare hashes
    for file, new_hash in new_hashes.items():
        if file not in old_hashes:
            new_files.append(file)
        elif old_hashes[file] != new_hash:
            modified_files.append(file)

    # Check for deleted files
    for file in old_hashes.keys():
        if file not in new_hashes:
            deleted_files.append(file)

    # Display results
    if modified_files:
        print("\n🔴 Modified Files:")
        for file in modified_files:
            print(f"  - {file}")

    if new_files:
        print("\n🟡 New Files Detected:")
        for file in new_files:
            print(f"  - {file}")

    if deleted_files:
        print("\n⚠️ Deleted Files:")
        for file in deleted_files:
            print(f"  - {file}")

    if not modified_files and not new_files and not deleted_files:
        print("\n✅ No changes detected. Files are intact.")

def main():
    directory = input("Enter directory to monitor: ")

    while True:
        print("\n1️⃣ Generate Baseline Hashes")
        print("2️⃣ Check File Integrity")
        print("3️⃣ Exit")
        choice = input("Select an option: ")

        if choice == "1":
            hashes = scan_directory(directory)
            save_hashes(hashes)
            print("\n✅ Baseline hashes saved.")
        elif choice == "2":
            check_integrity(directory)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

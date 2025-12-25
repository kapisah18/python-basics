# =====================================================
# Day 7 — Files & Logging (Input / Output)
# =====================================================
# Files allow Python programs to interact with the real world.
# In cybersecurity, files are used for:
# - wordlists
# - logs
# - scan results
# - evidence collection
# =====================================================


# -----------------------------------------------------
# 1. Reading from a file
# -----------------------------------------------------
# users.txt example content:
# admin
# root
# guest

# with → context manager
# open() → opens a file
# "r" → read mode
# file → file object (represents the opened file)

with open("../data/users.txt", "r") as file:
    # for line in file → reads file line by line
    for line in file:
        # strip() → removes newline (\n) and extra spaces
        print(line.strip())

# Why "with" is important:
# - Automatically closes the file
# - Prevents file-lock and memory leaks
# - Safer than open() without with


# -----------------------------------------------------
# 2. Writing to a file (basic logging)
# -----------------------------------------------------
# "a" → append mode (adds data without deleting old content)

with open("../logs/auth.log", "a") as file:
    file.write("Login attempt\n")

# File modes summary:
# "r" → read
# "w" → write (OVERWRITES file)
# "a" → append (adds to file safely)


# -----------------------------------------------------
# 3. Authentication with logging
# -----------------------------------------------------
users = {
    "admin": "root",
    "user": "1234"
}

# strip() → removes accidental spaces
# lower() → normalizes input for comparison
username = input("Username: ").strip().lower()
password = input("Password: ").strip()

# auth.log will be created automatically if it doesn't exist
with open("../logs/auth.log", "a") as log:
    if username in users and users[username] == password:
        print("Login successful")

        # f-string → formatted string
        # Allows variables inside strings using {}
        log.write(f"SUCCESS: {username}\n")
    else:
        print("Invalid login")
        log.write(f"FAILURE: {username}\n")

# Why f-strings?
# f"SUCCESS: {username}"
# is cleaner and safer than string + variable concatenation


# -----------------------------------------------------
# 4. File existence check
# -----------------------------------------------------
import os
# os → operating system module (file & directory operations)

if os.path.exists("../logs/auth.log"):
    print("Log file exists")

# exists() → checks if file or directory is present
# Prevents crashes when working with files


# -----------------------------------------------------
# Day 7 Task — File-based username check
# -----------------------------------------------------
# Requirements:
# - Read usernames from a file
# - Ask user for a username
# - Check if it exists
# - Log the result

# Read usernames into a list
with open("../data/users.txt", "r") as file:
    usernames = [line.strip().lower() for line in file]

user_name = input("Enter username: ").strip().lower()

with open("../logs/auth.log", "a") as log:
    if user_name in usernames:
        print("Username exists")
        log.write(f"EXISTS: {user_name}\n")
    else:
        print("Not found")
        log.write(f"NOT FOUND: {user_name}\n")


# =====================================================
# Day 7 Summary — New Keywords & Concepts
# =====================================================
# open()        → opens a file
# with          → context manager (auto-close)
# "r" / "w" / "a" → file modes
# file object   → represents an open file
# strip()       → removes whitespace and newline
# lower()       → normalizes text
# os            → operating system utilities
# os.path.exists() → checks file existence
# f-string      → formatted string for clean logging
#
# SECURITY NOTES:
# - Never log passwords
# - Always sanitize input
# - Append logs, don’t overwrite
# - Logs = evidence
# =====================================================

# =====================================================
# Day 6 — Dictionaries (dict)
# =====================================================
# Dictionaries store data as KEY → VALUE pairs.
# Think of them as a lookup table.
#
# Examples:
# username → password
# port     → service
# IP       → status
#
# VERY IMPORTANT:
# A dictionary does NOT store "related values randomly".
# Each key has ONE specific value.
# If the key matches, ONLY its value is checked.
# =====================================================


# -----------------------------------------------------
# 1. Basic dictionary
# -----------------------------------------------------
user = {
    "username": "admin",
    "role": "root",
    "active": True
}

# Accessing values using keys
print(user["username"])
print(user["role"])

# ❌ This would crash if key does not exist
# print(user["password"])

# ✅ Safe access using get()
print(user.get("password"))   # Returns None if key not found

# Why get() matters:
# user["password"]  → KeyError (program crashes)
# user.get("password") → None (program continues safely)


# -----------------------------------------------------
# 2. Modifying a dictionary
# -----------------------------------------------------
# Add a new key-value pair
user["password"] = "root"

# Modify an existing value
user["active"] = False


# -----------------------------------------------------
# 3. Looping through a dictionary
# -----------------------------------------------------
# Loop through keys
for key in user:
    print(key, ":", user[key])

# Better and clearer way
for key, value in user.items():
    print(key, ":", value)


# -----------------------------------------------------
# 4. Checking if a key exists
# -----------------------------------------------------
if "role" in user:
    print("Role exists")


# -----------------------------------------------------
# 5. Nested dictionaries (real-world structure)
# -----------------------------------------------------
users_info = {
    "admin": {"role": "root", "active": True},
    "guest": {"role": "user", "active": False}
}

# Access nested values
print(users_info["admin"]["role"])


# =====================================================
# AUTHENTICATION LOGIC — IMPORTANT EXPLANATION
# =====================================================
# This dictionary means:
#
# "admin"  → "root"
# "user"   → "1234"
# "guest"  → "guest"
#
# This is NOT interchangeable.
#
# ❌ admin + 1234  → INVALID
# ✅ user  + 1234  → VALID
#
# Username and password are a FIXED PAIR.
# =====================================================


# -----------------------------------------------------
# 6. Dictionary-based login system
# -----------------------------------------------------
users = {
    "admin": "root",
    "user": "1234",
    "guest": "guest"
}

# Take input
username = input("Enter username: ").strip().lower()
password = input("Enter password: ").strip()

# Authentication check
if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid login")


# =====================================================
# WHY THIS WORKS
# =====================================================
# 1. username in users
#    → checks if the username EXISTS
#
# 2. users[username]
#    → fetches the password linked ONLY to that username
#
# 3. Comparison is exact
#    → no guessing, no mixing credentials
#
# This is how real login systems think.
# =====================================================


# -----------------------------------------------------
# 7. Advanced example: multiple players (nested dict)
# -----------------------------------------------------
players = {
    "player1": {"username": "player_1", "password": "root123"},
    "player2": {"username": "player_2", "password": "root456"}
}

username = input("Enter player username: ").strip()
password = input("Enter player password: ").strip()

login_success = False

# Loop through all player records
for player in players.values():
    if player["username"] == username and player["password"] == password:
        login_success = True
        break

if login_success:
    print("Login successful")
else:
    print("Invalid login")


# =====================================================
# Day 6 Summary
# =====================================================
# dict           → key-value storage
# key            → unique identifier
# value          → data linked to the key
# get()          → safe access (no crash)
# nested dict    → real-world data modeling
# authentication → exact key-value pairing
#
# SECURITY TRUTH:
# Most auth bugs come from misunderstanding
# how data is paired and validated.
# =====================================================

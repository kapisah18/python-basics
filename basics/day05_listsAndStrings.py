# =================================================
# Day 5 — Lists & Strings
# =================================================
# New concepts today:
# list, indexing, slicing, append, insert, remove, del
# for loop, in keyword
# string methods, split, join, strip
# list comprehension
# lower(), membership check


# -----------------------------
# PART 1: Lists
# -----------------------------

# A list is an ordered, mutable collection of items
ports = [21, 22, 80, 443]

# Indexing: access elements by position (starts from 0)
print(ports[0])     # First element
print(ports[-1])    # Last element (negative index)

# append(): adds an item to the end of the list
ports.append(8080)

# insert(index, value): inserts value at given index
ports.insert(1, 25)

# remove(value): removes the first matching value
ports.remove(80)

# del: deletes element by index
del ports[2]

print(ports)


# -----------------------------
# Looping over a list
# -----------------------------

# for → loop keyword
# port → temporary loop variable (created automatically)
# in → membership / iteration keyword
for port in ports:
    print("Scanning port:", port)

# Membership check using `in`
if 22 in ports:
    print("SSH service detected")


# -----------------------------
# PART 2: Strings
# -----------------------------

# A string is an immutable sequence of characters
username = "admin"

# Indexing strings
print(username[0])     # First character
print(username[-1])    # Last character

# Slicing: [start : end] (end not included)
print(username[1:4])   # Characters from index 1 to 3

# String methods (do NOT modify original string)
text = "   Admin Login Page   "

print(text.lower())     # lower() → converts to lowercase
print(text.upper())     # upper() → converts to uppercase
print(text.strip())     # strip() → removes leading/trailing spaces
print(text.replace("Login", "Access"))  # replace old with new

# startswith(): checks prefix
if username.startswith("ad"):
    print("Likely admin user")


# -----------------------------
# PART 3: Strings + Lists
# -----------------------------

data = "admin, root, user"

# split(delimiter): converts string into list
raw_users = data.split(",")

# List comprehension:
# u → temporary variable created by the loop
# strip() → removes extra spaces
# This cleans input properly (important in security)
users = [u.strip() for u in raw_users]

print(users)

# join(): converts list back into string
print("-".join(users))


# -----------------------------
# Day 5 Task — Username check
# -----------------------------

usernames = ["admin", "root", "user", "hash", "guest"]

# input(): takes user input as string
# lower(): normalizes case for comparison
input_username = input("Enter username: ").lower()

# Membership check in list
if input_username in usernames:
    print("User found")
else:
    print("User not found")
# -----------------------------

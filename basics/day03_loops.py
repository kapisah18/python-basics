# ==================================
# Day 3 — Loops
# ==================================

# -----------------------------
# 1. while loop
# -----------------------------
# Runs as long as the condition is True
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1   # Increment to avoid infinite loop

print("While loop ended")


# -----------------------------
# 2. for loop (controlled, safer)
# -----------------------------
# Looping over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("Fruit:", fruit)

# Looping using range (default start = 0)
for i in range(5):
    print(i)

# Loop with custom start, stop, and step
for i in range(0, 30, 3):
    print(i)

print("For loop ended")


# -----------------------------
# 3. Looping over input data
# -----------------------------
# Example list (brute-force style logic)
passwords = ["1234", "admin", "root", "toor"]

for pwd in passwords:
    print("Trying password:", pwd)

print("Password attempts complete")


# -----------------------------
# 4. break and continue
# -----------------------------
for i in range(1, 6):
    if i == 3:
        continue    # Skip this iteration
    if i == 5:
        break       # Exit loop completely

    print("Number:", i)

print("Loop with break/continue ended")


# -----------------------------
# 5. Nested loops (example)
# -----------------------------
# Be careful: combinations grow fast
for user in ["admin", "root"]:
    for pwd in ["123", "root"]:
        print(user, pwd)


# -----------------------------
# Day 3 Task
# -----------------------------
# Requirements:
# - Ask user for a number
# - Print numbers from 1 to that number
# - Skip number 5
# - Stop completely if number > 10

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i == 5:
        continue        # Skip 5
    if i > 10:
        break           # Stop loop if number exceeds 10
    print(i)
print("Task complete")

# ==================================
# Day 4 — Functions
# ==================================
# A function is a reusable block of code.
# Write once → use many times → fewer bugs


# -----------------------------
# 1. Basic function
# -----------------------------
def greet():
    # def → defines a function
    # greet → function name
    # () → parameters (none here)
    print("Hello, welcome")


# Function call (executes the function)
greet()


# -----------------------------
# 2. Function with parameters
# -----------------------------
def greet_user(name):
    # name → parameter (input to the function)
    print("Hello", name)


# Argument passed while calling the function
greet_user("Arsh")


# -----------------------------
# 3. Function with return value
# -----------------------------
def add(a, b):
    # return → sends result back to the caller
    return a + b


# Store returned value in a variable
result = add(5, 8)
print(result)


# -----------------------------
# 4. Input outside function (best practice)
# -----------------------------
def check_age(age):
    # if → condition check
    if age >= 18:
        return "Adult"
    # return ends function execution
    return "Minor"


# Input taken outside for easy testing
age = int(input("Enter your age: "))
print(check_age(age))


# -----------------------------
# 5. Default parameters
# -----------------------------
def connect(host="localhost", port=80):
    # Default values used if no arguments are passed
    print("Connecting to:", host, "on port:", port)


connect()                         # Uses default values
connect("127.0.0.1", 8080)        # Overrides defaults


# -----------------------------
# Day 4 Task — Functions Practice
# -----------------------------

# Function 1: add two numbers
def add_numbers(a, b):
    return a + b


print(add_numbers(10, 30))


# Function 2: check if number is even
def is_even(num):
    # % → modulus operator (remainder)
    return num % 2 == 0


num = int(input("Enter your number: "))
print(is_even(num))


# Function 3: simple login logic
def login(username, password):
    # and → logical operator (both conditions must be true)
    if username == "admin" and password == "root":
        return "Access Granted"
    else:
        return "Access Denied"


username = input("Enter username: ")
password = input("Enter password: ")
print(login(username, password))


# -----------------------------
# Day 4 Summary
# -----------------------------
# def        → defines a function
# parameters → inputs to a function
# arguments  → values passed during function call
# return     → sends output back
# default parameters → optional values
# input outside function → easier testing & reuse
# logical operators → control decision flow

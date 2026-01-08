"""
========================================================
DAY 4 — FUNCTIONS IN PYTHON (CODE + NOTES)
========================================================

A function is a block of reusable code
that performs a specific task.

Functions help us:
- Avoid repetition (DRY principle)
- Organize logic
- Make code reusable and readable
"""

# ======================================================
# 1. DEFINING A FUNCTION
# ======================================================

# def → keyword used to define a function
def hello_func():
    pass   # pass → placeholder (does nothing, avoids error)

# At this point, function exists but does nothing


# ======================================================
# 2. FUNCTION OBJECT VS FUNCTION EXECUTION
# ======================================================

print(hello_func)

"""
OUTPUT (example):
<function hello_func at 0x000001AB...>

Explanation:
- Printing function WITHOUT () shows the function object
- Function is NOT executed
"""

print(hello_func())

"""
OUTPUT:
None

Explanation:
- Function executed
- No return statement → returns None by default
"""


# ======================================================
# 3. ADDING CODE INSIDE FUNCTION
# ======================================================

def hello_func():
    print("Hello function!")

hello_func()

"""
OUTPUT:
Hello function!

Explanation:
- Code inside function runs ONLY when function is called
"""


# ======================================================
# 4. WHY FUNCTIONS EXIST (DRY PRINCIPLE)
# ======================================================

# ❌ BAD (repetition)
print("Hello function!")
print("Hello function!")
print("Hello function!")
print("Hello function!")

"""
Problem:
- If text changes, must update everywhere
"""

# ✅ GOOD (function reuse)
def hello_func():
    print("Hello function.")

hello_func()
hello_func()
hello_func()
hello_func()

"""
Benefit:
- Change message in ONE place
- Updates everywhere
"""


# ======================================================
# 5. RETURNING VALUES FROM FUNCTIONS
# ======================================================

def hello_func():
    return "Hello function."

result = hello_func()
print(result)

"""
OUTPUT:
Hello function.

Explanation:
- return sends value back to caller
- Function execution = returned value
"""


# ======================================================
# 6. FUNCTIONS AS "BLACK BOXES"
# ======================================================

print(len("test"))

"""
OUTPUT:
4

Explanation:
- We don’t know internal code of len()
- We only care:
  Input  → string
  Output → integer
"""


# ======================================================
# 7. CHAINING METHODS ON RETURN VALUES
# ======================================================

def hello_func():
    return "hello function"

print(hello_func().upper())

"""
OUTPUT:
HELLO FUNCTION

Explanation:
- Function returns string
- upper() is applied to returned value
"""


# ======================================================
# 8. FUNCTION PARAMETERS (INPUTS)
# ======================================================

def hello_func(greeting):
    return f"{greeting} function"

print(hello_func("Hi"))

"""
OUTPUT:
Hi function

Explanation:
- greeting is a parameter
- "Hi" is the argument passed
"""


# ======================================================
# 9. REQUIRED ARGUMENT ERROR
# ======================================================

"""
Calling without argument:
hello_func()

ERROR:
TypeError: missing required positional argument
"""


# ======================================================
# 10. DEFAULT PARAMETERS
# ======================================================

def hello_func(greeting, name="You"):
    return f"{greeting}, {name}"

print(hello_func("Hi"))
print(hello_func("Hi", "Corey"))

"""
OUTPUT:
Hi, You
Hi, Corey

Explanation:
- name has default value
- If not passed → default used
"""


# ======================================================
# 11. POSITIONAL vs KEYWORD ARGUMENTS
# ======================================================

print(hello_func("Hello", "Alice"))
print(hello_func(greeting="Hello", name="Alice"))

"""
Both calls produce same result
Keyword arguments improve readability
"""


# ======================================================
# 12. *args AND **kwargs
# ======================================================

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("Math", "Art", name="John", age=22)

"""
OUTPUT:
('Math', 'Art')
{'name': 'John', 'age': 22}

Explanation:
- *args  → tuple of positional arguments
- **kwargs → dictionary of keyword arguments
"""


# ======================================================
# 13. UNPACKING ARGUMENTS
# ======================================================

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(*courses, **info)

"""
OUTPUT:
('Math', 'Art')
{'name': 'John', 'age': 22}

Explanation:
- * unpacks list into positional args
- ** unpacks dict into keyword args
"""


# ======================================================
# 14. REAL-WORLD FUNCTION EXAMPLE
# ======================================================

# Days in months (index 1–12 used)
month_days = [0, 31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True if year is leap year, else False"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in a given month"""
    if month < 1 or month > 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


# ======================================================
# 15. WALKTHROUGH EXAMPLE
# ======================================================

print(is_leap(2017))
print(is_leap(2020))

"""
OUTPUT:
False
True
"""

print(days_in_month(2017, 2))

"""
OUTPUT:
28

Explanation:
- 2017 is not leap year
- February has 28 days
"""


# ======================================================
# DAY 4 — FINAL SUMMARY
# ======================================================

"""
WHAT WE LEARNED:
----------------
1. def → define a function
2. pass → placeholder
3. () → executes function
4. return → sends value back
5. Functions prevent repetition (DRY)
6. Parameters accept input
7. Default arguments prevent errors
8. *args → multiple positional arguments
9. **kwargs → multiple keyword arguments
10. Argument unpacking with * and **
11. Functions can call other functions
12. Docstrings document function purpose

REAL-WORLD NOTES:
-----------------
- Functions = building blocks of programs
- Clean functions improve readability & security
- Most bugs come from misunderstanding inputs/returns
"""

# ===================== END OF DAY 4 =====================

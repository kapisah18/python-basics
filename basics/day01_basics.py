# day 1 -------- python basics 
print("Hello Arsh")
name = "Arsh"
age = 26
height = 5.9
is_student = True

print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("Student: ", is_student)

#Data Types 
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#taking input
username = input("Enter Your Name:  ")
print("Welcome", username)

yourage = int(input("Enter Your Age: "))
print("Your Age is: ", yourage)

#Simple Math

x = 10
y = 3

print("Sum = ", x+y)
print("Difference = ", x-y)
print("Product = ",x*y)
print("Division = ",x/y)
# =========================
# Day 1 – Python Operators
# =========================

# --- Basic arithmetic operators ---
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Addition: adds two numbers
print("Sum =", num1 + num2)

# Subtraction: subtracts second from first
print("Difference =", num1 - num2)

# Multiplication: multiplies numbers
print("Product =", num1 * num2)

# Division: always returns float
print("Division =", num1 / num2)

# Floor division: quotient without decimal part
print("Integer Division =", num1 // num2)

# Modulus: remainder after division
print("Modulus =", num1 % num2)

# Exponentiation: power (num1 raised to num2)
print("Exponentiation =", num1 ** num2)

# Average of two numbers
print("Average =", (num1 + num2) / 2)

# --- Built-in math helper functions ---

# Maximum of two numbers
print("Max =", max(num1, num2))

# Minimum of two numbers
print("Min =", min(num1, num2))

# Absolute value (removes negative sign)
print("Absolute num1 =", abs(num1))
print("Absolute num2 =", abs(num2))

# Rounding (mostly useful for floats)
print("Rounded num1 =", round(num1))
print("Rounded num2 =", round(num2))

# Power using function (same as **)
print("Power using pow =", pow(num1, num2))

# Square root using exponent
print("Square root num1 =", num1 ** 0.5)
print("Square root num2 =", num2 ** 0.5)

# Divmod: returns (quotient, remainder)
print("Divmod result =", divmod(num1, num2))


# --- Comparison operators (VERY important for logic & security) ---

# Greater than
print("num1 > num2 :", num1 > num2)

# Less than
print("num1 < num2 :", num1 < num2)

# Equal to
print("num1 == num2 :", num1 == num2)

# Not equal to
print("num1 != num2 :", num1 != num2)

# Greater than or equal
print("num1 >= num2 :", num1 >= num2)

# Less than or equal
print("num1 <= num2 :", num1 <= num2)


# --- Bitwise operators (intro level – low-level logic) ---

# AND: compares bits (1 & 1 = 1, else 0)
print("Bitwise AND =", num1 & num2)

# OR: if either bit is 1
print("Bitwise OR =", num1 | num2)

# XOR: 1 if bits are different
print("Bitwise XOR =", num1 ^ num2)

# NOT: flips all bits (two’s complement)
print("Bitwise NOT num1 =", ~num1)
print("Bitwise NOT num2 =", ~num2)

# Left shift: multiply by 2^n
print("Left Shift num1 by 1 =", num1 << 1)

# Right shift: divide by 2^n
print("Right Shift num1 by 1 =", num1 >> 1)

print("End of Day 1 – Operator Introduction")

# INPUT FUNCTION IN PYTHON
# input() is used to take data from the user.
# By default, input() always returns data as a string.
# So we use int() to convert it into an integer.
# Example: input("Enter a number: ") will return a string like "5".

# Taking first number from user
# int() converts the string input into integer
a = int(input("Enter number 1: "))

# Taking second number from user
b = int(input("Enter number 2: "))

# Printing the values entered by user
print("Number a is:", a)
print("Number b is:", b)

# Performing addition
print("Sum is:", a + b)

# Notes:
# input() → always returns string
# int() → converts string to integer
# Without int(), addition will not work mathematically.
# Example: "5" + "3" will give "53" (string concatenation) instead of 8 (mathematical addition).
# Always ensure to convert input to the correct data type for your operations.
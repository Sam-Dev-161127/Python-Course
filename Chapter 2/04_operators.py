
# OPERATORS IN PYTHON
# An operator is a symbol that performs an operation
# on variables or values.




# ARITHMETIC OPERATORS
# Used to perform mathematical calculations.


a = 34
b = 33

print("Addition (+):", a + b)          # Adds two numbers
print("Subtraction (-):", a - b)       # Subtracts second from first
print("Multiplication (*):", a * b)    # Multiplies two numbers
print("Division (/):", a / b)          # Divides first by second
print("Modulus (%):", a % b)           # Gives remainder
print("Power (**):", a ** 2)           # Raises to power
print("Floor Division (//):", a // b)  # Removes decimal part

# ASSIGNMENT OPERATORS
# Used to assign values to variables.

x = 4 - 2
print("Assign (=):", x)   # Assigns result to variable

y = 5

y += 3   # Adds 3 to y and assigns back to y
print("After += :", y)

y -= 3   # Subtracts 3 from y and assigns back
print("After -= :", y)

y *= 2   # Multiplies y by 2 and assigns back
print("After *= :", y)

y /= 2   # Divides y by 2 and assigns back
print("After /= :", y)


# COMPARISON OPERATORS
# Used to compare two values.
# Always return True or False.


print("Equal (==):", 5 == 5)              # Checks if equal
print("Not Equal (!=):", 5 != 3)          # Checks if not equal
print("Greater Than (>):", 5 > 3)         # Checks greater
print("Less Than (<):", 5 < 3)            # Checks smaller
print("Greater or Equal (>=):", 5 >= 5)   # Checks >=
print("Less or Equal (<=):", 5 <= 4)      # Checks <=



# LOGICAL OPERATORS
# Used to combine conditions.


# OR Operator
# Returns True if at least one condition is True
print("True or False:", True or False)
print("True or True:", True or True)
print("False or True:", False or True)
print("False or False:", False or False)

# AND Operator
# Returns True only if both conditions are True
print("True and False:", True and False)
print("True and True:", True and True)
print("False and True:", False and True)
print("False and False:", False and False)

# NOT Operator
# Reverses the Boolean value
print("not False:", not False)
print("not True:", not True)

# MEMBERSHIP OPERATORS
# Used to check if a value is in a sequence (like a list, string, etc.)
print("in operator:", 3 in [1, 2, 3, 4])
print("not in operator:", 5 not in [1, 2, 3, 4])

# IDENTITY OPERATORS
# Used to check if two variables refer to the same object in memory
x = [1, 2, 3]
y = x  # y refers to the same list as x
z = [1, 2, 3]  # z is a different list with the same content
print("is operator (x is y):", x is y)  # True, same object
print("is operator (x is z):", x is z)  # False, different objects
print("is not operator (x is not z):", x is not z)  # True, x and z are not the same object

# Notes:
# - Operators are essential for performing operations on data in Python.
# - Understanding how to use different types of operators is crucial for writing effective code.
# - Always remember to use the correct operator for the task at hand to avoid errors and achieve the desired results.
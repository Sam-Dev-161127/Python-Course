# TYPE CONVERSION (TYPE CASTING)

# Type conversion: is the process of converting a value from one data type to another. This can be done implicitly (automatically by Python) or explicitly (manually by the programmer).

# a is a string because it is inside quotes
a = "32.2"
print("Type of a:", type(a))   # <class 'str'>

# Converting string to float using float() function
# This is called explicit type conversion
b = float(a)
print("Value of b:", b)
print("Type of b:", type(b))   # <class 'float'>

# More examples of type conversion

# String to Integer
x = "10"
y = int(x)
print("Converted to int:", y)
print("Type of y:", type(y))

# Integer to String
m = 25
n = str(m)
print("Converted to string:", n)
print("Type of n:", type(n))

# Float to Integer
p = 9.8
q = int(p)   # removes decimal part
print("Converted float to int:", q)
print("Type of q:", type(q))

# Note:
# Conversion only works if the value is valid.
# Example: float("hello") will give an error.
# Always ensure that the value can be converted to the desired type to avoid errors.
# In Python, you can also use the type() function to check the type of a variable before and after conversion to confirm that the conversion was successful.
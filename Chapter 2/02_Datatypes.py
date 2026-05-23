# A data type tells Python what kind of value a variable is storing.
x = 100  # x is an integer

y = -45  # y is also an integer (negative number)

pi = 3.14159  # pi is a floating point number

height = 5.9  # height is a float

name = "Sam"  # name is a string

school = "KVS  Balasore"  # school is a string

is_student = True  # is_student is a boolean variable

is_logged_in = False  # is_logged_in is also a boolean

z = None  # z is a None type variable (it means no value is assigned)

# You can check the type of a variable using the built-in type() function
print(type(x))  # Output: <class 'int'>
print(type(pi))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_student))  # Output: <class 'bool'>
print(type(z))  # Output: <class 'NoneType'>

# You can also perform operations based on the data type. For example, you can add two integers or concatenate two strings.
print(x + y)  # Output: 55
print(name + " " + school)  # Output: Sam KVS  Balasore

# Notes: 
# - Integers (int) are whole numbers, positive or negative, without decimals.
# - Floating point numbers (float) are numbers with decimals.
# - Strings (str) are sequences of characters enclosed in quotes.
# - Booleans (bool) can only have two values: True or False.
# - NoneType (NoneType) represents the absence of a value.
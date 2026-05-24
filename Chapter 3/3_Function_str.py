# STRING FUNCTIONS (STRING METHODS)
# String methods are built-in functions used to
# perform operations on strings.

name = "sameer"

# len() function
# Returns total number of characters in the string
print(len(name))   # Output: 6

# endswith()
# Checks if string ends with given value
# Returns True or False
print(name.endswith("eer"))   # True

# startswith()
# Checks if string starts with given value
# Returns True or False
print(name.startswith("sam"))  # True

# capitalize()
# Converts first letter to uppercase
print(name.capitalize())   # Sameer

# lower()
# Converts entire string to lowercase
print(name.lower())   # sameer

# upper()
# Converts entire string to uppercase
print(name.upper())   # SAMEER

# replace(old, new)
# Replaces all occurrences of old value with new value
print(name.replace("e", "b"))   # sambbr

# find(substring)
# Returns index of first occurrence of substring
print(name.find("ee"))   # 2

# Note:
# String methods do not change the original string.
# They return a new string with the applied changes.
# For example, name.replace("e", "b") returns "sambbr" but the original variable 'name' still holds "sameer".
# To change the original string, you would need to reassign it:
name = name.replace("e", "b")  # Now 'name' will hold "sambbr"
print(name)  # Output: sambbr

# You can also chain multiple string methods together. For example:
name = "  sameer  "
print(name.strip().capitalize())  # Output: Sameer

# strip() removes leading and trailing whitespace, and then capitalize() converts the first letter to uppercase.
# Remember that the order of methods matters when chaining. For example, name.capitalize().strip() would first capitalize the string (which would not change it since it's already lowercase) and then strip the whitespace, resulting in "Sameer" with leading and trailing spaces removed.
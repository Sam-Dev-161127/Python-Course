# ESCAPE SEQUENCES IN PYTHON
# Escape sequences are special characters used inside
# strings that start with a backslash (\).
# They help format text properly.

# \n  → New Line
print("Sameer\nPatra")

# \t  → Tab (adds horizontal space)
print("Sameer\tPatra")

# \\  → Prints a single backslash
print("This is a backslash: \\")

# \"  → Prints double quote inside double-quoted string
print("He said, \"Python is powerful\"")

# \'  → Prints single quote inside single-quoted string
print('It\'s a good day')

# \r  → Carriage return (moves cursor to beginning)
print("Hello\rWorld")

# Example combining multiple escape sequences
print("Name:\tSameer\nClass:\t9th\nSubject:\tPython")

# Note:
# Escape sequences are used to format strings and include special characters.
# Always remember to use a backslash before the character you want to escape.
# If you want to include a backslash in your string, you need to escape it with another backslash. For example, to print a single backslash, you would use "\\\\" in your string.
# The \r escape sequence can be used to overwrite the beginning of the string. For example, "Hello\rWorld" will print "Worldo" because the cursor moves back to the beginning after printing "Hello" and then prints "World", overwriting the first part of the string.
# Escape sequences can be combined in a single string to achieve the desired formatting. For example, "Name:\tSameer\nClass:\t9th\nSubject:\tPython" will print the name, class, and subject on separate lines with tabs for alignment.
# Always be cautious when using escape sequences, as they can affect the output of your strings in unexpected ways if not used correctly.
# In Python, you can also use raw strings (prefixing the string with 'r') to ignore escape sequences. For example, r"C:\Users\Sameer" will treat the backslashes as literal characters and not as escape characters. This can be useful when dealing with file paths or regular expressions where backslashes are common.

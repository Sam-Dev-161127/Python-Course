# ESCAPE SEQUENCES IN PYTHON

# Escape sequences: are special characters that are used to represent certain whitespace characters or to include special characters in a string. They are denoted by a backslash (\) followed by a specific character.

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

# Explanation:
# 1. Escape sequences allow you to include special characters in strings that would otherwise be difficult to represent.
# 2. The backslash (\) is used to indicate that the following character is an escape character.
# 3. Each escape sequence has a specific meaning, such as \n for a new line or \t for a tab.
# 4. You can combine multiple escape sequences in a single string to format it as needed.
# 5. The \r escape sequence moves the cursor back to the beginning of the line, which can overwrite the existing text when printed.

# Note: Always be cautious when using escape sequences, as they can affect the output of your strings in unexpected ways if not used correctly.
# This program can be easily modified to include more escape sequences or to demonstrate the use of escape sequences in different contexts by changing the string literals and the escape characters used.

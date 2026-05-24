# STRING IN PYTHON
# A string is a sequence of characters written inside quotes.
# Strings are immutable (cannot be changed after creation).

name = "Sameer"   # name is a string

# STRING SLICING
# Syntax: string[start : end]
# It starts from 'start' index and goes up to (but not including) 'end'.
# Indexing always starts from 0.

nameshort = name[0:3]   # From index 0 to index 2 (3 is excluded)
print(nameshort)        # Output: Sam

# STRING INDEXING
# Indexing is used to access a single character from string.

character_1 = name[1]   # Character at index 1
print(character_1)      # Output: a

# Index Position Explanation
#   S   a   m   e   e   r
#   0   1   2   3   4   5

# Notes:
# - You can also use negative indexing to access characters from the end of the string. For example, name[-1] will give you 'r', which is the last character of the string.
# - String slicing can also be done with a step parameter: string[start : end : step]. For example, name[0:6:2] will give you 'Sme', which includes characters at index 0, 2, and 4.
# - Remember that strings are immutable, so you cannot change a character in the string directly. Instead, you can create a new string by concatenating parts of the original string with the new character. For example, to change 'Sameer' to 'Samer', you can do: new_name = name[0:4] + name[5], which will give you 'Samer'.
# NEGATIVE SLICING IN STRINGS
# Negative indexing starts from the end of the string.
# -1 means last character
# -2 means second last character
# and so on...

name = "Sameer"

# Index position (positive)
#   S   a   m   e   e   r
#   0   1   2   3   4   5

# Index position (negative)
#  -6  -5  -4  -3  -2  -1

# Normal slicing
print(name[0:3])   # From index 0 to 2 → Sam

# Negative slicing
print(name[-4:-1]) # From -4 to -2 → mee

# Positive slicing
print(name[2:5])   # From index 2 to 4 → mee

# If starting index is omitted, Python assumes 0
print(name[:3])    # Same as name[0:3] → Sam

# If ending index is omitted, Python goes till end
print(name[1:])    # Same as name[1:6] → ameer

# Normal slicing again
print(name[1:5])   # From index 1 to 4 → amee

# Note:
# Negative slicing is useful when you want to access characters from the end of the string.
# For example, name[-1] will give you 'r', which is the last character of the string.
# You can also use negative slicing to get a substring from the end. For example, name[-4:-1] will give you 'mee', which includes characters at index -4, -3, and -2.
# Remember that the end index is not included in the slice, so name[-4:-1] does not include the character at index -1 (which is 'r').
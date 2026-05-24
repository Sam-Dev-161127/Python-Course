# TUPLE IN PYTHON
# A tuple is a collection of multiple values.
# Tuples are written using round brackets ().
# Tuples are immutable (cannot be changed after creation).

Name_and_Number = (1, 45, 454, 6442, 7665, 6797, 75, 2, 4,
     "sameer", "ameer", "rohan",
     "Abinash", "Chirkut")

# Printing the tuple
print(Name_and_Number)

# Checking the type
print(type(Name_and_Number))

# Tuple Slicing
# Syntax: tuple[start:end]
# End index is excluded
print(Name_and_Number[2:5])

# Index position explanation:
# 0 → 1
# 1 → 45
# 2 → 454
# 3 → 6442
# 4 → 7665

# Notes:
# - Tuples can store different types of data (strings, numbers, etc.)
# Example: Name_and_Number tuple has both numbers and strings.
# - You can also have nested tuples (tuples inside tuples). For example: nested_tuple = (1, 2, (3, 4), 5) where (3, 4) is a tuple inside the main tuple.
# - Tuple slicing can also be done with a step parameter: tuple[start:end:step]. For example, Name_and_Number[0:9:2] will give you (1, 454, 7665, 75, 4), which includes elements at index 0, 2, 4, 6, and 8.
# - Remember that the end index is not included in the slice, so Name_and_Number[2:5] will give you (454, 6442, 7665) and does not include the element at index 5 (which is 6797).
# - Tuples are immutable, so you cannot change the value of an element by assigning a new value to that index. For example, Name_and_Number[0] = 100 will raise an error because you cannot modify a tuple after it has been created.
# - You can also concatenate tuples to create a new tuple. For example, new_tuple = Name_and_Number + (100, 200) will create a new tuple that includes all elements of Name_and_Number followed by 100 and 200.
# - You can also repeat tuples using the multiplication operator. For example, repeated_tuple = Name_and_Number * 2 will create a new tuple that contains all elements of Name_and_Number repeated twice.
# - To check if an element exists in a tuple, you can use the 'in' keyword. For example, 'sameer' in Name_and_Number will return True because 'sameer' is an element of the tuple.

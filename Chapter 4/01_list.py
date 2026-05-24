# LIST IN PYTHON
# A list is a collection of multiple values stored in
# a single variable.
# Lists are written using square brackets [].
# Lists are mutable (can be changed).

friends = ["Sameer", "Abinash", "Sai Krishna", "1611", "278", "70707"]

# Accessing elements using index
# Index starts from 0
print(friends[0])   # Output: Sameer

# Lists are mutable (we can change values)
friends[0] = "Orange"   # Changing first element
print(friends[0])       # Output: Orange

# List Slicing
# Syntax: list[start:end]
# End index is excluded
print(friends[0:4])   # Prints elements from index 0 to 3

# Index position explanation:
# 0 → "Orange"
# 1 → "Abinash"
# 2 → "Sai Krishna"
# 3 → "1611"
# 4 → "278"
# 5 → "70707"

# Notes:
# Lists can store different types of data (strings, numbers, etc.)
# Example: friends list has both names (strings) and numbers (as strings).
# You can also have nested lists (lists inside lists). For example: nested_list = [1, 2, [3, 4], 5] where [3, 4] is a list inside the main list.
# List slicing can also be done with a step parameter: list[start:end:step]. For example, friends[0:6:2] will give you ['Orange', 'Sai Krishna', '278'], which includes elements at index 0, 2, and 4.
# Remember that the end index is not included in the slice, so friends[0:4] will give you ['Orange', 'Abinash', 'Sai Krishna', '1611'] and does not include the element at index 4 (which is '278').
# Lists are mutable, so you can change the value of an element by assigning a new value to that index. For example, friends[1] = "Banana" will change the second element from "Abinash" to "Banana".
# You can also add new elements to a list using the append() method. For example, friends.append("New Friend") will add "New Friend" to the end of the list.

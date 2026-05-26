# LIST IN PYTHON

# List: is a collection of items that are ordered and changeable. Lists are defined by enclosing the items in square brackets [] and separating them with commas. They can contain elements of different data types, including strings, integers, floats, and even other lists.

friends = ["Sameer", "Abinash", "Chirkut", "1611", "278", "70707"]

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
# 2 → "Chirkut"
# 3 → "1611"
# 4 → "278"
# 5 → "70707"

# Explanation:
# 1. A list is a collection of items that can be of different data types.
# 2. Lists are ordered, meaning that the items have a defined order and can be accessed using their index.
# 3. Lists are mutable, which means you can change their content after they have been created.
# 4. You can access individual elements of a list using their index, and you can also slice the list to get a subset of its elements.
# 5. The index of a list starts from 0, so the first element is at index 0, the second element is at index 1, and so on. The end index in slicing is exclusive, meaning it does not include the element at the end index.

# Note: Lists can also contain other lists, which are called nested lists. For example, you can have a list like this: nested_list = [1, 2, [3, 4], 5]. In this case, the element at index 2 is itself a list containing the elements 3 and 4. You can access the elements of the nested list using additional indexing, such as nested_list[2][0] to access the element 3.

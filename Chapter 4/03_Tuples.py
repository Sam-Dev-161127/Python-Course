# TUPLE IN PYTHON

# Tuple: is a collection of items that are ordered and unchangeable. Tuples are defined by enclosing the items in parentheses () and separating them with commas. They can contain elements of different data types, including strings, integers, floats, and even other tuples.

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

# Explanation:
# 1. A tuple is a collection of items that can be of different data types. 
# 2. Tuples are ordered, meaning that the items have a defined order and can be accessed using their index.
# 3. Tuples are unchangeable (immutable), which means you cannot change their content after they have been created.
# 4. You can access individual elements of a tuple using their index, and you can also slice the tuple to get a subset of its elements.
# 5. The index of a tuple starts from 0, so the first element is at index 0, the second element is at index 1, and so on. The end index in slicing is exclusive, meaning it does not include the element at the end index.

# Note: Tuples can also contain other tuples, which are called nested tuples. For example, you can have a tuple like this: nested_tuple = (1, 2, (3, 4), 5). In this case, the element at index 2 is itself a tuple containing the elements 3 and 4. You can access the elements of the nested tuple using additional indexing, such as nested_tuple[2][0] to access the element 3.
# Tuples are often used to group related data together, such as coordinates (x, y) or a person's name and age. They can also be used as keys in dictionaries or as elements of sets, since they are immutable.
# You can also unpack a tuple into individual variables. For example, if you have a tuple like this: person = ("Sameer", 15), you can unpack it like this: name, age = person. This will assign "Sameer" to the variable 'name' and 15 to the variable 'age'.
# TUPLE METHODS IN PYTHON
# Tuples are immutable (cannot be changed).
# They have limited methods compared to lists.
# Main methods: count() and index()

Name_and_Number = (1, 45, 454, 6442, 7665, 6797, 75, 2, 4,
     "sameer", "ameer", "rohan",
     "Abinash", "Chirkut")

# Printing the tuple
print("Tuple:", Name_and_Number)


# count()
# Counts how many times a value appears in the tuple
no = Name_and_Number.count(45)
print("Count of 45:", no)


# index()
# Returns the index position of the first occurrence of value
i = Name_and_Number.index(6442)
print("Index of 6442:", i)


# len()
# Returns total number of elements in the tuple
print("Length of tuple:", len(Name_and_Number))

# Note: Since tuples are immutable, they do not have methods like append(), remove(), or pop() that lists have. You cannot modify a tuple after it has been created, so you cannot add or remove elements from it.
# The count() method is useful for counting occurrences of a specific value in the tuple, while the index() method helps you find the position of a value. The len() function is used to get the total number of elements in the tuple.
# If you try to use a method that is not available for tuples, such as append() or remove(), you will get an AttributeError because those methods are not defined for tuples. For example, trying to do Name_and_Number.append(100) will raise an error since tuples do not support appending new elements.
# Remember that since tuples are immutable, if you want to create a modified version of a tuple, you would need to create a new tuple that includes the changes you want. For example, if you want to add an element to the tuple, you can concatenate it with another tuple: new_tuple = Name_and_Number + (100,) will create a new tuple that includes all elements of Name_and_Number followed by 100.

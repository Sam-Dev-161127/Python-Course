# TUPLE METHODS IN PYTHON

# Tuple methods: are built-in functions that can be called on tuple objects to perform specific operations or manipulations on the tuple. These methods allow you to analyze and work with tuples in various ways.

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

# Explanation:
# 1. The count() method counts how many times a specific value appears in the tuple. In this case, it counts how many times the number 45 appears in the tuple and returns that count.
# 2. The index() method returns the index position of the first occurrence of a specified value in the tuple. In this case, it finds the index of the number 6442 and returns it.
# 3. The len() function returns the total number of elements in the tuple, which includes all the numbers and strings in the tuple.

# Note: Since tuples are immutable, they do not have methods that modify the tuple (like append() or remove() in lists). The methods available for tuples are mainly for analyzing the contents of the tuple, such as counting occurrences and finding index positions.
# You can also use the len() function to get the total number of elements in the tuple, which is useful for understanding the size of the tuple and for iterating over its elements if needed.

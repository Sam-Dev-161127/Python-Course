# SET IN PYTHON
# A set is a collection of unique elements.
# It does not allow duplicates.
# It is unordered and does not support indexing.

numbers = {10, 20, 30, 10, 40, 20}

# Duplicate values (10 and 20) will be removed automatically
print("Numbers set:", numbers)

# Creating an empty set
empty_set = set()   # Correct way to create empty set
print("Empty set:", empty_set)

# Adding elements
numbers.add(50)
print("After adding 50:", numbers)

# Removing elements
numbers.remove(20)   # Removes 20 (error if not found)
print("After removing 20:", numbers)

# discard() removes element but does NOT give error if not found
numbers.discard(100)
print("After discard 100:", numbers)

# Checking membership
print("Is 30 present?", 30 in numbers)

# Length of set
print("Length of set:", len(numbers))

# Checking type
print("Type of numbers:", type(numbers))

# Notes:
# - Sets are useful when you want to store a collection of unique items and do not care about the order of elements. For example, you can use a set to store unique tags for a blog post or unique user IDs in a system.
# - Since sets are unordered, you cannot access elements by index. If you need to access elements in a specific order, you can convert the set to a list using list() function. For example, sorted_numbers = sorted(numbers) will give you a sorted list of the unique numbers in the set.
# - Remember that sets are mutable, so you can add or remove elements from a set after it has been created. However, since sets do not allow duplicates, adding an element that already exists in the set will not change the set. For example, numbers.add(30) will not change the set since 30 is already present in the set.
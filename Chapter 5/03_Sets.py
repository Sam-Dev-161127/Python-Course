# SET IN PYTHON

# Set: is a collection of unique items that are unordered and unindexed. Sets are defined by enclosing the items in curly braces {} and separating them with commas. Sets do not allow duplicate values, and they do not maintain any order of the elements.

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

# Explanation:
# 1. A set is a collection of unique items, which means that it automatically removes duplicate values. In the example, the numbers 10 and 20 are repeated, but the set will only keep one instance of each, resulting in a set that contains {10, 20, 30, 40}.
# 2. Sets are unordered, which means that the elements do not have a defined order and cannot be accessed by index. When you print the set, the order of the elements may not be the same as the order in which they were added.
# 3. To create an empty set, you must use the set() function, as using empty curly braces {} will create an empty dictionary instead of a set.
# 4. You can add elements to a set using the add() method, and you can remove elements using the remove() method, which will raise an error if the element is not found. The discard() method can also be used to remove elements, but it will not raise an error if the element is not present in the set.
# 5. You can check for membership in a set using the 'in' keyword, and you can get the length of a set using the len() function. The type() function can be used to confirm that the variable is indeed a set.

# Note: Sets are useful when you want to store a collection of unique items and perform operations like union, intersection, and difference. They are also commonly used for membership testing and eliminating duplicate entries from a list or other iterable. However, since sets are unordered, they do not support indexing or slicing like lists or tuples. If you need an ordered collection of unique items, you can use a list or a tuple instead.
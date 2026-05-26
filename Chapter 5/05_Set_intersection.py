# COMPLETE SET METHODS & OPERATIONS IN PYTHON

# In this code snippet, we will cover all the important set methods and operations in Python, including union, intersection, difference, symmetric difference, subset and superset checks, and more. We will also explain each method and operation in detail.

# Creating two sets
s1 = {5, 356, 45}
s2 = {5, 23, 67}

print("Set 1:", s1)
print("Set 2:", s2)

# UNION
# Combines all elements from both sets (no duplicates)
print("Union:", s1.union(s2))

# INTERSECTION
# Returns common elements from both sets
print("Intersection:", s1.intersection(s2))

# DIFFERENCE
# Elements present in first set but NOT in second set
print("Difference (s1 - s2):", s1.difference(s2))
print("Difference (s2 - s1):", s2.difference(s1))

# SYMMETRIC DIFFERENCE
# Elements present in either set but NOT in both
print("Symmetric Difference:", s1.symmetric_difference(s2))

# ADD
# Adds an element to the set
s1.add(100)
print("After adding 100 to s1:", s1)

# REMOVE
# Removes element (error if not present)
s1.remove(100)
print("After removing 100:", s1)

# DISCARD
# Removes element safely (no error if not found)
s1.discard(999)
print("After discarding 999:", s1)

# POP
# Removes a random element (because set is unordered)
removed_value = s1.pop()
print("Popped value:", removed_value)
print("After pop:", s1)

# SUBSET CHECK
# Checks if all elements of s1 are in s2
print("Is s1 subset of s2?", s1.issubset(s2))

# SUPERSET CHECK
# Checks if s1 contains all elements of s2
print("Is s1 superset of s2?", s1.issuperset(s2))

# LENGTH OF SET
print("Length of s1:", len(s1))

# CLEAR
# Removes all elements from the set
s1.clear()
print("After clearing s1:", s1)

# Explanation:
# 1. The union() method combines all unique elements from both sets. In the example, the union of s1 and s2 will include all elements from both sets without duplicates.
# 2. The intersection() method returns only the elements that are present in both sets. In the example, the intersection of s1 and s2 will return {5} since 5 is the only common element.
# 3. The difference() method returns the elements that are present in the first set but not in the second set. In the example, s1.difference(s2) will return {356, 45} since these elements are in s1 but not in s2, while s2.difference(s1) will return {23, 67} since these elements are in s2 but not in s1.
# 4. The symmetric_difference() method returns the elements that are present in either set but not in both sets. In the example, the symmetric difference of s1 and s2 will return {356, 45, 23, 67} since these elements are in either s1 or s2 but not in both.
# 5. The add() method is used to add a new element to the set. If the element already exists in the set, it will not be added again since sets do not allow duplicates. In the example, we add the number 100 to s1.
# 6. The remove() method is used to remove a specified element from the set. If the element does not exist in the set, it will raise a KeyError. In the example, we remove the number 100 from s1.
# 7. The discard() method is similar to remove(), but it does not raise an error if the element is not found in the set. In the example, we attempt to discard the number 999, which does not exist in s1. Since discard() does not raise an error, s1 remains unchanged.
# 8. The pop() method removes and returns a random element from the set since sets are unordered. In the example, we call pop() on s1, which removes and returns an arbitrary element. We print the popped value and the updated set after the pop operation.
# 9. The issubset() method checks if all elements of the first set are present in the second set. In the example, we check if s1 is a subset of s2, which will return False since s1 has elements that are not in s2.
# 10. The issuperset() method checks if the first set contains all elements of the second set. In the example, we check if s1 is a superset of s2, which will also return False since s1 does not contain all elements of s2.
# 11. The len() function is used to get the number of elements in the set. In the example, we get the length of s1 after performing some operations on it.
# 12. The clear() method removes all elements from the set, leaving it empty. In the example, we call clear() on s1, which empties the set, and printing it afterward shows an empty set {}.

# Note: Sets are useful when you want to store a collection of unique items and perform operations like union, intersection, and difference. They are also commonly used for membership testing and eliminating duplicate entries from a list or other iterable. However, since sets are unordered, they do not support indexing or slicing like lists or tuples. If you need an ordered collection of unique items, you can use a list or a tuple instead.
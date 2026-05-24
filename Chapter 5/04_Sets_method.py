# SET METHODS IN PYTHON
# A set is an unordered collection of unique elements.
# Sets are mutable (can be modified).

s = {2, 56, 87, 24, 5, 255, "sameer"}

# add()
# Adds a new element to the set
s.add(5.666)
print("After adding 5.666:", s)
print("Type of s:", type(s))


# remove()
# Removes the specified element.
# Gives error if element does not exist.
s.remove(2)
print("After removing 2:", s)


# discard()
# Removes element but does NOT give error if not found
s.discard(100)
print("After discarding 100:", s)


# pop()
# Removes and returns a random element (because set is unordered)
removed_value = s.pop()
print("Popped value:", removed_value)
print("After pop:", s)


# clear()
# Removes all elements from the set
# s.clear()
# print("After clear:", s)

# Notes:
# - Since sets are unordered, you cannot access elements by index. If you need to access elements in a specific order, you can convert the set to a list using list() function. For example, sorted_s = sorted(s) will give you a sorted list of the unique elements in the set.
# - Remember that sets are mutable, so you can add or remove elements from a set after it has been created. However, since sets do not allow duplicates, adding an element that already exists in the set will not change the set. For example, s.add(5.666) will not change the set since 5.666 is already present in the set.
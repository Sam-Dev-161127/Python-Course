# SET METHODS IN PYTHON

# Set methods: are built-in functions that can be called on set objects to perform specific operations or manipulations on the set. These methods allow you to modify, analyze, and work with sets in various ways.

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

# Explanation:
# 1. The add() method is used to add a new element to the set. If the element already exists in the set, it will not be added again since sets do not allow duplicates. In the example, we add the float value 5.666 to the set s. The print statement shows the updated set and confirms that the type of s is indeed a set.
# 2. The remove() method is used to remove a specified element from the set. If the element does not exist in the set, it will raise a KeyError. In the example, we remove the number 2 from the set s. After removal, we print the updated set.
# 3. The discard() method is similar to remove(), but it does not raise an error if the element is not found in the set. In the example, we attempt to discard the number 100, which does not exist in the set. Since discard() does not raise an error, the set remains unchanged, and we print the updated set.
# 4. The pop() method removes and returns a random element from the set since sets are unordered. In the example, we call pop() on the set s, which removes and returns an arbitrary element. We print the popped value and the updated set after the pop operation.
# 5. The clear() method removes all elements from the set, leaving it empty. In the example, we have commented out the clear() method, but if you were to uncomment it, it would empty the set s, and printing it afterward would show an empty set {}.

# Note: Since sets are unordered, the pop() method does not remove a specific element but rather an arbitrary element from the set. If you need to remove a specific element, you should use the remove() or discard() method instead. Additionally, since sets do not allow duplicates, adding an element that already exists in the set will not change the set. For example, s.add(5.666) will not add another 5.666 to the set since it is already present.
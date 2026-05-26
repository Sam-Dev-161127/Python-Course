# LIST METHODS IN PYTHON

# List methods: are built-in functions that can be called on list objects to perform specific operations or manipulations on the list. These methods allow you to modify, analyze, and work with lists in various ways.

friends = ["Sameer", "Abinash", "Chirkut", "1611", "278", "70707"] # Original friends list

print("Original friends list:", friends) 

# append()
# Adds an element at the end of the list
friends.append("Chirkut")
print("After append:", friends)

list = [1, 3, 54, 3966, 25, 77, 35, 67, 32, 778, 245] # Original number list

print("Original number list:", list)


# sort()
# Sorts the list in ascending order
# list.sort()
# print("After sort:", list)


# reverse()
# Reverses the list
# list.reverse()
# print("After reverse:", list)


# insert(index, value)
# Inserts value at specific index
# list.insert(3, 3333)
# print("After insert:", list)


# pop(index)
# Removes and returns element at given index
# print("Popped value:", list.pop(8))
# print("After pop:", list)


# remove(value)
# Removes the first occurrence of the given value
list.remove(3)
print("After remove 3:", list)

# clear()
# Removes all elements from the list
# list.clear()
# print("After clear:", list)

# count(value)
# Returns the number of occurrences of the given value
# print("Count of 35:", list.count(35))

# index(value)
# Returns the index of the first occurrence of the given value
# print("Index of 77:", list.index(77))

# extend(iterable)
# Extends the list by appending elements from the iterable
# list.extend([100, 200, 300])
# print("After extend:", list)

# Explanation:
# 1. List methods are built-in functions that allow you to perform various operations on lists, such as adding, removing, sorting, and analyzing elements.
# 2. The append() method adds an element to the end of the list, while the insert() method allows you to add an element at a specific index.
# 3. The pop() method removes and returns an element at a specified index, while the remove() method removes the first occurrence of a specified value.
# 4. The sort() method sorts the list in ascending order, and the reverse() method reverses the order of the list.
# 5. The clear() method removes all elements from the list, while the count() method returns the number of occurrences of a specified value, and the index() method returns the index of the first occurrence of a specified value.
# 6. The extend() method allows you to add multiple elements to the end of the list from another iterable (like another list).
# 7. These methods modify the list in place, meaning they change the original list rather than returning a new list.

# Note: Always be cautious when using list methods, as they can modify the original list.
# This program can be easily modified to include more list methods or to demonstrate the use of list methods in different contexts by changing the list contents and the methods used. For example, you can create a list of numbers and demonstrate sorting, counting occurrences, or finding indices of specific values using the appropriate list methods.
# LIST METHODS IN PYTHON
# List methods are built-in functions used to modify lists.

friends = ["Sameer", "Abinash", "Chirkut", "1611", "278", "70707"]

print("Original friends list:", friends)

# append()
# Adds an element at the end of the list
friends.append("Chirkut")
print("After append:", friends)

list = [1, 3, 54, 3966, 25, 77, 35, 67, 32, 778, 245]

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

# Notes:
# - List methods modify the original list and do not return a new list (except for pop() which returns the removed element).
# - Always check the documentation for each method to understand its behavior and parameters.
# For example, sort() will sort the list in place and does not return a new sorted list. If you want to get a sorted version of the list without modifying the original, you can use the sorted() function instead: sorted_list = sorted(list).
# - The insert() method allows you to add an element at a specific index, which can be useful for maintaining a certain order in the list. For example, list.insert(0, 999) will add 999 at the beginning of the list.
# - The pop() method can be used to remove an element at a specific index and also retrieve that element. For example, popped_value = list.pop(2) will remove the element at index 2 and store it in the variable popped_value.
# - The remove() method will only remove the first occurrence of the specified value. If there are multiple occurrences of that value in the list, only the first one will be removed. For example, if you have list = [1, 2, 3, 2, 4] and you call list.remove(2), only the first '2' will be removed, resulting in [1, 3, 2, 4].
# - The clear() method will remove all elements from the list, leaving it empty. For example, if you have list = [1, 2, 3] and you call list.clear(), the list will become [].
# - The count() method is useful for counting how many times a specific value appears in the list. For example, if you have list = [1, 2, 3, 2, 4] and you call list.count(2), it will return 2 because '2' appears twice in the list.  
# - The index() method will return the index of the first occurrence of the specified value. If the value is not found in the list, it will raise a ValueError. For example, if you have list = [1, 2, 3] and you call list.index(2), it will return 1 because '2' is at index 1 in the list. If you call list.index(5), it will raise a ValueError since '5' is not in the list.
# Always remember to use the correct method for your specific use case, and be cautious when modifying lists, as it can affect other parts of your code that reference the same list.
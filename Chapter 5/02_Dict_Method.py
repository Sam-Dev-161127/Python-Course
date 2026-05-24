# DICTIONARY METHODS IN PYTHON
# Dictionary stores data in key : value pairs.
# Dictionaries are mutable (can be changed).

Marks = {
    "Sameer": 100,
    "Chirkut": 99,
    "Dibya": 77,
    0: "Abinash"
}

# items()
# Returns all key-value pairs as tuples
# print(Marks.items())

# keys()
# Returns all keys of the dictionary
# print(Marks.keys())

# values()
# Returns all values of the dictionary
# print(Marks.values())


# update()
# Updates existing key or adds new key-value pair
Marks.update({"Sam": 55, "Ash": 78})
print("After update:", Marks)

# Harry value changed from 100 to 55
# Ash added as new key


# get()
# Returns value of given key.
# If key does not exist, returns None (no error).
print("Using get():", Marks.get("Sameer2"))


# Accessing using square brackets []
# This will give error if key does not exist
# print(Marks["Sameer2"])   # KeyError

# pop()
# Removes a key and returns its value
print("Using pop():", Marks.pop("Sameer"))
print("After pop:", Marks)
# Sameer key is removed from the dictionary and its value 100 is returned by pop() method.
# If you try to pop a key that does not exist, it will raise a KeyError. For example, Marks.pop("Sameer2") will raise an error since "Sameer2" is not a key in the Marks dictionary. However, you can provide a default value to return if the key does not exist: Marks.pop("Sameer2", "Key not found") will return "Key not found" instead of raising an error.

# clear()
# Removes all key-value pairs from the dictionary
# Marks.clear()
# print("After clear:", Marks)  # Output: {}
# The clear() method will empty the dictionary, leaving it with no key-value pairs. After calling Marks.clear(), the Marks dictionary will be empty, and printing it will show {}.

# Note: Since dictionaries are mutable, you can modify them by adding, updating, or removing key-value pairs. The methods shown above are commonly used for these operations. Always be cautious when modifying a dictionary while iterating over it, as it can lead to unexpected behavior.
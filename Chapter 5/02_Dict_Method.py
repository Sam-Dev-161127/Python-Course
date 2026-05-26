# DICTIONARY METHODS IN PYTHON

# Dictionary methods: are built-in functions that can be called on dictionary objects to perform specific operations or manipulations on the dictionary. These methods allow you to modify, analyze, and work with dictionaries in various ways.

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

# Explanation:
# 1. The items() method returns a view object that displays a list of dictionary's key-value pairs as tuples. Each tuple contains a key and its corresponding value from the dictionary.
# 2. The keys() method returns a view object that displays a list of all the keys in the dictionary. This allows you to see what keys are available in the dictionary.
# 3. The values() method returns a view object that displays a list of all the values in the dictionary. This allows you to see what values are stored in the dictionary.
# 4. The update() method is used to update the dictionary with new key-value pairs or to change the value of existing keys. If you provide a key that already exists in the dictionary, its value will be updated to the new value you provide. If you provide a new key, it will be added to the dictionary with the specified value.
# 5. The get() method is used to access the value of a specific key in the dictionary. If the key exists, it returns the corresponding value. If the key does not exist, it returns None instead of raising an error, which makes it safer to use when you are not sure if the key is present in the dictionary.
# 6. The pop() method is used to remove a key-value pair from the dictionary and return the value of the removed key. If the key does not exist, it will raise a KeyError unless you provide a default value to return instead.
# 7. The clear() method is used to remove all key-value pairs from the dictionary, effectively emptying it. After calling clear(), the dictionary will have no keys or values, and it will be represented as {} when printed.
# 8. These methods allow you to manipulate and work with dictionaries in various ways, such as adding new entries, updating existing entries, accessing values safely, and clearing the dictionary when needed. Always be cautious when using methods that modify the dictionary, as they will change the original dictionary in place.
# This program can be easily modified to include more dictionary methods or to demonstrate the use of dictionary methods in different contexts by changing the dictionary contents and the methods used. For example, you can create a dictionary of student names and their grades, and then use the items(), keys(), values(), update(), get(), pop(), and clear() methods to manipulate and analyze the dictionary as needed.

# Note: When using the pop() method, if you try to pop a key that does not exist in the dictionary, it will raise a KeyError. To avoid this, you can provide a default value to return if the key is not found. For example, Marks.pop("Sameer2", "Key not found") will return "Key not found" instead of raising an error since "Sameer2" is not a key in the Marks dictionary.
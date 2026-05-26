# DICTIONARY IN PYTHON

# Dictionary: is a collection of key-value pairs that are unordered, changeable, and indexed. Dictionaries are defined by enclosing the items in curly braces {} and separating the key-value pairs with commas. Each key is separated from its value by a colon (:). Keys must be unique and immutable (like strings or numbers), while values can be of any data type and can be duplicated.

# Empty Dictionary
Name = {}  
print("Empty dictionary:", Name)


# Dictionary storing marks
Marks = {
    "Sameer": 99,
    "Dibya": 77
}

# Accessing value using key
# Syntax: dictionary[key]
print("Marks of Sameer:", Marks["Sameer"])


# Hindi to English word dictionary
Words = {
    "billi": "cat",
    "gaye": "cow",
    "kauwa": "crow",
    "hati": "elephant"
}

# Taking input from user
Word = input("Enter the word which you want meaning: ")

# Printing meaning using dictionary
print("Meaning is:", Words[Word])

# Explanation:
# 1. A dictionary is a collection of key-value pairs where each key is unique and is used to access its corresponding value.
# 2. Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. Each key is separated from its value by a colon (:).
# 3. You can access the value of a dictionary by using its key. For example, Marks["Sameer"] will return the value 99, which is the mark of Sameer.
# 4. Dictionaries are unordered, which means that the items do not have a defined order and cannot be accessed by index like lists or tuples. Instead, you access values using their keys.
# 5. Dictionaries are mutable, which means you can change their content after they have been created. You can add new key-value pairs, modify existing values, or remove key-value pairs from the dictionary.
# 6. In the example of the Hindi to English word dictionary, we take input from the user and use that input as a key to access the corresponding value (meaning) from the dictionary.

# Note: When accessing a value using a key, if the key does not exist in the dictionary, it will raise a KeyError. To avoid this, you can use the get() method of the dictionary, which returns None (or a specified default value) if the key is not found. For example, Words.get(Word) will return the meaning if the word exists in the dictionary or None if it does not exist. You can also provide a default value like Words.get(Word, "Word not found") to return "Word not found" if the key is not present in the dictionary.
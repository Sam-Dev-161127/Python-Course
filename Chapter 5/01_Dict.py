# DICTIONARY IN PYTHON
# A dictionary stores data in key : value pairs.
# It is written using curly brackets {}.
# Keys must be unique.
# Dictionaries are mutable (can be changed).


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

# Notes:
# - You can also have nested dictionaries (dictionaries inside dictionaries). For example: nested_dict = {"person1": {"name": "Sameer", "age": 25}, "person2": {"name": "Dibya", "age": 30}} where each key (person1 and person2) has a dictionary as its value.
# - To check if a key exists in a dictionary, you can use the 'in' keyword. For example, "Sameer" in Marks will return True because "Sameer" is a key in the Marks dictionary.
# - You can also add new key-value pairs to a dictionary. For example, Marks["Rohan"] = 88 will add a new key "Rohan" with the value 88 to the Marks dictionary.
# - To remove a key-value pair from a dictionary, you can use the del keyword. For example, del Marks["Dibya"] will remove the key "Dibya" and its associated value from the Marks dictionary.
# - You can also use the get() method to access values in a dictionary. For example, Marks.get("Sameer") will return 99, and Marks.get("Dibya") will return None since "Dibya" has been removed from the dictionary. The get() method is useful because it does not raise an error if the key does not exist, unlike using square brackets which would raise a KeyError.
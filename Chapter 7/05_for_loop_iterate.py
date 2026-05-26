# FOR LOOP ITERATION IN PYTHON
# You can loop through lists, tuples, strings, etc.

# For loop with a list
l = [1, 2, 3, 4, 67, 4, 56]
print("Looping through list:") # Loop through each element in the list l
for i in l:
    print(i)

# For loop with a tuple
k = (34, 23, 54, 24, 34)
print("\nLooping through tuple:") # Loop through each element in the tuple k
for i in k:
    print(i)

# For loop with a string
s = "sameer"
print("\nLooping through string:") # Loop through each character in the string s
for i in s:
    print(i)

'''
Output:

Looping through list: # Loop through each element in the list l
1
2
3
4
67
4
56

Looping through tuple: # Loop through each element in the tuple k
34
23
54
24
34

Looping through string: # Loop through each character in the string s
s
a
m
e
e
r
'''

# Explanation:
# 1. The for loop iterates over a sequence (like a list, string, or range) and executes the block of code for each item in the sequence.
# 2. The variable (like i, name, char) takes on the value of each item in the sequence during each iteration of the loop.
# 3. You can use for loops to iterate over any iterable object, such as lists, tuples, strings, dictionaries, sets, etc.
# 4. The range() function is commonly used to generate a sequence of numbers, which is useful for looping a specific number of times. You can specify the start, end, and step values in range() to customize the sequence of numbers generated. For example, range(0, 10, 2) will generate the even numbers from 0 to 8 (0, 2, 4, 6, 8).
# 5. For loops are often more concise and easier to read than while loops when you know the number of iterations in advance or when iterating over a collection of items.

# Notes:
# - The for loop iterates over each element in the collection (list, tuple, string) and executes the block of code for each element.
# - The variable (i in this case) takes on the value of each element in the collection during each iteration of the loop.
# - You can use for loops to iterate over any iterable object, such as lists, tuples, strings, dictionaries, sets, etc.
# - The range() function is commonly used to generate a sequence of numbers, which is useful for looping a specific number of times. You can specify the start, end, and step values in range() to customize the sequence of numbers generated. For example, range(0, 10, 2) will generate the even numbers from 0 to 8 (0, 2, 4, 6, 8).
# - For loops are often more concise and easier to read than while loops when you know the number of iterations in advance or when iterating over a collection of items.
# - When looping through a string, each character is treated as an individual element. This allows you to perform operations on each character, such as counting occurrences, modifying characters, or checking for specific characters in the string.
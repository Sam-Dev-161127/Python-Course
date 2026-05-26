# FOR LOOP IN PYTHON
# Used to repeat a block of code multiple times.

# Loop from 0 to 3 (range(4) generates 0, 1, 2, 3)
for i in range(4):
    print(i)

'''
Output:
0
1
2
3
'''

# Loop from 1 to 5 (range(1, 6) generates 1, 2, 3, 4, 5)
for i in range(1, 6):
    print(i)

'''
Output:
1
2
3
4
5
'''

# Loop through a list of names
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

'''
Output:
Alice
Bob
Charlie
'''

# Loop through a string
s = "Hello"
for char in s:
    print(char)

'''
Output:
H
e
l
l
o
'''

# Explanation:
# 1. The for loop iterates over a sequence (like a list, string, or range) and executes the block of code for each item in the sequence.
# 2. The variable (like i, name, char) takes on the value of each item in the sequence during each iteration of the loop.
# 3. You can use for loops to iterate over any iterable object, such as lists, tuples, strings, dictionaries, sets, etc.
# 4. The range() function is commonly used to generate a sequence of numbers, which is useful for looping a specific number of times. You can specify the start, end, and step values in range() to customize the sequence of numbers generated. For example, range(0, 10, 2) will generate the even numbers from 0 to 8 (0, 2, 4, 6, 8).
# 5. For loops are often more concise and easier to read than while loops when you know the number of iterations in advance or when iterating over a collection of items.


# Notes:
# - The for loop iterates over a sequence (like a list, string, or range) and executes the block of code for each item in the sequence.
# - The variable (like i, name, char) takes on the value of each item in the sequence during each iteration of the loop.
# - You can use for loops to iterate over any iterable object, such as lists, tuples, strings, dictionaries, sets, etc.
# - The range() function is commonly used to generate a sequence of numbers, which is useful for looping a specific number of times. You can specify the start, end, and step values in range() to customize the sequence of numbers generated. For example, range(0, 10, 2) will generate the even numbers from 0 to 8 (0, 2, 4, 6, 8).
# - For loops are often more concise and easier to read than while loops when you know the number of iterations in advance or when iterating over a collection of items.
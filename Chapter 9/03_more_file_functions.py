# READING FILES IN PYTHON

# Reading files: is the process of accessing and retrieving data from a file on your computer. In Python, you can read files using the open() function to open the file and the read() or readline() methods to read its content.

f = open("file.txt") # By default, open() uses "r" mode for reading

# lines = f.readlines() # readlines() reads all lines and returns a list of strings

# print(lines, type(lines)) # Output: ['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n', 'Line 5\n'] <class 'list'>

# line1 = f.readline()
# print(line1, type(line1)) # Output: Line 1 <class 'str'> (Note: it includes the newline character \n at the end of the line)

# line2 = f.readline()
# print(line2, type(line2)) # Output: Line 2 <class 'str'> (Note: it includes the newline character \n at the end of the line)

# line3 = f.readline()
# print(line3, type(line3)) # Output: Line 3 <class 'str'> (Note: it includes the newline character \n at the end of the line)

# line4 = f.readline()
# print(line4, type(line4)) # Output: Line 4 <class 'str'> (Note: it includes the newline character \n at the end of the line)

# line5 = f.readline()
# print(line5, type(line5)) # Output: Line 5 <class 'str'> (Note: it includes the newline character \n at the end of the line)

# line6 = f.readline()
# print(line6 == "") # Output: True (When readline() reaches the end of the file, it returns an empty string "")

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()
f.close() 

# EXPLANATION:
# 1. open("file.txt") → opens the file in read mode and returns a file object.
# 2. f.readline() → reads one line from the file and returns it as a string. It includes the newline character \n at the end of the line.
# 3. When readline() reaches the end of the file, it returns an empty string "".
# 4. The while loop continues to read lines until it reaches the end of the file, at which point it stops because line becomes an empty string.
# 5. f.close() → closes the file to free up system resources and ensure that any changes are saved properly.

# Note: Always remember to close the file after you're done with it to prevent memory leaks and other issues. You can also use the 'with' statement to handle files, which automatically takes care of closing the file for you, even if an error occurs. For example:
# with open("file.txt", "r") as f:
#     # Do something with the file
# # The file is automatically closed when exiting the 'with' block, even if an error occurs within the block. This is a recommended practice for handling files in Python to ensure proper resource management.
# This program can be easily modified to read files line by line using a for loop as well, which is often more concise and efficient. For example:
# with open("file.txt", "r") as f:
#     for line in f:
#         print(line)
# In this case, the for loop iterates over each line in the file object 'f', and the file is automatically closed after the block of code is executed.

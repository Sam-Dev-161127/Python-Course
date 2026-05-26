# FILE HANDLING IN PYTHON

# File handling: is the process of working with files in Python. It allows you to create, read, update, and delete files on your computer. Python provides built-in functions and methods to handle files efficiently.

# Example: Reading a file

# 1. Open the file in read mode
# 'file.txt' should exist in the same directory as this script
f = open("file.txt", "r")  # "r" stands for read mode

# 2. Read the entire content of the file
data = f.read()  

# 3. Print the content
print("File content:")
print(data)

# 4. Close the file
f.close()  

# EXPLANATION:
# 1. open("file.txt", "r") → opens the file named "file.txt" in read mode and returns a file object.
# 2. f.read() → reads the entire content of the file and stores it in the variable 'data'.
# 3. print(data) → prints the content of the file to the console.
# 4. f.close() → closes the file to free up system resources and ensure that any changes are saved properly.

# Note: Always remember to close the file after you're done with it to prevent memory leaks and other issues. You can also use the 'with' statement to handle files, which automatically takes care of closing the file for you, even if an error occurs. For example:
# with open("file.txt", "r") as f:
#     data = f.read()
#     print(data)
# In this case, the file will be automatically closed after the block of code is executed.

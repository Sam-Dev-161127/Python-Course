# WRITING TO A FILE IN PYTHON

# Writing to a file: is the process of saving data to a file on your computer. In Python, you can write to a file using the open() function with the appropriate mode ("w" for write, "a" for append) and the write() method to add content to the file.

# Text to write in the file
text_to_write = "Hey Sam, you are awesome"

# 1. Open a file in write mode ("w")
# If the file doesn't exist, it will be created
# If the file exists, its content will be overwritten
f = open("myfile.txt", "w")

# 2. Write the string to the file
f.write(text_to_write)

# 3. Close the file to save changes
f.close()

# EXPLANATION:
# 1. open("myfile.txt", "w") → opens a file named "myfile.txt" in write mode. If the file does not exist, it will be created. If it already exists, its content will be overwritten.
# 2. f.write(text_to_write) → writes the string stored in the variable 'text_to_write' to the file. The write() method takes a string as an argument and writes it to the file.
# 3. f.close() → closes the file to ensure that all changes are saved properly and to free up system resources.

# Note: Always remember to close the file after writing to it to prevent memory leaks and ensure that the data is saved correctly. You can also use the 'with' statement to handle files, which automatically takes care of closing the file for you, even if an error occurs. For example:
# with open("myfile.txt", "w") as f:
#     f.write(text_to_write)
# In this case, the file will be automatically closed after the block of code is executed, ensuring that your data is saved properly without needing to explicitly call f.close().
# FILE HANDLING USING 'WITH' STATEMENT

# The 'with' statement in Python is used for resource management, such as handling files. It ensures that resources are properly released after their use, even if an error occurs. When you use 'with' to open a file, it automatically takes care of closing the file once the block of code is executed.

# Traditional way (manual close)
f = open("file.txt", "r")  # Open file in read mode
print(f.read())             # Read and print the entire content
f.close()                   # Must close manually

# Recommended way using 'with'
with open("file.txt", "r") as f:  # Open file; 'with' handles closing
    print(f.read())               # Read and print the file content

# EXPLANATION:
# 1. The 'with' statement is used to wrap the execution of a block of code with methods defined by a context manager. In this case, it manages the file resource.
# 2. open("file.txt", "r") → opens the file in read mode and returns a file object, which is assigned to the variable 'f'.
# 3. The block of code under the 'with' statement is executed, where you can perform operations on the file (like reading or writing).
# 4. Once the block of code is executed, the 'with' statement automatically closes the file, ensuring that resources are released properly, even if an error occurs within the block.

# Note: Using 'with' is considered best practice for file handling in Python because it ensures that files are properly closed and resources are managed efficiently, reducing the risk of memory leaks and other issues related to file handling.

# This program can be easily modified to write to a file using 'with' as well. For example:
text_to_write = "Hey Sam, you are awesome"
with open("file.txt", "w") as f:  # Open file in write mode
    f.write(text_to_write)        # Write the text to the file
# In this case, the file will be automatically closed after the block of code is executed, ensuring that your data is saved properly without needing to explicitly call f.close().

# You can also use 'with' to append to a file by using "a" mode. For example:
text_to_append = "Hey Sam, you are awesome\n"
with open("file.txt", "a") as f:  # Open file in append mode
    f.write(text_to_append)       # Append the text to the file
# In this case, the file will be automatically closed after the block of code is executed, ensuring that your data is saved properly without needing to explicitly call f.close().

# The 'with' statement can also be used to read files line by line. For example:
with open("file.txt", "r") as f:
    for line in f:
        print(line)
# In this case, the for loop iterates over each line in the file object 'f', and the file is automatically closed after the block of code is executed.
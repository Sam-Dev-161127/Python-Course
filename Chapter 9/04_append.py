# APPENDING TO A FILE IN PYTHON

# Appending to a file: is the process of adding new content to the end of an existing file without overwriting its current content. In Python, you can append to a file using the open() function with the "a" mode (append) and the write() method to add new content.

# Text to append
text_to_append = "Hey Sam, you are awesome\n"  # Add \n to move to a new line

# 1. Open the file in append mode ("a")
# "a" mode adds new content at the end of the file
f = open("myfile.txt", "a")  

# 2. Write the string to the file
f.write(text_to_append)

# 3. Close the file
f.close()

# EXPLANATION:
# 1. open("myfile.txt", "a") → opens the file named "myfile.txt" in append mode. If the file does not exist, it will be created. If it already exists, new content will be added to the end of the file without overwriting the existing content.
# 2. f.write(text_to_append) → writes the string stored in the variable 'text_to_append' to the file. The write() method takes a string as an argument and writes it to the file. The \n at the end of the string ensures that the next time you append, it will start on a new line.
# 3. f.close() → closes the file to ensure that all changes are saved properly and to free up system resources.

# Note: Always remember to close the file after appending to it to prevent memory leaks and ensure that the data is saved correctly. You can also use the 'with' statement to handle files, which automatically takes care of closing the file for you, even if an error occurs. For example:
# with open("myfile.txt", "a") as f:
#     f.write(text_to_append)
# In this case, the file will be automatically closed after the block of code is executed, ensuring that your data is saved properly without needing to explicitly call f.close().
# This program can be easily modified to append multiple lines of text by using a loop or by writing a list of strings to the file. For example:
# lines_to_append = ["Line 1\n", "Line 2\n", "Line 3\n"]
# with open("myfile.txt", "a") as f:
#     f.writelines(lines_to_append)
# In this example, the writelines() method is used to write a list of strings to the file, and each string in the list should include a newline character \n at the end to ensure that each line is written on a new line in the file.

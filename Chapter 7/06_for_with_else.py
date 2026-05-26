# FOR LOOP WITH ELSE IN PYTHON
# The else block runs only if the loop completes normally (no break)

l = [1, 7, 8]

# Loop through the list
for item in l:
    print(item)
else:
    # This runs after the loop finishes normally
    print("Done! Loop has finished.")

'''
Output:
1
7
8
Done! Loop has finished.
'''

# Explanation:
# In this example, we have a list l containing the integers 1, 7, and 8. The for loop iterates through each item in the list and prints it. After the loop has finished iterating through all items, the else block is executed, printing "Done! Loop has finished." This demonstrates how the else block works in conjunction with a for loop in Python.

# Notes:
# - The else block is executed only if the loop completes without encountering a break statement. If a break statement is executed inside the loop, the else block will be skipped.
# - This can be useful for scenarios where you want to perform some action after the loop has finished iterating over all items, such as printing a message, performing cleanup, or handling cases where the loop did not find what it was looking for.
# - In this example, since there is no break statement in the loop, the else block will always execute after the loop has finished iterating through the list l.

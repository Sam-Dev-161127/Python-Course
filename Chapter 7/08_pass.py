# THE PASS STATEMENT IN PYTHON

# 'pass' is a placeholder statement
# It does nothing but is syntactically required
# Useful when you plan to write code later

# Example with a for loop
for s in range(5):  # small range for clarity
    pass  # Loop runs but does nothing

print("The for loop with pass ran without errors!")

# Using pass in a while loop
# We'll need to initialize s first
s = 0
while s < 5:  # small range for clarity
    print(s)   # This will print the value
    s += 1
    pass       # Optional here; does nothing

'''
Output:
The for loop with pass ran without errors!
0
1
2
3
4
'''

# EXPLANATION:
# 1. 'pass' does nothing. It’s used as a placeholder.
# 2. Useful in loops, functions, classes, or if/else blocks where code is not written yet.
# 3. Prevents syntax errors when an indented block is required.
# 4. The loop itself still executes normally.

# Notes:
# - 'pass' is often used during development when you want to outline the structure of your code but haven't implemented the logic yet. It allows you to run your code without errors while you work on the implementation.
# - In the context of loops, 'pass' can be used when you want to create a loop that does nothing for certain iterations, or when you want to create a loop that will be filled in later with actual code.
# - 'pass' can also be used in functions and classes as a placeholder for future code. For example, you might define a function with 'pass' if you want to create the function signature but haven't implemented the function body yet.
# - In if/else statements, 'pass' can be used when you want to handle a condition but haven't decided what to do yet. This allows you to write the structure of your code without having to fill in the logic immediately.
# - Overall, 'pass' is a useful tool for maintaining the structure of your code while allowing you to focus on the implementation details at a later time. It helps prevent syntax errors and allows you to run your code even when certain parts are not yet implemented.
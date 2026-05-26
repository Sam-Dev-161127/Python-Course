# BREAK AND CONTINUE IN PYTHON LOOPS

# BREAK: Stop the loop immediately
print("Example of BREAK:")
for k in range(100):
    if k == 34:
        break  # Exit the loop immediately when k is 34
    print(k)

# Explanation:
# 1. The loop starts from 0 and goes up to 99.
# 2. When k becomes 34, the 'break' statement stops the loop immediately.
# 3. Numbers 0 to 33 are printed. 34 and above are NOT printed.
# 4. Useful for stopping loops early, e.g., when searching for a value.

print("\nExample of CONTINUE:")
# CONTINUE: Skip the current iteration

for k in range(40):  # Smaller range for clarity
    if k == 34:
        continue  # Skip this iteration and continue with next
    print(k)

# Explanation:
# 1. The loop runs from 0 to 39.
# 2. When k is 34, the 'continue' statement skips printing it.
# 3. The loop continues with k = 35, 36, ..., 39.
# 4. Useful for ignoring specific values while still looping through all others.

# Notes:
# - 'break' exits the loop entirely, while 'continue' only skips the current iteration.
# - Both can be used in 'for' and 'while' loops.
# - Use 'break' when you want to stop processing further, and 'continue' when you want to skip certain conditions but keep processing the rest.
# - In nested loops, 'break' and 'continue' affect only the innermost loop they are in.
# - Be cautious when using 'break' and 'continue' as they can make code harder to read if overused or used in complex loops. Always consider readability and maintainability when using these statements.
# - In the context of 'for' loops, 'break' can be used to exit early when a certain condition is met, while 'continue' can be used to skip over certain iterations without exiting the loop entirely.
# - In 'while' loops, 'break' can be used to exit the loop when a certain condition is met, while 'continue' can be used to skip over certain iterations without exiting the loop entirely.
# - Both 'break' and 'continue' can be used in combination with 'else' blocks in loops. If a 'break' statement is executed, the 'else' block will not run. If a 'continue' statement is executed, the loop will skip to the next iteration, but the 'else' block will still run if the loop completes normally.
# - In summary, 'break' and 'continue' are powerful tools for controlling the flow of loops in Python, allowing you to exit early or skip specific iterations as needed. Use them judiciously to enhance the functionality of your loops while maintaining code readability.
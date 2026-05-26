# WHILE LOOP IN PYTHON
# Repeats code while a condition is True

i = 1   # Initialization

# Loop runs as long as i < 6
while i < 6:
    print(i)
    i += 1   # Increment i by 1 (same as i = i + 1)

'''
Output:
1
2
3
4
5
'''
# Explanation:
# 1. We start with i = 1.
# 2. The loop checks if i < 6. Since 1 < 6, it prints 1 and increments i to 2.
# 3. The loop checks if i < 6 again. Since 2 < 6, it prints 2 and increments i to 3.
# 4. This process continues until i becomes 6. At that point, the condition i < 6 is no longer True, so the loop stops.
# 5. The numbers 1 to 5 are printed, but 6 is not printed because the loop stops before it can print 6.

# If we had forgotten to increment i, the loop would have run forever (infinite loop) because the condition would always be True. Always ensure that your while loops have a way to eventually become False to avoid infinite loops.

# Notes:
# - The while loop continues to execute the block of code as long as the condition (i < 6) is True. Once i becomes 6, the condition becomes False and the loop stops.
# - It's important to ensure that the loop will eventually terminate. If you forget to increment i, or if the condition is always True, you will create an infinite loop that will run forever. Always make sure to update the variable that controls the loop condition to avoid this.
# - You can use while loops for tasks where the number of iterations is not known beforehand, such as reading user input until a certain condition is met, or processing items in a list until it's empty.
# - In this example, we start with i = 1 and keep printing i and incrementing it until it reaches 5. Once i becomes 6, the loop condition (i < 6) is no longer True, so the loop ends.
# LOOPS IN PYTHON
# Used to repeat tasks multiple times.
# Two main types: for loop, while loop

# Without loop: manually printing numbers
print(1)
print(2)
print(3)
print(4)
print(5)

# FOR LOOP
# Repeats code for a given range or collection
print("Using for loop:")
for i in range(1, 6):   # range(start, end) → end is excluded
    print(i)

# Explanation:
# i takes values 1, 2, 3, 4, 5 automatically
# Python executes print(i) for each value

# Note: range(1, 6) generates numbers from 1 to 5 (6 is not included). You can change the start and end values to generate different ranges. For example, range(0, 10) will generate numbers from 0 to 9.
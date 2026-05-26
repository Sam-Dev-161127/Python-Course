# MULTIPLICATION TABLE USING INPUT()

# Take input from the user and convert it to integer
number = int(input("Enter the number for which you want the multiplication table: "))

print(f"\nMultiplication Table of {number}:")

# Loop from 1 to 10
for i in range(1, 11):
    result = number * i  # Multiply the number by the current loop value
    print(f"{number} * {i} = {result}")

'''
Example Run:
Enter the number for which you want the multiplication table: 5

Multiplication Table of 5:
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
'''

# Explanation:
# 1. We start by taking input from the user using the input() function. The input is a string, so we convert it to an integer using int().
# 2. We then print a header for the multiplication table.
# 3. We use a for loop to iterate from 1 to 10 (inclusive) using range(1, 11).
# 4. Inside the loop, we calculate the result of multiplying the input number by the current value of i.
# 5. We print the multiplication result in a formatted string for better readability.

# Notes:
# - The input() function allows us to take user input, which is useful for making our program interactive.
# - The int() function is used to convert the input string to an integer, which is necessary for performing arithmetic operations.
# - The for loop is used to repeat the multiplication operation for each value of i from 1 to 10, allowing us to generate the multiplication table for the given number.
# - The f-string (formatted string) is used to format the output in a clear and readable way, showing the multiplication expression and its result.
# This program can be easily modified to generate multiplication tables for a range of numbers or to include more or fewer multiples by changing the range in the for loop.
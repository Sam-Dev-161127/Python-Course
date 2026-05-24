# MULTIPLE IF STATEMENTS IN PYTHON
# You can use several if or if-elif-else blocks independently.

# Taking input from user
a = int(input("Enter your age:"))

# IF STATEMENT NO: 1
# Checking if age is even or odd
if a % 2 == 0:
    print("Age is even")
else:
    print("Age is odd")
# End of IF statement no: 1

# IF STATEMENT NO: 2
# Checking voting eligibility using if-elif-else ladder
if a >= 18:
    print("You are capable of voting")
    print("You can vote for Bjp, Bjd, Aam, Congress, etc.") # This is just an example, not a political endorsement.
    print("Vote wisely!")

elif a < 0:
    print("Sorry, age cannot be negative. You cannot vote.") # This is an edge case to handle invalid input.

elif a == 0:
    print("You entered 0, which is not a valid age.") # This is another edge case to handle invalid input.

else:
    print("You are below 18, so you cannot vote") # This is the else block for the second IF statement.

# This always executes
print("End of Program")
# End of IF statement no: 2

# Notes:
# - You can have multiple if statements in a program, and they will be evaluated independently. In this example, the first if statement checks if the age is even or odd, while the second if statement checks voting eligibility. Both will run regardless of each other's conditions.
# - The second if statement uses an if-elif-else ladder to check multiple conditions related to age and voting eligibility. The first if checks if the age is 18 or above, the second elif checks for negative ages, the third elif checks for zero, and the else block handles all other cases (ages below 18).
# - Always remember to handle edge cases, such as negative ages or non-integer inputs, to make your program more robust. You can use additional conditions or try-except blocks for better error handling.
# IF - ELIF - ELSE STATEMENT (LADDER)
# Used when there are multiple conditions to check.
# Python checks conditions from top to bottom.
# Taking input from user
a = int(input("Enter your age: "))

# IF-ELIF-ELSE LADDER
if a >= 18:
    # Runs if age is 18 or above
    print("You are capable of voting") 
    print("You can vote for Bjp, Bjd, Aam, Congress, etc.") # This is just an example, not a political endorsement.
    print("Vote wisely!")

elif a < 0:
    # Runs if age is negative
    print("Sorry, age cannot be negative. You cannot vote.") # This is an edge case to handle invalid input.

elif a == 0:
    # Runs if age is exactly 0
    print("You entered 0, which is not a valid age.") # This is another edge case to handle invalid input.

else:
    # Runs if none of the above conditions are True
    print("You are below 18, so you cannot vote.")

# This always executes, outside the ladder
print("End of Program")

# Notes:
# - The if statement checks the first condition. If it's True, it executes that block and skips the rest of the ladder. If it's False, it moves to the next condition in the elif statement, and so on. If none of the conditions are True, it executes the else block.
# - You can have as many elif statements as needed to check multiple conditions. The else block is optional and will run if all previous conditions are False.
# - Always remember to handle edge cases, such as negative ages or non-integer inputs, to make your program more robust. You can use additional conditions or try-except blocks for better error handling.
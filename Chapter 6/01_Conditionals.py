# CONDITIONAL STATEMENTS IN PYTHON
# Used to perform different actions based on conditions.
# The main types: if, else, elif

# Taking input from user
a = int(input("Enter your age: "))

# IF-ELSE STATEMENT
# Executes one block if condition is True, otherwise executes else block
if a >= 18:
    print("You are capable of voting")
    print("You can vote for Bjp, Bjd, Aam, Congress, etc.")
    print("Vote wisely!")
else:
    print("You are not capable of voting")
    print("Wait until you turn 18!")

# This will always execute, outside if-else
print("End of program")

# Notes:
# - The condition in the if statement is evaluated to either True or False. If it's True, the code block under if is executed. If it's False, the code block under else is executed.
# - You can have multiple statements inside the if and else blocks, and they will all be executed if the respective condition is met.
# - The input() function is used to take user input, and int() is used to convert the input string to an integer, since age is a number.
# - Remember to handle edge cases, such as negative ages or non-integer inputs, in a real-world application. You can use additional conditions or try-except blocks for better error handling.
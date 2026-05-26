# FUNCTIONS IN PYTHON WITH OWN VARIABLES

# Function: is a reusable block of code that performs a specific task. Functions help to break down complex problems into smaller, manageable pieces, promote code reusability, and improve readability. A function can take input parameters, perform operations, and return a value.

# Function definition
def avg():
    """
    This function calculates the average of three numbers
    stored in variables and prints the result.
    """
    
    # Define my own variables instead of taking user input
    num1 = 10  # First number
    num2 = 20  # Second number
    num3 = 30  # Third number

    # Calculate the average
    average = (num1 + num2 + num3) / 3  

    # Print the result
    print(f"The average of {num1}, {num2}, {num3} is: {average}") # Output the average in a formatted string

# Function calls
# Calling the function multiple times

print("First call:")
avg()  # Calls the avg function and executes code inside
print("Thank you!\n")

print("Second call:")
avg()  # Calls again; no need to rewrite code
print("Thank you!\n")

print("Third call:")
avg()  # Function reused multiple times
print("Thank you!\n")

print("Fourth call:")
avg()  # Function can be reused as many times as needed
print("Thank you!\n")

# EXPLANATION:
# 1. def avg(): → defines a function named 'avg'.
# 2. Variables num1, num2, num3 → store numbers for average calculation.
# 3. average = (num1 + num2 + num3)/3 → calculates the average.
# 4. print(...) → displays the average.
# 5. avg() → calls the function; the code inside runs.
# 6. Reusing functions avoids repeating the same code.

# Note:
# - Functions allow us to encapsulate code that performs a specific task, making our programs more organized and reusable.
# - By defining our own variables inside the function, we can perform calculations without needing user input, which is useful for testing and when fixed values are needed.
# - We can call the function as many times as we want, and it will execute the same code each time, which promotes code reusability and reduces redundancy.
# - The print statements after each function call provide feedback to the user, indicating that the function has been executed and showing the result.
# This program can be easily modified to take user input for the numbers or to calculate the average of a different set of numbers by changing the variables inside the function.
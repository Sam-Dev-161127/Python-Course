# FUNCTION WITH ARGUMENTS IN PYTHON

# Function with arguments: A function that takes input parameters (arguments) to perform a specific task. Arguments allow you to pass data to the function, making it more flexible and reusable for different inputs.

# Function definition
def good_day(name, ending):
    """
    This function greets the person by name and prints
    a closing message (ending). It also returns a string.
    """
    # Print greeting
    print("Good day, " + name) # Concatenate "Good day, " with the name parameter and print it
    
    # Print ending message
    print(ending)
    
    # Return a value
    return "ok"

# Function call with arguments

# Call the function by passing the arguments "Sameer" and "Thank you"
a = good_day("Sameer", "Thank you")

# The function returned "ok", which we print here
print(a)

# EXPLANATION:
# 1. def good_day(name, ending): → 'name' and 'ending' are parameters.
# 2. Parameters allow you to pass information to the function.
# 3. print("Good day," + name) → prints the greeting using the 'name'.
# 4. print(ending) → prints the ending message.
# 5. return "ok" → the function sends a value back to the caller.
# 6. a = good_day(...) → stores the returned value ("ok") in variable 'a'.
# 7. print(a) → prints the returned value.
# 8. Functions with arguments are flexible and reusable for different inputs.

# Note:
# - Functions with arguments allow us to pass different values each time we call the function, making it more versatile and reusable.
# - The return statement allows a function to send a value back to the caller, which can be stored in a variable or used directly.
# - In this example, we defined a function that takes two parameters (name and ending), prints a greeting and a closing message, and returns a string. We then called the function with specific arguments and printed the returned value.
# This program can be easily modified to include more parameters, perform different actions based on the input
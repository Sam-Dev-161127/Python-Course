# FUNCTION WITH DEFAULT ARGUMENTS

# Default arguments: are parameters that have a default value specified in the function definition. If the caller does not provide a value for that parameter, the default value will be used. This allows for more flexible and reusable functions, as it provides a fallback option when certain arguments are not supplied.

# Function definition with a default argument for 'ending'
def good_day(name, ending="Thank you"):
    """
    This function greets a person by name.
    If no ending message is provided, it uses the default: "Thank you".
    """
    print(f"Good day, {name}")  # Greeting using the name
    print(ending)               # Ending message

# Function calls

# Case 1: Passing both arguments
good_day("Sameer", "Thanks")

# Case 2: Passing only the name; ending uses default value
good_day("Rahol")

'''
Output:
Good day, Sameer
Thanks
Good day, Rahol
Thank you
'''

# EXPLANATION:
# 1. 'ending="Thank you"' → default value for the parameter 'ending'.
# 2. If you pass a second argument, it overrides the default.
# 3. If you do not pass a second argument, the default value is used.
# 4. This makes functions flexible and easier to reuse.
# 5. f-strings (f"Good day, {name}") make string formatting easier.

# Note:
# - Default arguments allow you to specify a default value for a parameter in a function definition. This means that if the caller does not provide a value for that parameter, the default value will be used.
# - In the example above, the 'good_day' function has a default argument for 'ending'. If the caller does not provide a value for 'ending', it will default to "Thank you".
# - This feature is particularly useful for functions that have parameters that are often the same, allowing the caller to omit those parameters when they want to use the common default value, while still providing the flexibility to specify a different value when needed.
# - The use of f-strings (formatted string literals) allows for easier and more readable string formatting, making it simple to include variable values directly within the string. In this case, it is used to greet the person by name in a clear and concise way.
# This program can be easily modified to include more parameters with default values or to perform different actions based on the input by changing the function definition and the logic inside the function.
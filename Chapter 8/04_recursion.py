# RECURSION IN PYTHON

# Recursion: A function that calls itself to solve a problem by breaking it down into smaller, more manageable subproblems. It typically has a base case to stop the recursion and a recursive case that continues to call the function until the base case is reached.

# Example: Calculating the factorial of a number using recursion. 


'''
Factorial of n (n!) is:
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * 1
factorial(3) = 3 * 2 * 1
factorial(4) = 4 * 3 * 2 * 1
factorial(5) = 5 * 4 * 3 * 2 * 1
factorial(n) = n * factorial(n-1)
'''

# Function definition using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n-1)

# Using input from the user
n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")

'''Output:'''
'''

Example Run:
Enter a number: 5
The factorial of 5 is: 120
'''

# EXPLANATION:
# 1. Base Case: Stops recursion at n=0 or n=1 → return 1
# 2. Recursive Case: factorial(n) = n * factorial(n-1)
# 3. Each function call waits for the next call to complete.
# 4. Recursion continues until base case is reached.
# 5. Factorial of n is calculated by multiplying all numbers from n down to 1.
# 6. Recursion is useful for problems that can be broken into smaller identical subproblems.

# Note:
# - Recursion can lead to elegant and simple code, but it can also cause issues like stack overflow if the base case is not properly defined or if the recursion goes too deep. Always ensure that your recursive function has a well-defined base case to prevent infinite recursion.
# - In the example of calculating factorial, the function calls itself with a smaller value of n until it reaches the base case. This is a common pattern in recursive functions, where the problem is reduced step by step until it can be solved directly.
# - Recursion can be used in various applications such as tree traversal, backtracking algorithms, and divide-and-conquer strategies. It is a powerful tool in programming, but it should be used judiciously to avoid performance issues.
# This program can be easily modified to calculate other recursive functions, such as Fibonacci numbers or to solve problems like the Tower of Hanoi by changing the logic inside the recursive function and defining appropriate base and recursive cases.
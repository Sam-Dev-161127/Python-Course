# Valid Variable Names

a = 77        # valid (starts with alphabet)
aaa = 10      # valid (multiple letters allowed)
sameer = 442  # valid
_sameer = 44  # valid (underscore allowed at start)
student1 = 10     # valid (number allowed after first letter)
marks_2026 = 95   # valid (underscore allowed)


# Invalid Variable Names

# @sameer = 33    # invalid (cannot start with symbol)
# 1name = "Sam"   # invalid (cannot start with number)
# s@meer = 50     # invalid (@ symbol not allowed)
# if = 10         # invalid (Python keyword)
# for = 5         # invalid (Python keyword)
# while = 3       # invalid (Python keyword)


# Case Sensitivity Example

name = "Sam"
Name = "Rohan"   # different variable (Python is case-sensitive)

# Notes: Variable names are case-sensitive in Python. This means that 'name' and 'Name' are considered two different variables. It's important to be consistent with variable naming to avoid confusion and errors in your code.
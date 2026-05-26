# INSTANCE ATTRIBUTE VS CLASS ATTRIBUTE IN PYTHON

# Instance attribute: is an attribute that is specific to an instance of a class. It is defined within the __init__ method or can be added to an instance after it has been created. Each instance of the class can have different values for its instance attributes.

class Employee: # This is a class definition. It defines a class named Employee.

    language = "Python" #This is a class attribute. It is shared by all instances of the class.

    salary = 1200000 # This is also a class attribute. It is shared by all instances of the class.


sameer = Employee() # This creates an instance of the Employee class and assigns it to the variable sameer.

sameer.name = "Sameer" # This is an instance attribute. It is unique to the instance sameer.

sameer.language = "JavaScript"  # This will create an instance attribute for sameer. It will not change the class attribute language for other instances of the class.

print(sameer.name, sameer.language, sameer.salary) # This will print the name, language and salary of sameer. It will print "Sameer JavaScript 1200000" because we have created an instance attribute for sameer.

# Here name and language are instance attributes and salary is a class attribute. We can access class attributes using object as well as class name. But we can access object attributes only using object name.

# Explanation:
# 1. We defined a class named Employee with two class attributes: language and salary.
# 2. We created an instance of the Employee class named sameer and assigned it the name "Sameer" as an instance attribute.
# 3. We created an instance attribute for sameer named language and assigned it the value
# "JavaScript". This does not change the class attribute language for other instances of the class.
# 4. We printed the name, language, and salary of sameer. Since we created an instance attribute for language, it used that value instead of the class attribute, resulting in "Sameer JavaScript 1200000".
# 5. Instance attributes are unique to each instance of the class, while class attributes are shared among all instances. You can access class attributes using either the class name or the instance name, but instance attributes can only be accessed using the instance name.
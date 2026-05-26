# CLASSES IN PYTHON

# Class: is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. A class is like a template for creating objects, and an object is an instance of a class.

class Employee: # This is a class definition. It defines a class named Employee.
    
    language = "Python" # This is a class attribute. It is shared by all instances of the class.

    salary = 1200000 # This is also a class attribute. It is shared by all instances of the class.


sameer = Employee() # This creates an instance of the Employee class and assigns it to the variable sameer.

sameer.name = "Sameer" # This is an instance attribute. It is unique to the instance sameer.

print(sameer.name,sameer.language,sameer.salary) # This will print the name, language and salary of sameer. It will print "Sameer Python 1200000" because we have not created an instance attribute for sameer.

rohan = Employee() # This creates an instance of the Employee class and assigns it to the variable rohan.

rohan.name = "Rohan Roro Robinson" # This is an instance attribute. It is unique to the instance rohan.

print(rohan.name,rohan.language,rohan.salary) # This will print the name, language and salary of rohan. It will print "Rohan Roro Robinson Python 1200000" because we have not created an instance attribute for rohan.

# Here name is object attribute and language and salary are class attributes. We can access class attributes using object as well as class name. But we can access object attributes only using object name.

# Explanation:
# 1. We defined a class named Employee with two class attributes: language and salary.
# 2. We created an instance of the Employee class named sameer and assigned it the name "Sameer" as an instance attribute.
# 3. We printed the name, language, and salary of sameer. Since we did not create instance attributes for language and salary, it used the class attributes, resulting in "Sameer Python 1200000".
# 4. We created another instance of the Employee class named rohan and assigned it the name "Rohan Roro Robinson" as an instance attribute.
# 5. We printed the name, language, and salary of rohan. Similar to sameer, it used the class attributes for language and salary, resulting in "Rohan Roro Robinson Python 1200000".
# 6. Class attributes are shared among all instances of the class, while instance attributes are unique to each instance. You can access class attributes using either the class name or the instance name, but instance attributes can only be accessed using the instance name.

# Note:
# - In this example, we have not defined an __init__ method, which is a special method used to initialize instance attributes when an object is created. If we had defined an __init__ method, we could have set the name, language, and salary for each instance at the time of object creation. For example:
# class Employee:
#     def __init__(self, name, language, salary):
#         self.name = name
#         self.language = language
#         self.salary = salary
# sameer = Employee("Sameer", "Python", 1200000)
# rohan = Employee("Rohan Roro Robinson", "Python", 1200000)
# This way, we can set the attributes for each instance when we create the object, and we can also have different values for each instance if needed.
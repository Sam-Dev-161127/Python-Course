# SELF IN PYTHON

# Self: is a reference to the current instance of the class. It is used to access the attributes and methods of the class in Python. The self parameter is a convention and can be named anything, but it is recommended to use self for better readability.

class Employee: # This is a class definition. It defines a class named Employee.

    language = "Python" #This is a class attribute. It is shared by all instances of the class.

    salary = 1200000 # This is also a class attribute. It is shared by all instances of the class.

    def getInfo(self): # This is a method definition. It defines a method named getInfo that belongs to the Employee class.
        print(f"The language is {self.language} and the salary is {self.salary}") # This will print the language and salary of the Employee class. It will print "The language is Python and the salary is 1200000" because we are accessing the class attributes using the class name.

    @staticmethod
    def greet(): # This is another method definition. It defines a method named greet that belongs to the Employee class.
        print("Good Morning") # This will print "Good Morning" when the greet method is called.

sameer = Employee() # This creates an instance of the Employee class and assigns it to the variable sameer.

sameer.name = "Sameer" # This is an instance attribute. It is unique to the instance sameer.

# sameer.language = "JavaScript"  # This will create an instance attribute for sameer. It will not change the class attribute language for other instances of the class.

print(sameer.name, sameer.language, sameer.salary) # This will print the name, language and salary of sameer. It will print "Sameer JavaScript 1200000" because we have created an instance attribute for sameer.

Employee.getInfo(sameer) # This will call the getInfo method of the Employee class and pass the instance sameer as an argument. It will print "The language is JavaScript and the salary is 1200000" because we are accessing the instance attributes using the instance name.

Employee.greet() # This will call the greet method of the Employee class. It will print "Good Morning" because we are calling the greet method using the class name.

# Explanation:
# 1. We defined a class named Employee with two class attributes: language and salary.
# 2. We defined a method named getInfo that prints the language and salary of the Employee class using the self parameter to access the class attributes.
# 3. We defined another method named greet that prints "Good Morning" when called.
# 4. We created an instance of the Employee class named sameer and assigned it the name "Sameer" as an instance attribute.
# 5. We printed the name, language, and salary of sameer. Since we created an instance attribute for language, it used that value instead of the class attribute, resulting in "Sameer JavaScript 1200000".
# 6. We called the getInfo method of the Employee class and passed the instance sameer as an argument. It printed "The language is JavaScript and the salary is 1200000" because we accessed the instance attributes using the instance name.
# 7. We called the greet method of the Employee class and passed the instance sameer as an argument. It printed "Good Morning" because we called the greet method using the class name and passed the instance as an argument.  

# Note:
# - The self parameter is a reference to the current instance of the class and is used to access the attributes and methods of the class. It is a convention to use self as the name of the first parameter in instance methods, but you can name it anything you like. However, using self is recommended for better readability and to follow Python conventions.
# - In the example, we defined a method getInfo that uses self to access the class attributes language and salary. We also defined a static method greet that does not use self because it does not need to access any instance or class attributes. Static methods are defined using the @staticmethod decorator and do not take self as a parameter. They can be called using the class name without needing an instance of the class.

# Multiple Inheritance in Python

# Multiple Inheritance: is a feature in object-oriented programming languages that allows a class to inherit attributes and methods from more than one parent class. This can be useful when you want to create a new class that combines the functionality of multiple existing classes.
class Employee: # Parent Class
    company = "ITC" # Class Attribute
    name = "Sameer" # Instance Attribute
    salary = 10000000 # Instance Attribute
    def show(self): # Instance Method
        print(f"The name of the employee is {self.name} and the salray is {self.salary}") # This method will print the name and salary of the employee. It uses the self parameter to access the instance attributes name and salary.

class Coder: # Parent Class
    language = "Python" # Class Attribute
    def printlanguage(self): # Instance Method
        print(f"Out of all the languages here is your language: {self.language}") # This method will print the programming language of the coder. It uses the self parameter to access the instance attribute language.

# class Programmer: # Inheritance
#     company = "Fiverr" # This will override the company attribute of the Employee class. Now, when we access the company attribute using an instance of the Programmer class, it will return "Fiverr" instead of "ITC".
#     def show(self): # This is a method definition. It defines a method named show that belongs to the Programmer class. This method will print the name and salary of the programmer. It uses the self parameter to access the instance attributes name and salary.
#         print(f"The name is {self.name} and the salry is {self.salary}") # This will print the name and salary of the programmer. It uses the self parameter to access the instance attributes name and salary.

#     def showLanguage(self): # This is another method definition. It defines a method named showLanguage that belongs to the Programmer class. This method will print the name and the programming language of the programmer. It uses the self parameter to access the instance attributes name and language.
#         print(f"The name is {self.name} and he is good in {self.language} language") # This will print the name and the programming language of the programmer. It uses the self parameter to access the instance attributes name and language.

class Programmer(Employee, Coder ): # Multiple Inheritance
    company = "Fiverr" # This will override the company attribute of the Employee class. Now, when we access the company attribute using an instance of the Programmer class, it will return "Fiverr" instead of "ITC".
    def showLanguage(self): # This is another method definition. It defines a method named showLanguage that belongs to the Programmer class. This method will print the name and the programming language of the programmer. It uses the self parameter to access the instance attributes name and language.
        print(f"The name of the company is {self.company} and he is good with {self.language} language") # This will print the name of the company and the programming language of the programmer. It uses the self parameter to access the instance attributes company and language.

a = Employee() # This creates an instance of the Employee class and assigns it to the variable a.
b = Programmer() # This creates an instance of the Programmer class and assigns it to the variable b.


b.show() # This will call the show method of the Programmer class. It will print "The name of the employee is Sameer and the salray is 10000000" because we are accessing the instance attributes name and salary using the instance b.
b.printlanguage() # This will call the printlanguage method of the Coder class. It will print "Out of all the languages here is your language: Python" because we are accessing the instance attribute language using the instance b.
b.showLanguage() # This will call the showLanguage method of the Programmer class. It will print "The name of the company is Fiverr and he is good with Python language" because we are accessing the instance attributes company and language using the instance b.

# Explanation:
# 1. We defined two parent classes named Employee and Coder, each with their own class attributes and instance methods.
# 2. We defined a child class named Programmer that inherits from both Employee and Coder classes. The Programmer class has its own class attribute company that overrides the company attribute of the Employee class, and it also has an additional method showLanguage that prints the name of the company and the programming language of the programmer.
# 3. We created an instance of the Employee class named a and an instance of the Programmer class named b.
# 4. We called the show method of the Programmer class using the instance b, which printed "The name of the employee is Sameer and the salray is 10000000" because we accessed the instance attributes name and salary using the instance b.
# 5. We called the printlanguage method of the Coder class using the instance b, which printed "Out of all the languages here is your language: Python" because we accessed the instance attribute language using the instance b.
# 6. We called the showLanguage method of the Programmer class using the instance b, which printed "The name of the company is Fiverr and he is good with Python language" because we accessed the instance attributes company and language using the instance b.

# Note:
# - Multiple inheritance allows a child class to inherit attributes and methods from more than one parent class. In this example, the Programmer class inherits from both Employee and Coder classes, allowing it to access the attributes and methods of both parent classes.
# - When there are multiple parent classes, the child class can override the attributes and methods of any of the parent classes by defining them with the same name. In this example, the company attribute of the Programmer class overrides the company attribute of the Employee class. When we access the company attribute using an instance of the Programmer class, it returns "Fiverr" instead of "ITC".
# - The child class can also add new attributes and methods that are not present in any of the parent classes. In this example, the showLanguage method is defined in the Programmer class but not in either the Employee or Coder classes. This allows us to have additional functionality in the child class while still retaining the functionality of both parent classes.
# - We can create multiple instances of the child class (Programmer) and each instance can have its own unique attributes while still sharing the common attributes and methods of both parent classes (Employee and Coder). This is one of the key benefits of multiple inheritance in object-oriented programming.
# - However, multiple inheritance can also lead to ambiguity if there are attributes or methods with the same name in both parent classes. In such cases, Python uses the Method Resolution Order (MRO) to determine which attribute or method to use. The MRO follows a specific order of precedence when looking for attributes and methods in the parent classes. It is important to be aware of this when using multiple inheritance to avoid unexpected behavior.
# - In general, multiple inheritance can be a powerful tool for code reuse and creating complex class hierarchies, but it should be used with caution to avoid potential issues with ambiguity and maintainability.
# - In this example, we have a simple case of multiple inheritance where the Programmer class inherits from both Employee and Coder classes. The Programmer class can access the attributes and methods of both parent classes, allowing us to create a more versatile class that combines the functionality of both parent classes.
# - We can also use the super() function in the child class to call the methods of the parent classes. This can be useful when we want to extend the functionality of a method from the parent class rather than completely overriding it. In this example, we did not use super() because we completely overrode the showLanguage method in the Programmer class, but in other cases, you might want to call the parent class's method and then add additional functionality in the child class's method.
# - Overall, multiple inheritance is a powerful feature in object-oriented programming that allows for greater flexibility and code reuse, but it should be used judiciously to avoid potential issues with ambiguity and maintainability. 
# - In this example, we have a simple case of multiple inheritance where the Programmer class inherits from both Employee and Coder classes. The Programmer class can access the attributes and methods of both parent classes, allowing us to create a more versatile class that combines the functionality of both parent classes.
# - We can also use the super() function in the child class to call the methods of the parent classes. This can be useful when we want to extend the functionality of a method from the parent class rather than completely overriding it. In this example, we did not use super() because we completely overrode the showLanguage method in the Programmer class, but in other cases, you might want to call the parent class's method and then add additional functionality in the child class's method.
# Overall, multiple inheritance is a powerful feature in object-oriented programming that allows for greater flexibility and code reuse, but it should be used judiciously to avoid potential issues with ambiguity and maintainability.

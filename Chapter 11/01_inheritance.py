# Inheritance in Python

# Inheritance: is a fundamental object-oriented programming concept that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

class Employee: # Paranet Class
    company = "ITC" # Class Attribute
    def show(self): # Instance Method
        print(f"The name of the employee is {self.name} and the salry is {self.salary}") # This method will print the name and salary of the employee. It uses the self parameter to access the instance attributes name and salary.


# class Programmer:
#     company = "Fiverr"
#     def show(self):
#         print(f"The name is {self.name} and the salry is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in {self.language} language")

class Programmer(Employee): # Inheritance
    company = "Fiverr" # This will override the company attribute of the Employee class. Now, when we access the company attribute using an instance of the Programmer class, it will return "Fiverr" instead of "ITC".
    def showLanguage(self): # This is a method definition. It defines a method named showLanguage that belongs to the Programmer class. This method will print the name and the programming language of the programmer. It uses the self parameter to access the instance attributes name and language.
        print(f"The name is {self.name} and he is good in {self.language} language") # This will print the name and the programming language of the programmer. It uses the self parameter to access the instance attributes name and language.

a = Employee() # This creates an instance of the Employee class and assigns it to the variable a.
b = Programmer() # This creates an instance of the Programmer class and assigns it to the variable b.


print(a.company, b.company) # This will print the company attribute of both instances a and b. It will print "ITC Fiverr" because the company attribute of the Employee class is "ITC" and the company attribute of the Programmer class is "Fiverr".

b.name = "Sameer" # This is an instance attribute. It is unique to the instance b.
b.salary = 75000 # This is another instance attribute. It is unique to the instance b.
b.language = "Python" # This is another instance attribute. It is unique to the instance b.

b.show() # This will call the show method of the Programmer class. It will print "The name of the employee is Sameer and the salry is 75000" because we are accessing the instance attributes name and salary using the instance b.

b.showLanguage() # This will call the showLanguage method of the Programmer class. It will print "The name is Sameer and he is good in Python language" because we are accessing the instance attributes name and language using the instance b.

# Explanation:
# 1. We defined a parent class named Employee with a class attribute company and an instance method show that prints the name and salary of the employee.
# 2. We defined a child class named Programmer that inherits from the Employee class. The Programmer class has its own class attribute company that overrides the company attribute of the Employee class, and it also has an additional method showLanguage that prints the name and programming language of the programmer.
# 3. We created an instance of the Employee class named a and an instance of the Programmer class named b.
# 4. We printed the company attribute of both instances a and b. It printed "ITC Fiverr" because the company attribute of the Employee class is "ITC" and the company attribute of the Programmer class is "Fiverr".
# 5. We set the instance attributes name, salary, and language for the instance b
# 6. We called the show method of the Programmer class using the instance b, which printed "The name of the employee is Sameer and the salry is 75000" because we accessed the instance attributes name and salary using the instance b.
# 7. We called the showLanguage method of the Programmer class using the instance b, which printed "The name is Sameer and he is good in Python language" because we accessed the instance attributes name and language using the instance b.

# Note:
# - Inheritance allows the child class (Programmer) to reuse the code of the parent class (Employee) and also to add its own attributes and methods. This promotes code reusability and helps to create a natural hierarchical relationship between classes.
# - The child class can override the attributes and methods of the parent class by defining them with the same name. In this example, the company attribute of the Programmer class overrides the company attribute of the Employee class. When we access the company attribute using an instance of the Programmer class, it returns "Fiverr" instead of "ITC".
# - The child class can also add new attributes and methods that are not present in the parent class. In this example, the showLanguage method is defined in the Programmer class but not in the Employee class. This allows us to have additional functionality in the child class while still retaining the functionality of the parent class.
# - We can create multiple instances of the child class (Programmer) and each instance can have its own unique attributes while still sharing the common attributes and methods of the parent class (Employee). This is one of the key benefits of inheritance in object-oriented programming.

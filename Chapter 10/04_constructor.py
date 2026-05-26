# CONSTRUCTOR IN PYTHON

# Constructor: is a special method in Python that is automatically called when an object of a class is created. It is used to initialize the attributes of the class. The constructor method in Python is defined using the __init__() method.

class Employee: # This is a class definition. It defines a class named Employee.

    language = "Python" #This is a class attribute. It is shared by all instances of the class.

    salary = 1200000 # This is also a class attribute. It is shared by all instances of the class.

    def __init__(self, name, salary, language): # Dunder method which is automatically called. Only init

        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self): # This is a method definition. It defines a method named getInfo that belongs to the Employee class.
        print(f"The language is {self.language} and the salary is {self.salary}") # This will print the language and salary of the Employee class. It will print "The language is Python and the salary is 1200000" because we are accessing the class attributes using the class name.

    @staticmethod #
    def greet(): # This is another method definition. It defines a method named greet that belongs to the Employee class.
        print("Good Morning") # This will print "Good Morning" when the greet method is called.

sameer = Employee("Sameer", 1300000, "C++") # This creates an instance of the Employee class and assigns it to the variable sameer.

# sameer.name = "Sameer"

print(sameer.name, sameer.salary, sameer.language)

# Explanation:
# 1. We defined a class named Employee with two class attributes: language and salary.
# 2. We defined a constructor method __init__ that takes three parameters: name, salary, and language. This method is automatically called when an object of the Employee class is created.
# 3. Inside the constructor, we initialized the instance attributes name, salary, and language with the values passed as arguments.
# 4. We created an instance of the Employee class named sameer and passed the values "Sameer", 1300000, and "C++" as arguments to the constructor.
# 5. We printed the name, salary, and language of sameer. It will print "Sameer 1300000 C++" because we initialized these attributes in the constructor.

# Note:
# - The __init__ method is a special method in Python that serves as the constructor for a class. It is called automatically when an object of the class is created, and it is used to initialize the attributes of the class.
# - The self parameter in the __init__ method refers to the instance being created, allowing us to set the attributes for that specific instance. In this example, we set the name, salary, and language attributes for the sameer instance when it is created.
# - The constructor allows us to create objects with specific attributes right at the time of object creation, making our code cleaner and more efficient. We can create multiple instances of the Employee class with different attributes by passing different arguments to the constructor.
class Employee: # Paranet Class
    company = "ITC"
    name = "Sameer"
    salary = 10000000
    def show(self):
        print(f"The name of the employee is {self.name} and the salray is {self.salary}")

class Coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

# class Programmer:
#     company = "Fiverr"
#     def show(self):
#         print(f"The name is {self.name} and the salry is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in {self.language} language")

class Programmer(Employee, Coder ): # Inheritance
    company = "Fiverr"
    def showLanguage(self):
        print(f"The name of the company is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()


b.show()
b.printlanguage()
b.showLanguage()
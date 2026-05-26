class Employee: # Paranet Class
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salry is {self.salary}")


# class Programmer:
#     company = "Fiverr"
#     def show(self):
#         print(f"The name is {self.name} and the salry is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in {self.language} language")

class Programmer(Employee): # Inheritance
    company = "Fiverr"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()


print(a.company, b.company) 
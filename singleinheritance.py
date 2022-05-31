class Employee:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Name = " +self.name)

class Programmer(Employee):
    def __init__(self, name):
        self.name = name

    def LearnPython(self):
        print("Learning Python language")

class HR(Employee):
    def __init__(self, name):
        self.name = name

    def ManageHR(self):
        print("Hiring and training program")

emp1 = Employee("Brian")
emp1.printName()

P1 = Programmer("John")
P1.printName()

P1.LearnPython()

H1 = HR("Arham")
H1.printName()

H1.ManageHR()
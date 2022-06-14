class Shapes:
    def __init__(self, length):
        self.length = length
    def area(self):
        print("Area of sqr = ", self.length * self.length)

class Rectangle(Shapes):
    def __init__(self, length, breadth):
        super().__init__(length)
        self.breadth = breadth
    def area(self):
        super().area()
        return "Area of rect", self.length * self.breadth

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

a2 = Rectangle(length, breadth)
print(a2.area())
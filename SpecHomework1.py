import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
     """Method documentation"""
     return

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim

# New classes added from UML diagram
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print("Consider me implemented", perim)
        return perim

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

# Instance of each new class and result of the calc_perimeter method
rect = Rectangle(10, 5)
rect.calc_perimeter()

square = Square(7)
square.calc_perimeter()